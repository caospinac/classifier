.ONESHELL:
.PHONY: install clean clean-all shell run dev

SHELL := /bin/bash
venv_dir = .venv
env_file = .env
training_data_dir = training_data


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

bucket_url = https://firebasestorage.googleapis.com/v0/b/autoclassifier.appspot.com/o

training-data:
	@for file in np_ds_01.csv np_ds_02.csv npn_ds_03.csv; do
	 	wget $(bucket_url)/datasets%2F$$file?alt=media -O $(training_data_dir)/$$file
	done

run-services-install: run-services
	@docker-compose -f docker-compose.services.yml exec jupyter conda install nltk elasticsearch
	@docker-compose -f docker-compose.services.yml exec jupyter python -c "import nltk; nltk.download(['stopwords', 'wordnet'])"

jupyter-token:
	@docker-compose -f docker-compose.services.yml exec jupyter jupyter notebook list | grep "?token"

run-services:
	docker-compose -f docker-compose.services.yml up -d

build:
	@docker-compose build

run-docker:
	@docker-compose up

run-docker-d:
	@docker-compose up -d

train:
	@source $(venv_dir)/bin/activate
	eval $$(cat $(env_file)) python scripts/train.py
