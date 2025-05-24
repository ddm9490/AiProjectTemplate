---

# 🚀 AI 프로젝트 템플릿

이 템플릿은 PyTorch 기반의 AI 모델 개발을 위한 **체계적이고 효율적인 시작점**을 제공합니다. 복잡한 초기 설정과 인프라 구성에 드는 시간을 최소화하고, 사용자가 **핵심 AI/ML 로직 개발에만 집중**할 수 있도록 설계되었습니다.

---

## ✨ 주요 기능

이 템플릿은 AI/ML 프로젝트의 생명주기 전반을 아우르는 강력한 기능들을 통합합니다:

* **PyTorch 기반 모델 개발**: 딥러닝 모델 개발을 위한 강력한 PyTorch 프레임워크를 기반으로 합니다.
* **체계적인 모델 학습 관리**:
    * **Apache Airflow**: 데이터 준비, 모델 학습, 평가, 배포 등 복잡한 ML 파이프라인의 워크플로우를 정의하고 자동화할 수 있도록 지원합니다.
    * **MLflow**: 모델 학습 실험 추적 (메트릭, 파라미터, 아티팩트 로깅), 모델 관리, 그리고 배포를 위한 통합 플랫폼을 제공합니다.
* **직관적인 시각화 및 디버깅**:
    * **TensorBoard**: 모델 학습 과정의 메트릭, 그래프, 이미지 등 다양한 정보를 시각화하여 학습 상황을 직관적으로 이해하고 디버깅하는 데 도움을 줍니다.
* **모듈화된 코드 구조**:
    * `src/my_template/` 내부에 `abc_interfaces`, `data`, `models`, `training` 등 명확하게 구분된 모듈들을 통해 코드의 재사용성과 유지보수성을 높입니다.
    * 특히 `abc_interfaces`를 통해 필수적으로 구현해야 할 메서드를 정의함으로써, 일관된 개발 패턴을 유도하고 사용자에게 명확한 가이드를 제공합니다.
* **강력한 코드 품질 및 테스트 워크플로우**:
    * `ruff` (린터/포매터), `pytest` (테스트 프레임워크), `pre-commit` (Git 훅)이 통합되어 코드를 커밋하기 전에 자동으로 품질 검사 및 포매팅, 그리고 테스트를 수행합니다. 이를 통해 깨끗하고 잘 작동하는 코드만 저장소에 반영됩니다.

---

## 📚 프로젝트 구조

이 템플릿은 AI 개발 워크플로우를 효율적으로 관리하고 확장할 수 있도록 설계된 체계적인 폴더 구조를 갖추고 있습니다.

```
.
├── checkpoints/          # 모델 체크포인트 저장 디렉토리
├── config/               # 애플리케이션 및 모델 설정 파일
│   ├── config.yaml       # 주요 설정 파일
│   └── config_model.py   # 모델 관련 설정 (코드 형태)
├── data/                 # 데이터 저장 디렉토리
│   ├── processed/        # 전처리된 데이터
│   └── raw/              # 원본 데이터
├── docs/                 # 프로젝트 문서 (사용 가이드, API 문서 등)
├── experiments/          # MLflow 등 실험 추적 결과 저장
├── logs/                 # 애플리케이션 및 모델 학습 로그
├── notebooks/            # Jupyter Notebook 파일
│   ├── .ipynb_checkpoints/ # 노트북 임시 저장 파일
│   └── main.ipynb        # 주요 데이터 탐색, 모델 프로토타이핑 노트북
├── outputs/              # 모델 추론 결과, 시각화 등 최종 결과물
├── scripts/              # 유틸리티 스크립트 및 진입점
│   ├── folder_tree.py    # 폴더 구조 시각화 스크립트 (개발 편의용)
│   └── main.py           # 애플리케이션의 주요 실행 진입점 (예: 학습, 추론)
├── src/                  # 핵심 소스 코드 디렉토리
│   └── my_template/      # 프로젝트의 Python 패키지
│       ├── abc_interfaces/ # 추상 기본 클래스(ABC) 인터페이스 정의
│       │   ├── data_interfaces.py
│       │   ├── model_interfaces.py
│       │   ├── training_interfaces.py
│       │   └── utils_interfaces.py
│       ├── data/         # 데이터 로딩, 전처리, 시각화 관련 모듈
│       │   ├── DataLoader.py
│       │   ├── DataProcessor.py
│       │   ├── Dataset.py
│       │   └── DataVisualizer.py
│       ├── models/       # 모델 정의 및 아키텍처
│       │   └── Model.py
│       ├── training/     # 모델 학습 및 평가 파이프라인
│       │   ├── CallBacks/    # 학습 콜백 함수 (예: EarlyStopping)
│       │   ├── losses/       # 손실 함수 정의
│       │   ├── optimizers/   # 옵티마이저 정의
│       │   ├── Evaluator.py
│       │   ├── ExperimentManager.py
│       │   ├── PipeLine.py
│       │   ├── Trainer.py
│       │   ├── TrainVisualizer.py
│       │   └── Tuner.py
│       └── utils/        # 공통 유틸리티 함수 및 헬퍼 모듈 (주로 템플릿 제공)
│           ├── Config.py
│           ├── ConfigurationManager.py
│           ├── Logger.py
│           ├── Saver.py
│           └── UtilityManager.py
├── tests/                # 테스트 코드 디렉토리
│   ├── integration/      # 통합 테스트
│   │   ├── test_data_pipeline.py
│   │   ├── test_inference.py
│   │   └── test_model_training.py
│   ├── unit/             # 단위 테스트 (세부 모듈별)
│   │   ├── data/
│   │   ├── models/
│   │   ├── training/
│   │   └── utils/
│   ├── conftest.py       # pytest 설정 및 픽스처
│   └── run_test.py       # 테스트 실행 스크립트 (선택 사항)
├── .env                  # 환경 변수 (민감 정보 등)
├── .gitignore            # Git 버전 관리에서 제외할 파일/폴더
├── .pre-commit-config.yaml # Git 커밋 훅 설정
├── poetry.lock           # Poetry 의존성 잠금 파일
├── pyproject.toml        # 프로젝트 메타데이터 및 Poetry/도구 설정
├── README.md             # 프로젝트 개요 및 사용 가이드
└── requirements.txt      # Poetry 사용 전 환경 호환성을 위한 (선택 사항)
```

---

## 🚀 프로젝트 시작하기: 의존성 설치 및 개발 환경 설정

이 프로젝트 템플릿은 **Poetry**를 사용하여 의존성을 관리하고 개발 환경을 설정합니다. Poetry는 일관된 개발 환경을 구축하고, 린트, 테스트, 코드 포매팅과 같은 중요한 개발 워크플로우를 자동화하는 데 필수적인 도구입니다.

### 1단계: Poetry 설치

아직 시스템에 Poetry가 설치되어 있지 않다면, 다음 명령어를 사용하여 설치하세요.

```bash
# macOS / Linux / WSL (권장)
curl -sSL https://install.python-poetry.org | python3 -

# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
설치 후, 터미널을 다시 시작하거나 시스템의 환경 변수를 업데이트해야 할 수 있습니다. `poetry --version`을 실행하여 Poetry가 제대로 설치되었는지 확인하세요.

### 2단계: 프로젝트 의존성 설치

프로젝트 템플릿을 클론하거나 다운로드한 후, 프로젝트의 루트 디렉토리로 이동하세요. 이제 Poetry를 사용하여 모든 필요한 의존성(런타임 및 개발 도구 포함)을 설치합니다.

```bash
poetry install --with dev
```

이 명령어는 `pyproject.toml` 파일에 정의된 모든 패키지를 가상 환경에 설치합니다. 여기에는 `torch`, `mlflow` 같은 주요 라이브러리뿐만 아니라, `ruff` (린터/포매터), `pytest` (테스트 프레임워크), `pre-commit` (Git 훅 관리)와 같은 개발 도구들도 포함됩니다.

### 3단계: Pre-commit 훅 설치

로컬 Git 커밋 시 자동으로 코드 품질 검사 및 포매팅을 수행하도록 `pre-commit` 훅을 설치합니다. 이 단계는 한 번만 수행하면 됩니다.

```bash
poetry run pre-commit install
```

이제 `git commit` 명령을 실행할 때마다 `ruff`를 이용한 코드 린트 검사 및 포매팅이 자동으로 이루어집니다. 코드가 자동으로 수정되거나 린트 오류가 발견되면 커밋이 중단될 수 있습니다. 이때는 수정된 파일을 다시 `git add .` 한 후 커밋을 재시도하면 됩니다.

---

## ✨ 개발 워크플로우: 코드 품질 및 테스트

이 프로젝트 템플릿은 높은 코드 품질을 유지하고, 기능이 의도대로 작동하는지 보장하기 위해 강력한 린트(Lint) 및 테스트 도구를 통합했습니다. `ruff`와 `pytest`를 사용하여 효율적인 개발 워크플로우를 구축할 수 있습니다.

### 1. 코드 린팅 (Linting) 및 포매팅 - `ruff`

**Ruff**는 매우 빠르고 강력한 Python 린터이자 포매터입니다. 코드를 분석하여 잠재적 버그, 스타일 위반, 비효율적인 코드 등을 찾아내며, 자동으로 수정 가능한 부분은 고쳐줍니다. `pyproject.toml`에 설정된 규칙을 따릅니다.

#### 수동 린트 검사 및 포매팅

언제든지 프로젝트 전체에 대해 린트 검사를 실행하거나 코드를 포매팅할 수 있습니다. 이는 커밋하기 전, 큰 변경 사항을 적용한 후 유용합니다.

* **린트 검사 실행:**
    ```bash
    poetry run ruff check .
    ```
    이 명령은 현재 디렉토리와 하위 디렉토리의 모든 Python 파일에 대해 린트 검사를 수행하고, 발견된 문제를 터미널에 출력합니다.

* **린트 오류 자동 수정:**
    `ruff`는 자동으로 수정 가능한 린트 오류를 고칠 수 있습니다.
    ```bash
    poetry run ruff check . --fix
    ```

* **코드 포매팅:**
    `ruff format`은 `Black`과 유사하게 코드 스타일을 자동으로 정돈합니다.
    ```bash
    poetry run ruff format .
    ```

* **린트 보고서 파일로 저장 (선택 사항):**
    린트 결과를 `reports/lint/` 폴더에 텍스트 또는 JSON 형식으로 저장할 수 있습니다. (필요 시 `reports/lint/` 폴더를 생성해야 합니다.)
    ```bash
    poetry run ruff check . > reports/lint/ruff_report.txt
    poetry run ruff check . --output-format json > reports/lint/ruff_report.json
    ```

### 2. 테스트 (Testing) - `pytest`

**Pytest**는 강력하고 유연한 Python 테스트 프레임워크입니다. 작성된 테스트 코드를 실행하여 애플리케이션의 기능이 올바르게 작동하는지 검증합니다. `pyproject.toml`에 설정된 테스트 경로 및 옵션을 따릅니다.

#### 수동 테스트 실행

언제든지 모든 테스트 또는 특정 테스트 그룹을 수동으로 실행하여 코드 변경 후 기능이 손상되지 않았는지 확인할 수 있습니다.

* **모든 테스트 실행:**
    ```bash
    poetry run pytest
    ```
    이 명령은 `pyproject.toml`의 `[tool.pytest.ini_options]`에 설정된 `testpaths`(`tests` 폴더)를 찾아 모든 테스트를 실행합니다. 기본적으로 코드 커버리지 리포트(`reports/coverage/`)도 함께 생성됩니다.

* **특정 테스트 파일 실행:**
    ```bash
    poetry run pytest tests/unit/data/test_DataLoader.py
    ```
    `tests/unit/data/test_DataLoader.py` 파일에 있는 테스트만 실행합니다.

* **코드 커버리지 리포트 확인:**
    테스트 실행 후, `reports/coverage/index.html` 파일을 웹 브라우저로 열면 코드 커버리지 상세 보고서를 확인할 수 있습니다.

### 3. Git 커밋 전 자동화 (Pre-commit Hooks)

이 템플릿은 `pre-commit` 프레임워크를 사용하여 Git 커밋 전에 자동으로 린트 검사 및 코드 포매팅을 수행합니다. 이는 깨끗하고 일관된 코드만 저장소에 커밋되도록 보장합니다.

#### 워크플로우

1.  **코드 작성 및 수정:** 평소처럼 코드를 작성하고 수정합니다.
2.  **변경 사항 스테이징:**
    ```bash
    git add .
    ```
3.  **커밋 실행:**
    ```bash
    git commit -m "feat: Add new feature"
    ```
    이때 **`.pre-commit-config.yaml`에 정의된 훅들이 자동으로 실행**됩니다 (`ruff format` 및 `ruff check --fix` 포함).
    * 만약 코드가 포매팅되었거나, `ruff check --fix`에 의해 수정 가능한 린트 오류가 고쳐졌다면, `pre-commit`은 해당 변경 사항을 사용자에게 알리고 **커밋을 중단**합니다.
    * 이 경우, 수정된 파일을 다시 `git add .` 한 후 `git commit` 명령을 **재시도**해야 합니다.
    * 모든 훅이 성공적으로 통과하면 커밋이 완료됩니다.

이 워크플로우를 통해 개발 과정에서 지속적으로 코드 품질을 검증하고, 잘 정돈되고 테스트된 코드만 프로젝트 저장소에 반영할 수 있습니다.

---

## ✍️ 개발 가이드: 당신의 AI 모델을 채워넣기

이 템플릿의 가장 큰 강점은 복잡한 초기 설정 없이 **당신의 AI 모델 개발에만 집중**할 수 있도록 설계되었다는 점입니다. 다음 가이드를 따라 템플릿의 기능을 활용해보세요.

* **`src/my_template/` 내부 구현**:
    * `src/my_template/utils/` 폴더를 제외한 모든 모듈 (예: `data`, `models`, `training`, `abc_interfaces`)에서 **미리 정의된 인터페이스 및 메소드**를 구현합니다. 각 파일은 해당 도메인의 핵심 로직을 담도록 설계되어 있습니다.
    * 특히 `abc_interfaces/`에 정의된 추상 클래스들은 당신이 구현해야 할 필수 메서드들을 명확히 제시합니다.
* **`tests/` 폴더 활용**:
    * `tests/unit/` 및 `tests/integration/` 폴더 내에 작성된 테스트 파일을 참조하여, 당신이 구현한 각 모듈 및 파이프라인의 기능이 올바르게 작동하는지 검증하는 테스트 코드를 작성합니다.

---

