# src/my_template/training/Trainer.py
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from omegaconf import DictConfig

# rich 라이브러리 임포트
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    SpinnerColumn,
)
from rich.text import Text
from rich.style import Style


class SupervisedTrainer:
    def __init__(
        self,
        model: nn.Module,
        optimizer: optim.Optimizer,
        loss_fn: nn.Module,
        train_dataloader: DataLoader,
        val_dataloader: DataLoader,
        cfg: DictConfig,  # 전체 설정을 받아서 사용
    ):
        self.cfg = cfg
        self.device = torch.device(self.cfg.global_setting.device)
        self.model = model.to(self.device)
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.train_dataloader = train_dataloader
        self.val_dataloader = val_dataloader
        self.num_epochs = self.cfg.global_setting.num_epochs
        self.log_interval = self.cfg.training.trainer.log_interval
        self.eval_interval = self.cfg.training.trainer.eval_interval

        # rich 콘솔 객체 생성
        self.console = Console()

        # --- Trainer Initialized 정보 출력 (Table 사용) ---
        trainer_info_table = Table(
            title=Text("Trainer Initialized", style="bold green"),
            show_header=False,
            row_styles=["none", "dim"],
            box=None,  # Box 스타일 제거
        )
        trainer_info_table.add_column("Property", style="bold cyan")
        trainer_info_table.add_column("Value", style="yellow")

        trainer_info_table.add_row("Model", type(self.model).__name__)
        trainer_info_table.add_row("Optimizer", type(self.optimizer).__name__)
        trainer_info_table.add_row("Loss Function", type(self.loss_fn).__name__)
        trainer_info_table.add_row("Device", str(self.device))
        trainer_info_table.add_row("Epochs", str(self.num_epochs))
        trainer_info_table.add_row("Log Interval", str(self.log_interval))
        trainer_info_table.add_row("Eval Interval", str(self.eval_interval))

        self.console.print(Panel(trainer_info_table, border_style="green", expand=False))

        # --- (핵심) 모델 커스터마이징을 위한 확장점 ---
        if hasattr(self.cfg.model, "num_classes") and isinstance(self.model, nn.Module):
            adjusted = False
            if hasattr(self.model, "fc") and isinstance(self.model.fc, nn.Linear):
                self.console.print(
                    f"[bold blue]INFO:[/bold blue] Adjusting [bold magenta]{type(self.model).__name__}.fc[/bold magenta] layer to {self.cfg.model.num_classes} classes."
                )
                self.model.fc = nn.Linear(self.model.fc.in_features, self.cfg.model.num_classes).to(
                    self.device
                )
                adjusted = True
            elif hasattr(self.model, "classifier") and isinstance(
                self.model.classifier, nn.Sequential
            ):
                last_layer_idx = len(self.model.classifier) - 1
                if isinstance(self.model.classifier[last_layer_idx], nn.Linear):
                    self.console.print(
                        f"[bold blue]INFO:[/bold blue] Adjusting [bold magenta]{type(self.model).__name__}.classifier[/bold magenta] layer to {self.cfg.model.num_classes} classes."
                    )
                    self.model.classifier[last_layer_idx] = nn.Linear(
                        self.model.classifier[last_layer_idx].in_features,
                        self.cfg.model.num_classes,
                    ).to(self.device)
                    adjusted = True

            if not adjusted:
                self.console.print(
                    f"[bold yellow]WARNING:[/bold yellow] Model {type(self.model).__name__} has [bold red]no identifiable 'fc' or 'classifier' layer[/bold red] for automatic adjustment. Manual adjustment may be required."
                )
        # ---------------------------------------------

    def _train_one_epoch(self, epoch: int, task_description: Text):
        self.model.train()
        running_loss = 0.0

        # rich Progress bar for training
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=None),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            SpinnerColumn(spinner_name="dots"),
            TimeRemainingColumn(),
            TimeElapsedColumn(),
            console=self.console,
        ) as progress:
            train_task = progress.add_task(task_description, total=len(self.train_dataloader))

            for batch_idx, (inputs, labels) in enumerate(self.train_dataloader):
                inputs, labels = inputs.to(self.device), labels.to(self.device)

                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.loss_fn(outputs, labels)
                loss.backward()
                self.optimizer.step()

                running_loss += loss.item()

                if (batch_idx + 1) % self.log_interval == 0:
                    avg_loss = running_loss / self.log_interval
                    self.console.print(
                        f"  [bold blue]Epoch {epoch + 1}/{self.num_epochs}[/bold blue], "
                        f"Batch [bold cyan]{batch_idx + 1}/{len(self.train_dataloader)}[/bold cyan], "
                        f"Loss: [bold red]{avg_loss:.4f}[/bold red]"
                    )
                    running_loss = 0.0

                progress.update(train_task, advance=1)

    def _validate_one_epoch(self, epoch: int):
        self.model.eval()
        total_loss = 0.0
        correct = 0
        total = 0

        self.console.print(
            f"\n[bold yellow]Performing Validation for Epoch {epoch + 1}...[/bold yellow]"
        )

        with torch.no_grad():
            for inputs, labels in self.val_dataloader:
                inputs, labels = inputs.to(self.device), labels.to(self.device)
                outputs = self.model(inputs)
                loss = self.loss_fn(outputs, labels)
                total_loss += loss.item()

                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        avg_loss = total_loss / len(self.val_dataloader)
        accuracy = 100 * correct / total
        self.console.print(
            f"[bold green]Epoch {epoch + 1}/{self.num_epochs}[/bold green] - "
            f"Validation Loss: [bold red]{avg_loss:.4f}[/bold red], "
            f"Accuracy: [bold magenta]{accuracy:.2f}%[/bold magenta]\n"
        )
        return avg_loss, accuracy

    def train(self):
        self.console.print(
            Panel(
                Text("Starting Training", style="bold underline blue"),
                border_style="blue",
                expand=False,
            )
        )

        for epoch in range(self.num_epochs):
            self.console.print(
                f"\n[bold white on blue] Epoch {epoch + 1}/{self.num_epochs} [/bold white on blue]"
            )
            self._train_one_epoch(epoch, Text(f"Training Epoch {epoch + 1}", style="bold green"))

            if (epoch + 1) % self.eval_interval == 0:
                self._validate_one_epoch(epoch)

        self.console.print(
            Panel(
                Text("Training Finished", style="bold underline green"),
                border_style="green",
                expand=False,
            )
        )
