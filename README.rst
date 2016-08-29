Tipo Instalacion
================
.. image:: https://travis-ci.org/gisce/tipoinstalacion.svg?branch=master
    :target: https://travis-ci.org/gisce/tipoinstalacion
.. image:: https://coveralls.io/repos/github/gisce/tipoinstalacion/badge.svg?branch=master
    :target: https://coveralls.io/github/gisce/tipoinstalacion?branch=master


Libreria para calcular de forma automática el Tipo de Instalacion (TI)

Especificaciones de referencia
------------------------------

BOE http://www.boe.es/boe/dias/2015/12/12/pdfs/BOE-A-2015-13488.pdf

Instalaciones soportadas
------------------------

- Lineas
- Posiciones
- Transformadores
- Reactancias
- Condensadores
- Centros transformadores
- Fiabilidad

Para desarrollar
----------------

Para cualquier cambio en el comportamiento **debe haber** un test que implemente este
comportamiento **antes** de desarrollar el cambio (metodología `TDD <https://en.wikipedia.org/wiki/Test-driven_development>`_)

- Crear un virtualenv

.. code-block:: shell

    $ mkvirtualenv tipoinstalacion
    $ workon tipoinstalacion


- Clonar el repositorio

.. code-block:: shell

    $ git clone https://github.com/gisce/tipoinstalacion.git


- Instalar dependencias desarrollo

.. code-block:: shell

    $ cd tipoinstalacion
    $ pip install -r requirements-dev.txt
    $ pip install -e .

Ejecutar tests
--------------
Utilizamos el sistema de tests `Mamba <http://nestorsalceda.github.io/mamba/>`_

Con el virtualenv activado y situados en la raíz del repositorio ejecutamos:

.. code-block:: shell

    $ mamba --format=documentation
