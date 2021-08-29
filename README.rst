Notebook
--------

.. code-block::

  docker-compose up -d
  docker-compose exec jupyter conda install nltk elasticsearch
  docker-compose exec jupyter python -c "import nltk; nltk.download(['stopwords', 'wordnet'])"

Aplication
----------

.. code-block::

  make install

Services
--------

- Elasticsearch: http://localhost:9200
- Jupyter: http://localhost:8888
- Kibana: http://localhost:5601
