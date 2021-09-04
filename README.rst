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


Aplication
##########

.. code-block:: bash

  make dev

Running application
-------------------

.. code-block:: bash

  make run start

For development: :code:`make run start-dev`


Building
--------

.. code-block:: bash

  make build

Endpoints
.........

- API health check: http://localhost:8000/ping
- API docs: http://localhost:8000/redoc


Training
--------

Pull datasets

.. code-block:: bash

  make training-data
