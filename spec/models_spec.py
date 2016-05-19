# coding=utf-8
from tipoinstalacion.models import *

from expects import *


with description('Una Linea'):
    with before.all:
        self.linea = Linea()
    with it('must have atributo tensión'):
        assert hasattr(self.linea, 'tension')
    with it('must have atributo numero de circuitos'):
        assert hasattr(self.linea, 'num_circuitos')
    with it('must have atributo conductores'):
        assert hasattr(self.linea, 'num_conductores')
    with it('must have atributo seccion'):
        assert hasattr(self.linea, 'seccion')
    with it('must have atributo despliegue'):
        assert hasattr(self.linea, 'despliegue')

with description('Una posicion'):
    with before.all:
        self.posicion = Posicion()
    with it('must have atributo tensión'):
        assert hasattr(self.posicion, 'tension')

with description('Un condensador'):
    with before.all:
        self.condensador = Condensador()
    with it('must have atributo tensión'):
        assert hasattr(self.condensador, 'tension')


