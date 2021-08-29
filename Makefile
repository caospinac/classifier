# Makefile
SHELL := /bin/bash
VENV = .venv


all: env install

install: | $(VENV)
	@if [ ! -d $(VENV) ]; then \
		cp .env.tmpl .env; \
		echo ".env file created"; \
		python3 -m pip install -U --upgrade pip; \
		python3 -m pip install -U pipenv; \
		PIPENV_VENV_IN_PROJECT=1 python3 -m pipenv install -d; \
		$(VENV)/bin/pip install --upgrade pip; \
		$(VENV)/bin/pip install pipenv; \
	fi

venv:
	source $(VENV)/bin/activate

.vscode:
	cp -r .vscode.ex .vscode

env:
	@if [ ! -f .env ]; then \
		cp .env.tmpl .env; \
		echo ".env file created"; \
	fi

clean:
	rm -rf $(VENV)
	find -iname "*.py[cod]" -delete
