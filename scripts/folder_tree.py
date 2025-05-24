import os
import pathlib


def visualize_folder_structure(start_path, max_depth=None, exclude_patterns=None):
    """
    지정된 경로의 폴더 구조를 트리 형태로 시각화하여 출력합니다.

    Args:
        start_path (str): 시각화를 시작할 루트 폴더 경로.
        max_depth (int, optional): 탐색할 최대 깊이 (루트 폴더는 0). None이면 제한 없음.
        exclude_patterns (list, optional): 제외할 폴더/파일 이름 패턴 리스트 (예: ['.venv', '__pycache__']).
                                          부분 일치보다는 정확한 이름 일치를 권장합니다.
    """
    if not os.path.isdir(start_path):
        print(f"오류: '{start_path}'는 유효한 디렉토리가 아닙니다.")
        return

    start_path_obj = pathlib.Path(start_path)
    print(f"--- 폴더 구조 시각화 시작: {start_path_obj.resolve()} ---")

    # 제외 패턴을 집합(set)으로 변환하여 검색 속도 향상
    exclude_set = set(exclude_patterns) if exclude_patterns else set()

    # 재귀 함수 정의
    def _print_tree(current_path, current_depth):
        if max_depth is not None and current_depth > max_depth:
            return

        # 현재 깊이에 따른 들여쓰기 접두사 생성
        # 예: ├── (마지막이 아닌 항목), └── (마지막 항목), │ (연결선)
        prefix = "│   " * current_depth
        item_prefix = "├── "  # 기본 접두사

        items = sorted(list(current_path.iterdir()), key=lambda p: (not p.is_dir(), p.name.lower()))

        for i, item in enumerate(items):
            # 제외 패턴에 해당하는 항목은 건너뛰기
            if item.name in exclude_set:
                continue

            is_last_item = i == len(items) - 1  # 현재 아이템이 리스트의 마지막인지 확인

            # 마지막 항목이면 '└── ', 아니면 '├── '
            item_prefix = "└── " if is_last_item else "├── "

            # 폴더인지 파일인지 구분하여 출력
            if item.is_dir():
                print(f"{prefix}{item_prefix}{item.name}/")
                # 다음 재귀 호출 시, 마지막 아이템이면 빈 줄 추가
                if is_last_item:
                    _print_tree(item, current_depth + 1)
                else:
                    _print_tree(item, current_depth + 1)
            else:
                print(f"{prefix}{item_prefix}{item.name}")

    # 루트 폴더 자체는 들여쓰기 없이 출력
    print(".")  # 현재 디렉토리를 나타내는 . 또는 start_path_obj.name
    # 재귀 함수 호출
    _print_tree(start_path_obj, 0)  # 루트는 0 깊이부터 시작

    print("--- 시각화 완료 ---")


if __name__ == "__main__":
    # 시각화할 시작 경로 설정 (현재 디렉토리)
    # 이 스크립트를 실행하는 위치의 폴더 구조를 보여줍니다.
    # 특정 폴더를 지정하려면: folder_to_visualize = "/path/to/your/folder"
    folder_to_visualize = "."

    # 제외할 폴더/파일 패턴 리스트 (추가하고 싶은 것이 있다면 여기에 추가)
    # .venv, .pytest_cache, .ruff_cache 등 캐시/가상 환경 폴더를 제외합니다.
    excluded_list = [
        ".venv",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__",
        ".git",  # Git 관련 내부 폴더
        ".vscode",  # VS Code 설정 폴더
        "reports",  # 보고서 폴더
        ".coverage",  # 코드 커버리지 파일,
        "reports",  # 보고서 폴더
        ".github",  # GitHub 관련 폴더
        ".mypy_cache",  # mypy 캐시 폴더
    ]

    # 시각화 실행 (최대 깊이 3으로 제한)
    # visualize_folder_structure(folder_to_visualize, max_depth=3, exclude_patterns=excluded_list)

    # 또는 깊이 제한 없이 전체 구조 보기
    visualize_folder_structure(folder_to_visualize, exclude_patterns=excluded_list)

    # 특정 깊이까지 제한하고 싶다면 아래 주석 해제
    # visualize_folder_structure(folder_to_visualize, max_depth=2, exclude_patterns=excluded_list)
