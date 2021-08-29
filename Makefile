.ONESHELL:
.PHONY: install clean clean-all shell

SHELL := /bin/bash
venv_dir = .venv
env_file = .env


install: $(env_file) $(venv_dir)

$(venv_dir):
	python3 -m pip install -U --upgrade pip
	python3 -m pip install -U pipenv
	PIPENV_VENV_IN_PROJECT=1 python3 -m pipenv install -d
	$(venv_dir)/bin/pip install --upgrade pip
	$(venv_dir)/bin/pip install pipenv
	$(venv_dir)/bin/python -c "import nltk; nltk.download(['stopwords', 'wordnet'])"

$(env_file):
	cp $(env_file).tmpl $(env_file)

clean-all: clean
	rm -rf $(venv_dir)

clean:
	find -iname "*.py[cod]" -delete

shell:
	source $(venv_dir)/bin/activate

.vscode:
	cp -r .vscode.ex .vscode
