# coding=utf-8
from tipoinstalacion.models import *

from expects import *


with description('Una Linea'):
    with before.all:
        self.linea = Linea()
    with it('must have atributo tensión'):
        assert hasattr(self.linea, 'tension')
    with it('must have atributo seccion'):
        assert hasattr(self.linea, 'seccion')
