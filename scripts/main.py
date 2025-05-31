# scripts/main.py
import hydra
from omegaconf import DictConfig, OmegaConf
import torch
import random
import numpy as np
import os  # 데이터셋 다운로드 경로 생성용

# Trainer 클래스 임포트
from my_template.training.Trainer import SupervisedTrainer
# ConfigManager 임포트 (Pydantic 미사용 시 단순 플레이스홀더 역할)
# Logger 임포트 (현재는 Trainer에서 직접 print 사용)
# from src.my_template.utils.Logger import Logger


# 시드 고정 함수 (재현성 확보)
def set_seed(seed: int = 42) -> None:
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    np.random.seed(seed)
    random.seed(seed)


@hydra.main(config_path="../config", config_name="config", version_base="1.3")
def main(cfg: DictConfig) -> None:
    # 설정 내용 출력 (디버깅용)
    print("\n--- Loaded Configuration ---")
    print(OmegaConf.to_yaml(cfg))
    print("----------------------------\n")

    # 1. ConfigManager를 통한 설정 유효성 검사 (현재는 비활성화/스킵)

    # 2. 글로벌 설정 적용
    set_seed(cfg.global_setting.seed)
    print(f"Global_setting seed set to: {cfg.global_setting.seed}")
    print(f"Using device: {cfg.global_setting.device}")

    # 3. 데이터 폴더 생성 (CIFAR-10 다운로드 경로)
    os.makedirs(cfg.dataset.dataset.root, exist_ok=True)

    # 4. 모델 인스턴스화
    model_instance = hydra.utils.instantiate(cfg.model)
    print(f"Instantiated Model: {type(model_instance).__name__}")

    # 5. 옵티마이저 인스턴스화 (모델 파라미터 전달)
    optimizer_instance = hydra.utils.instantiate(
        cfg.training.optimizer, params=model_instance.parameters()
    )
    print(f"Instantiated Optimizer: {type(optimizer_instance).__name__}")

    # 6. 손실 함수 인스턴스화
    loss_fn_instance = hydra.utils.instantiate(cfg.training.loss)
    print(f"Instantiated Loss Function: {type(loss_fn_instance).__name__}")

    # 7. 데이터로더 인스턴스화
    # dataset 그룹 내의 train_dataloader 및 val_dataloader를 직접 참조
    train_dataloader_instance = hydra.utils.instantiate(cfg.dataset.train_dataloader)
    val_dataloader_instance = hydra.utils.instantiate(cfg.dataset.val_dataloader)
    print(
        f"Instantiated Train DataLoader: {type(train_dataloader_instance).__name__} with batch_size={train_dataloader_instance.batch_size}"
    )
    print(
        f"Instantiated Validation DataLoader: {type(val_dataloader_instance).__name__} with batch_size={val_dataloader_instance.batch_size}"
    )

    # 8. Trainer 인스턴스화 및 컴포넌트 주입
    trainer = SupervisedTrainer(
        model=model_instance,
        optimizer=optimizer_instance,
        loss_fn=loss_fn_instance,
        train_dataloader=train_dataloader_instance,
        val_dataloader=val_dataloader_instance,
        cfg=cfg,  # 전체 설정을 Trainer에 전달
    )

    # 9. 학습 시작
    trainer.train()


if __name__ == "__main__":
    main()
