# coding=utf-8
from tipoinstalacion.models import Linea, Posicion, Transformador

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
    with it('must have atraibut situacion'):
        assert hasattr(self.posicion, 'situacion')
    with it('must have atraibut tipo'):
        assert hasattr(self.posicion, 'tipo')

with description('Una posicion'):
    with before.all:
        self.t = Transformador()
    with it('must have atributo tensión primario'):
        assert hasattr(self.t, 'tension_p')
    with it('must have atraibut situacion'):
        assert hasattr(self.t, 'tension_s')
