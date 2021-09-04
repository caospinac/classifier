FROM python:3.9-alpine

WORKDIR /app

RUN apk update && apk add gcc g++ python3-dev
RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy
RUN python -c "import nltk; nltk.download(['stopwords', 'wordnet'])"

COPY . /app

CMD ["python", "main.py"]
