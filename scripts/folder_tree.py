import os
import pathlib
from typing import List, Optional

from rich.console import Console
from rich.tree import Tree
from rich.text import Text
from rich.style import Style


def visualize_folder_structure_rich(
    start_path: str, max_depth: Optional[int] = None, exclude_patterns: Optional[List[str]] = None
) -> None:
    """
    지정된 경로의 폴더 구조를 rich 라이브러리를 사용하여 시각화하여 출력합니다.

    Args:
        start_path (str): 시각화를 시작할 루트 폴더 경로.
        max_depth (int, optional): 탐색할 최대 깊이 (루트 폴더는 0). None이면 제한 없음.
        exclude_patterns (list, optional): 제외할 폴더/파일 이름 패턴 리스트 (예: ['.venv', '__pycache__']).
                                          정확한 이름 일치를 권장합니다.
    """
    console = Console()

    if not os.path.isdir(start_path):
        console.print(f"[bold red]오류:[/bold red] '{start_path}'는 유효한 디렉토리가 아닙니다.")
        return

    start_path_obj = pathlib.Path(start_path)
    console.print(
        f"[bold blue]--- 폴더 구조 시각화 시작: {start_path_obj.resolve()} ---[/bold blue]"
    )

    # 제외 패턴을 집합(set)으로 변환하여 검색 속도 향상
    exclude_set = set(exclude_patterns) if exclude_patterns else set()

    # Rich Tree 객체 생성 (루트 노드)
    # 루트 폴더는 파란색 아이콘과 굵은 글씨로 표시
    rich_tree = Tree(
        Text(f"{start_path_obj.name}/", style="bold green"),  # 루트 폴더는 초록색
        guide_style=Style(color="white"),
    )

    # 재귀 함수 정의
    def _add_nodes(current_node: Tree, current_path: pathlib.Path, current_depth: int) -> None:
        if max_depth is not None and current_depth > max_depth:
            return

        # 현재 경로의 항목들을 정렬 (폴더 먼저, 그 다음 파일 - 이름순)
        items = sorted(list(current_path.iterdir()), key=lambda p: (not p.is_dir(), p.name.lower()))

        for item in items:
            # 제외 패턴에 해당하는 항목은 건너뛰기
            if item.name in exclude_set:
                continue

            if item.is_dir():
                # 폴더는 파란색 아이콘과 굵은 글씨
                folder_text = Text(f"{item.name}/", style="bold deep_sky_blue1")
                folder_branch = current_node.add(folder_text)
                _add_nodes(folder_branch, item, current_depth + 1)
            else:
                # 파일 아이콘과 색상 (예: .py는 노란색, .txt는 흰색 등)
                file_icon = "📄"  # 기본 파일 아이콘
                file_style = "white"

                if item.suffix == ".py":
                    file_icon = "🐍"
                    file_style = "yellow"
                elif item.suffix in [".txt", ".md", ".json", ".yml", ".yaml"]:
                    file_icon = "📝"
                    file_style = "cyan"
                elif item.suffix in [".png", ".jpg", ".jpeg", ".gif"]:
                    file_icon = "🖼️"
                    file_style = "magenta"
                elif item.suffix in [".zip", ".tar", ".gz"]:
                    file_icon = "📦"
                    file_style = "orange4"
                elif item.suffix == ".html":
                    file_icon = "🌐"
                    file_style = "dark_red"
                elif item.suffix == ".css":
                    file_icon = "🎨"
                    file_style = "deep_sky_blue3"
                elif item.suffix == ".js":
                    file_icon = "💡"
                    file_style = "bright_yellow"
                elif item.suffix == ".csv":
                    file_icon = "📊"
                    file_style = "green4"

                file_text = Text(f"{file_icon} {item.name}", style=file_style)
                current_node.add(file_text)

    # 루트 노드부터 시작하여 트리 구성
    _add_nodes(rich_tree, start_path_obj, 0)

    # Rich 콘솔에 트리 출력
    console.print(rich_tree)
    console.print("[bold blue]--- 시각화 완료 ---[/bold blue]")


if __name__ == "__main__":
    # 시각화할 시작 경로 설정 (현재 디렉토리)
    folder_to_visualize = "."

    # 제외할 폴더/파일 패턴 리스트
    excluded_list = [
        ".venv",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__",
        ".git",
        ".vscode",
        "reports",
        ".coverage",
        ".github",
        ".mypy_cache",
        ".DS_Store",  # macOS 특정 파일
    ]

    # 예제 사용법
    print("\n--- 기본 시각화 (깊이 제한 없음) ---")
    visualize_folder_structure_rich(folder_to_visualize, exclude_patterns=excluded_list)

    # print("\n--- 최대 깊이 1로 제한 ---")
    # visualize_folder_structure_rich(folder_to_visualize, max_depth=1, exclude_patterns=excluded_list)

    # print("\n--- 특정 폴더 시각화 (예시) ---")
    # try:
    #     os.makedirs("./temp_test_dir/sub_folder/another_sub", exist_ok=True)
    #     with open("./temp_test_dir/file1.txt", "w") as f: f.write("test")
    #     with open("./temp_test_dir/sub_folder/file2.py", "w") as f: f.write("test")
    #     with open("./temp_test_dir/image.png", "w") as f: f.write("test")
    #     visualize_folder_structure_rich("./temp_test_dir", max_depth=2, exclude_patterns=[])
    # finally:
    #     import shutil
    #     if os.path.exists("./temp_test_dir"):
    #         shutil.rmtree("./temp_test_dir")
