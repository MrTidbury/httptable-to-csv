PYTHON_VERSION := "3.8.5"
PIPENV := $(shell command -v pipenv 2> /dev/null)

ifndef PIPENV
    $(error "Pipenv is not installed! See README.md")
endif


.PHONY: init dev requirements

export PIPENV_IGNORE_VIRTUALENVS=1
export PYTHONPATH=./src

init:
	pipenv --python ${PYTHON_VERSION} && \
	pipenv install --dev

dev:
	pipenv run python src/script.py

requirements:
	pipenv lock -r > requirements.txt
