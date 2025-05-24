# 변수 정의
PYTHON = python
LINT_REPORT = reports/lint/ruff-report.txt
COV_REPORT = reports/coverage/

# 린트 실행 및 결과 저장
lint:
    mkdir -p reports/lint
    ruff check . > $(LINT_REPORT)

# 코드 포맷팅
format:
    black . && isort .

# 테스트 실행 및 커버리지 리포트 생성
test:
    pytest

# 커버리지 리포트 생성
coverage:
    pytest --cov=. --cov-report=html:$(COV_REPORT)

# 모든 작업 실행
all: lint format test coverage