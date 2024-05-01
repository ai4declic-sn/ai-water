# Makefile

run-tests:
	poetry run pytest tests --cov=src/resources --cov-report=term-missing --cov-report=xml --junit-xml=tests-results.xml -vv

format:
	poetry run black .

lint:
	poetry run ruff check .

fix-lint:
	poetry run ruff check . --fix

static-analysis:
	poetry run mypy .

securuty-check:
	poetry run bandit -r .

google-auth-user:
	@echo Setting up GCP authorisation
	gcloud auth login

google-auth-api:
	@echo Setting up API authorisation
	gcloud auth application-default login

set-project:
	@test -n "$(PROJECT_ID)" || (echo "PROJECT_ID is not set" && exit 1)
	gcloud config set project $(PROJECT_ID)
