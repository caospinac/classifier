Notebook
--------
docker-compose up -d
docker-compose exec jupyter conda install nltk
docker-compose exec jupyter python -c "import nltk; nltk.download('stopwords')"

Aplication
----------
bash scripts/setup.sh
.venv/bin/python -c "import nltk; nltk.download('stopwords')"
