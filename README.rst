Notebook
--------

.. code-block::

  docker-compose up -d
  docker-compose exec jupyter conda install nltk elasticsearch
  docker-compose exec jupyter python -c "import nltk; nltk.download(['stopwords', 'wordnet'])"

Services
--------

- Elasticsearch: http://localhost:9200
- Jupyter: http://localhost:8888
- Kibana: http://localhost:5601

Aplication
----------

.. code-block::

  make dev

Running application
...................

.. code-block::

  make shell
  pipenv run start

Endpoints
.........

- API health check: http://localhost:8000/ping
- API docs: http://localhost:8000/redoc
