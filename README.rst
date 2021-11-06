Notebook & services
###################

First time

.. code-block:: bash

  make run-services-install

Thenceforth:

.. code-block:: bash

  make run-services

Services
--------

- Elasticsearch: http://localhost:9200
- Jupyter: http://localhost:8888
- Kibana: http://localhost:5601


Training
########

Pull datasets

.. code-block:: bash

  make training-data

Run training process

.. code-block:: bash

  make train


Aplication
##########

.. code-block:: bash

  make dev

Running application
-------------------

.. code-block:: bash

  make run

Building
--------

.. code-block:: bash

  make build

Endpoints
.........

- API health check: http://localhost:8000/ping
- API docs: http://localhost:8000/redoc

Evaluate text:

.. code-block:: bash

  curl --location --request POST 'http://localhost:8000/v1/get-perception' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "input": "Text to evaluate"
  }'



Available CLI commands
----------------------

* :code:`make run-services-install`: Installs and runs dep-services
* :code:`make run-services`: Runs dependencies services
* :code:`make training-data`: Downloads training data sets
* :code:`make train`: Trains the algorithm. Indexes data onto Elasticsearch
* :code:`make jupyter-token`: Gets Jupyter token for login
* :code:`make build`: Build main service
* :code:`make dev`: Install development dependencies
* :code:`make run`: Run application (development)
* :code:`make run-docker`: Run application
* :code:`make run-docker-d`: Run application (detached)
* :code:`make .vscode`: Creates default VSCode config
* :code:`make clean`: Remove cached Python files
* :code:`make clean-all`: Remove cached Python files and installed packages
