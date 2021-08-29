.ONESHELL:
.PHONY: install clean clean-all shell run

SHELL := /bin/bash
venv_dir = .venv
env_file = .env


dev: $(env_file) $(venv_dir)

$(venv_dir):
	@python3 -m pip install -U --upgrade pip
	@python3 -m pip install -U pipenv
	@PIPENV_VENV_IN_PROJECT=1 python3 -m pipenv install -d
	@$@/bin/pip install --upgrade pip
	@$@/bin/pip install pipenv
	@$@/bin/python -c "import nltk; nltk.download(['stopwords', 'wordnet'])"

$(env_file):
	@cp $@.tmpl $@

.vscode:
	@cp -r .vscode.ex .vscode

clean-all: clean
	@rm -rf $(venv_dir)

clean:
	@find -iname "*.py[cod]" -delete

run:
	clear
	@source $(venv_dir)/bin/activate
	@pipenv run start
