# coding=utf-8
from tipoinstalacion.models import Condensador

from expects import expect, equal

with description('Calculando el TI de un condensador'):
    with before.each:
        self.c = Condensador()

    with context('si 132k>=tension >66kV'):
        with it('must be TI-169'):
            for t in range(67, 132):
                self.c.tension = t
                expect(self.c.tipoinstalacion).to(equal('TI-169'))

    with context('si la 66kV>=tenision>36kV'):
        with it('must be TI-170'):
            for t in range(37, 66):
                self.c.tension = t
                expect(self.c.tipoinstalacion).to(equal('TI-170'))

    with context('si la 36V>=tenision>1kV'):
        with it('must be TI-171'):
            for t in range(2, 36):
                self.c.tension = t
                expect(self.c.tipoinstalacion).to(equal('TI-171'))
