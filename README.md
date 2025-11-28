### 모듈

Poetry → 의존성 (필수)

pre-commit → 코드 품질 관리 + ai 배포 과정에서 사용 (선택)

pytest → 코드 관리 + 테스트 기능 제공 (선택)

pylint, mypy, ruff → 문법 검사, 코드 관리 (선택)

hydra → config (선택), scheme

airflow apache→ 학습 과정 자동화 (선택)

mlflow → 학습 지표 관리 (선택)

sphinx → 문서 관리 (선택)

- tensorboard, pytorch, keras, tensorflow (필수, 선택)

### 폴더

.github → CI/CD 관련 * CI/CD 뭔지도 설명

.venv → 의존성 관리 및 개발 공간 분리

.vscode → 코드 품질 관리

checkpoint → 모델 체크포인트 저장

config → 개발 과정 추상화 + 모델 학습 요소 관리

data → 데이터셋 + 기타 데이터들 관리

docs → 관련 문서 저장

experiments → HPO 등에서 달라진 설정값에 따른 모델 실험 결과 저장

logs → 로그 저장

notebooks → 노트북 파일 보관

notebooks/eda → 데이터 분석, 탐색

notebooks/experiment → 모델 아이디어 검증

outputs → hydra 실행 데이터 저장 + 모델 최정 결과물

scripts → [main.py](http://main.py) 관리, 학습 진입점 관리

src → 자체 제작 모듈

my_template(이름 변경 가능) → 모델 핵심 기능, 구성요소 구현

deploy → 모델 배포, 상용화에 필요한 파일들

tests → 코드 테스트, Unit + Integration tests