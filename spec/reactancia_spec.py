# coding=utf-8
from tipoinstalacion.models import Reactancia

from expects import *

with description('Calculando el TI de una reactancia'):
    with before.each:
        self.r = Reactancia()

    with context('si 145k>=tension >72.5kV'):
        with it('must be TI-166'):
            for t in range(73, 145):
                self.r.tension = t
                expect(self.r.tipoinstalacion).to(equal('TI-167'))

    with context('si la 72.5kV>=tenision>36kV'):
        with it('must be TI-167'):
            for t in range(36, 72) + [72.5]:
                self.r.tension = t
                expect(self.r.tipoinstalacion).to(equal('TI-167'))
    with context('si la 36kV>=tenision>1kV'):
        with it('must be TI-168'):
            for t in range(2, 36):
                self.r.tension = t
                expect(self.r.tipoinstalacion).to(equal('TI-168'))
