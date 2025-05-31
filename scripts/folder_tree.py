import os
import pathlib
from typing import List, Optional
import fnmatch  # fnmatch 모듈 추가

from rich.console import Console
from rich.tree import Tree
from rich.text import Text
from rich.style import Style


def visualize_folder_structure_rich(
    start_path: str, max_depth: Optional[int] = None, exclude_patterns: Optional[List[str]] = None
) -> None:
    """
    지정된 경로의 폴더 구조를 rich 라이브러리를 사용하여 시각화하여 출력합니다.
    제외할 폴더/파일 이름에 와일드카드 패턴을 지원합니다.

    Args:
        start_path (str): 시각화를 시작할 루트 폴더 경로.
        max_depth (int, optional): 탐색할 최대 깊이 (루트 폴더는 0). None이면 제한 없음.
        exclude_patterns (list, optional): 제외할 폴더/파일 이름 패턴 리스트 (예: ['.venv', '__pycache__', 'data/*', '*.log']).
                                         Unix 쉘 스타일의 와일드카드 패턴을 지원합니다.
    """
    console = Console()

    if not os.path.isdir(start_path):
        console.print(f"[bold red]오류:[/bold red] '{start_path}'는 유효한 디렉토리가 아닙니다.")
        return

    start_path_obj = pathlib.Path(start_path)
    console.print(
        f"[bold blue]--- 폴더 구조 시각화 시작: {start_path_obj.resolve()} ---[/bold blue]"
    )

    _exclude_patterns = exclude_patterns if exclude_patterns else []

    rich_tree = Tree(
        Text(f"{start_path_obj.name}/", style="bold green"),
        guide_style=Style(color="white"),
    )

    def _add_nodes(current_node: Tree, current_path: pathlib.Path, current_depth: int) -> None:
        if max_depth is not None and current_depth > max_depth:
            return

        items = sorted(list(current_path.iterdir()), key=lambda p: (not p.is_dir(), p.name.lower()))

        for item in items:
            is_excluded = False
            item_relative_path_str = str(item.relative_to(start_path_obj))

            # **핵심 변경 부분: __pycache__와 같은 특정 이름의 폴더를 재귀적으로 제외**
            # 현재 아이템의 이름이 제외 목록에 직접 있는 경우 (e.g., '__pycache__')
            if item.is_dir() and item.name in _exclude_patterns:
                is_excluded = True

            # 패턴 매칭 (data/*, logs/*, *.log 등)
            if not is_excluded:  # 위에서 이미 제외되지 않았다면
                for pattern in _exclude_patterns:
                    # 'data/'와 같은 폴더 자체 매칭 (정확한 폴더 경로 + 슬래시)
                    if (
                        item.is_dir()
                        and fnmatch.fnmatch(item_relative_path_str + "/", pattern)
                        and pattern.endswith("/")
                    ):
                        is_excluded = True
                        break
                    # 파일 또는 폴더의 상대 경로 매칭
                    elif fnmatch.fnmatch(item_relative_path_str, pattern):
                        is_excluded = True
                        break

            if is_excluded:
                continue

            if item.is_dir():
                folder_text = Text(f"{item.name}/", style="bold deep_sky_blue1")
                folder_branch = current_node.add(folder_text)
                _add_nodes(folder_branch, item, current_depth + 1)
            else:
                file_icon = "📄"
                file_style = "white"

                if item.suffix == ".py":
                    file_icon = "🐍"
                    file_style = "yellow"
                elif item.suffix in [".txt", ".md", ".json", ".yml", ".yaml", ".lock"]:
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
                elif item.name == ".gitkeep":
                    file_icon = "📭"
                    file_style = "dim white"
                elif item.name.startswith("."):
                    file_icon = "🕵️‍♀️"
                    file_style = "dim white"

                file_text = Text(f"{file_icon} {item.name}", style=file_style)
                current_node.add(file_text)

    _add_nodes(rich_tree, start_path_obj, 0)

    console.print(rich_tree)
    console.print("[bold blue]--- 시각화 완료 ---[/bold blue]")


if __name__ == "__main__":
    folder_to_visualize = "."

    excluded_list = [
        ".venv",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__",  # 이 부분이 이제 item.name과 직접 매칭됩니다.
        ".git",
        ".vscode",
        "reports",
        ".coverage",
        ".github",
        ".mypy_cache",
        ".DS_Store",
        "data/raw/*",  # data 폴더 아래의 모든 파일/폴더 (data 폴더 자체는 보임)
        "data/processed/*",  # data 폴더 아래의 processed 폴더의 모든 파일/폴더
        "logs/*",  # logs 폴더 아래의 모든 파일/폴더
        "outputs/*",  # outputs 폴더 아래의 모든 파일/폴더
        "*.log",  # 모든 .log 파일 제외 (outputs/날짜/main.log 등)
        "*.pyc",  # 모든 .pyc 파일 제외
        "docs/추가할거.md",  # docs 폴더 아래의 특정 파일 제외
        "*/.gitkeep",  # .gitkeep 파일 제외
    ]

    print("\n--- 기본 시각화 (깊이 제한 없음) ---")
    visualize_folder_structure_rich(
        folder_to_visualize, max_depth=2, exclude_patterns=excluded_list
    )

'''
import os
import pathlib
from typing import List, Optional
import re # 정규표현식 모듈 추가

from rich.console import Console
from rich.tree import Tree
from rich.text import Text
from rich.style import Style


def visualize_folder_structure_rich(
    start_path: str, max_depth: Optional[int] = None, exclude_patterns: Optional[List[str]] = None
) -> None:
    """
    지정된 경로의 폴더 구조를 rich 라이브러리를 사용하여 시각화하여 출력합니다.
    제외할 폴더/파일 이름에 와일드카드 패턴을 지원합니다.

    Args:
        start_path (str): 시각화를 시작할 루트 폴더 경로.
        max_depth (int, optional): 탐색할 최대 깊이 (루트 폴더는 0). None이면 제한 없음.
        exclude_patterns (list, optional): 제외할 폴더/파일 이름 패턴 리스트 (예: ['.venv', '__pycache__', 'data/*', '*.log']).
                                         Unix 쉘 스타일의 와일드카드 패턴을 지원합니다.
    """
    console = Console()

    if not os.path.isdir(start_path):
        console.print(f"[bold red]오류:[/bold red] '{start_path}'는 유효한 디렉토리가 아닙니다.")
        return

    start_path_obj = pathlib.Path(start_path)
    console.print(
        f"[bold blue]--- 폴더 구조 시각화 시작: {start_path_obj.resolve()} ---[/bold blue]"
    )

    # 제외 패턴을 None이 아니면 리스트로 변환
    # re.compile을 사용하면 반복적인 패턴 매칭 성능을 향상시킬 수 있지만,
    # 여기서는 pathlib.Path.match()의 간단한 glob 스타일 패턴을 사용합니다.
    # 만약 re.compile을 사용하고 싶다면, glob 패턴을 정규 표현식으로 변환하는 과정이 필요합니다.
    # 현재는 pathlib.Path.match()가 더 적합합니다.
    _exclude_patterns = exclude_patterns if exclude_patterns else []


    # Rich Tree 객체 생성 (루트 노드)
    # 루트 폴더는 초록색
    rich_tree = Tree(
        Text(f"{start_path_obj.name}/", style="bold green"),
        guide_style=Style(color="white"),
    )

    # 재귀 함수 정의
    def _add_nodes(current_node: Tree, current_path: pathlib.Path, current_depth: int) -> None:
        if max_depth is not None and current_depth > max_depth:
            return

        # 현재 경로의 항목들을 정렬 (폴더 먼저, 그 다음 파일 - 이름순)
        # .gitkeep 파일은 항상 마지막에 오도록 정렬 규칙 추가 (선택 사항)
        items = sorted(list(current_path.iterdir()), key=lambda p: (not p.is_dir(), p.name == '.gitkeep', p.name.lower()))

        for item in items:
            # 제외 패턴에 해당하는 항목은 건너뛰기
            # item.match()를 사용하여 와일드카드 패턴 매칭
            is_excluded = False
            for pattern in _exclude_patterns:
                # 폴더인 경우 패턴이 '/'로 끝나면 폴더 자체를 제외 (예: 'data/')
                # 파일인 경우 또는 폴더 내부의 모든 것을 제외할 경우 (예: 'data/*')
                if item.is_dir():
                    if pattern.endswith('/') and item.match(pattern): # 'data/'와 같은 패턴 매치
                        is_excluded = True
                        break
                    elif pattern.endswith('/*') and item.match(pattern.rstrip('/\\')): # 'data/*'와 같은 패턴 매치
                        # 'data/*'는 'data' 폴더 자체를 제외하는 것이 아니라 'data' 내부를 제외하는 것이므로,
                        # 이 경우 item.name이 pattern.split('/')[0]과 일치하는지 확인
                        # 하지만 가장 간단한 방법은 'data/*'를 'data'로 처리하고
                        # 그 아래의 모든 것을 재귀적으로 무시하는 것입니다.
                        pass # 아래의 glob_match_current_level 에서 처리

                # glob.glob 스타일 매칭: 현재 item.name에 대해 패턴과 일치하는지 확인
                # item.name과 pattern을 직접 매칭하는 방식
                if item.match(pattern) or item.match(pattern.rstrip('/\\')): # 'data' or 'data/' or 'data/*'
                    is_excluded = True
                    break

                # 추가: 부모 경로까지 고려한 패턴 (예: 'data/raw/*')
                # 이 로직은 `exclude_patterns`에 전체 경로 패턴이 들어올 경우를 대비합니다.
                # 현재는 `item.name` (항목 이름) 기준으로만 매칭하므로,
                # 'data/raw/*'와 같은 패턴은 `start_path`가 '/'일 때만 작동합니다.
                # 더 복잡한 패턴 매칭을 원한다면 `fnmatch`나 `re` 모듈을 고려해야 합니다.
                if item.relative_to(start_path_obj).match(pattern):
                     is_excluded = True
                     break

            if is_excluded:
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
    # 'data/*'는 'data' 폴더 바로 아래의 모든 것을 의미합니다.
    # 'data'는 'data' 폴더 자체를 의미합니다.
    # '__pycache__'는 모든 '__pycache__' 폴더를 의미합니다.
    excluded_list = [
        ".venv",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__", # 모든 __pycache__ 폴더를 제외
        ".git",
        ".vscode",
        "reports",
        ".coverage",
        ".github",
        ".mypy_cache",
        ".DS_Store",  # macOS 특정 파일
        "data",       # data 폴더 자체와 그 내부 모든 것을 제외하려면 'data'
        # 또는 'data/*'로 data 폴더 자체는 포함하고 그 하위만 제외
        # 만약 data 폴더는 보이되, 그 안의 raw/ 와 processed/ 만 안보이게 하려면,
        # exclude_patterns 에 'data/raw', 'data/processed' 를 추가해야 합니다.
        # 이 함수는 각 항목의 이름과 패턴을 매칭합니다.
        # 즉, 'data/raw'를 exclude_patterns에 넣었다면, _add_nodes에서 item.name이 'raw'일 때
        # 해당 패턴과 매칭되는지를 확인해야 합니다.
        # 현재 코드에서는 item.name만으로 매칭하기 때문에,
        # 'data' 폴더를 제외하려면 'data'를 제외 패턴에 넣으면 됩니다.
        # 'data/*' 패턴은 'data' 폴더의 직계 자식에 대해서만 매칭됩니다.
    ]

    # 'data' 폴더 자체를 제외하고 싶다면 excluded_list에 'data'를 넣으세요.
    # 만약 'data' 폴더는 보이되, 그 하위 내용만 제외하고 싶다면,
    # 'data/raw'와 'data/processed'를 제외 목록에 추가하는 것이 더 적합합니다.
    # 이 경우 'data' 폴더 자체는 트리에서 보이지만, 그 아래 내용은 보이지 않습니다.
    excluded_list_for_data_content = [
        ".venv", ".pytest_cache", ".ruff_cache", "__pycache__", ".git",
        ".vscode", "reports", ".coverage", ".github", ".mypy_cache", ".DS_Store",
        "raw",       # 'data/raw' 폴더가 아닌, 모든 'raw' 이름의 폴더를 제외 (주의!)
        "processed", # 'data/processed' 폴더가 아닌, 모든 'processed' 이름의 폴더를 제외 (주의!)
    ]
    # 위 방식은 `raw`나 `processed`라는 이름의 다른 폴더도 제외할 수 있으므로 주의해야 합니다.
    # 더 정확한 방법은 `pathlib.Path.relative_to(start_path_obj)`를 활용하여
    # 전체 경로를 기준으로 패턴 매칭을 하는 것입니다.
    # 하지만 현재 함수는 `item.name`만을 기반으로 하므로,
    # `raw`, `processed`를 제외 패턴에 넣으면 `data/raw`와 `data/processed`가 제외됩니다.

    print("\n--- 기본 시각화 (깊이 제한 없음) ---")
    visualize_folder_structure_rich(folder_to_visualize, exclude_patterns=excluded_list)

    print("\n--- data 폴더의 내용을 제외하는 시각화 (예시) ---")
    # 'data' 폴더는 보이되, 그 하위인 'raw'와 'processed'를 제외
    excluded_for_selective_data = [
        ".venv", "__pycache__", ".git", ".vscode", ".DS_Store",
        "raw",        # 'data/raw'를 제외
        "processed",  # 'data/processed'를 제외
        "cifar-10-batches-py", # 'data/raw/cifar-10-batches-py' 도 제외 (특정 데이터셋)
    ]
    visualize_folder_structure_rich(folder_to_visualize, exclude_patterns=excluded_for_selective_data)

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
'''
