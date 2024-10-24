# coding=utf-8
from tipoinstalacion.models import *
from decimal import Decimal

from expects import *


def frange(start, end, step=0.1):
    """Floating range
    """
    step = Decimal(step)
    precision = abs(step.as_tuple().exponent)
    start = Decimal(str(round(start, precision)))
    end = Decimal(str(round(end, precision)))

    r = start
    while r < end:
        res = round(float(r), precision)
        yield res
        r += step

with description('Calculando el TI de una posicion'):
    with context('si lat tensión > 123 kV'):
        with before.each:
            self.p = Posicion()
            self.p.tension = 124
            self.p.tipo = 'B'
        with context('situado en Initerior'):
            with it('must be TI-88U'):
                self.p.situacion = 'I'
                expect(self.p.tipoinstalacion).to(equal('TI-88U'))
        with context('situado en Intemperie'):
            with it('must be TI-89U'):
                self.p.situacion = 'E'
                expect(self.p.tipoinstalacion).to(equal('TI-89U'))
        with context('situado en Mobil'):
            with it('must be TI-90U'):
                self.p.situacion = 'M'
                expect(self.p.tipoinstalacion).to(equal('TI-90U'))

with description('Calculando el TI de una posicion'):
    with context('si lat 123Kv >= tensión > 72.5kV'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'B'
            self.tensions = list(range(73, 123))
        with context('situado en Initerior'):
            with it('must be TI-88V'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-88V'))
        with context('situado en Intemperie'):
            with it('must be TI-89V'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-89V'))
        with context('situado en Mobil'):
            with it('must be TI-90V'):
                self.p.situacion = 'M'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-90V'))

with description('Calculando el TI de una posicion'):
    with context('si lat 72.5Kv >= tensión > 52kV'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'B'
            self.tensions = list(range(53, 72)) + [72.5]
        with context('situado en Initerior'):
            with it('must be TI-95U'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-95U'))
        with context('situado en Intemperie'):
            with it('must be TI-96U'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-96U'))
        with context('situado en Mobil'):
            with it('must be TI-97U'):
                self.p.situacion = 'M'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-97U'))

with description('Calculando el TI de una linia'):
    with context('si lat 52kV >= tensión > 36kV'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'B'
            self.tensions = list(list(range(37, 52)))
        with context('situado en Initerior'):
            with it('must be TI-95V'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-95V'))
        with context('situado en Intemperie'):
            with it('must be TI-96V'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-96V'))
        with context('situado en Mobil'):
            with it('must be TI-97V'):
                self.p.situacion = 'M'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-97V'))

with description('Calculando el TI de una linia'):
    with context('si lat 36kV >= tensión > 24kV'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'B'
            self.tensions = range(25, 37)
        with context('situado en Initerior'):
            with it('must be TI-102U'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-102U'))
        with context('situado en Intemperie'):
            with it('must be TI-103U'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-103U'))
        with context('situado en Mobil'):
            with it('must be TI-104U'):
                self.p.situacion = 'M'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-104U'))

with description('Calculando el TI de una linia'):
    with context('si lat 24Kv >= tensión > 17.5kV'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'B'
            self.tensions = range(18, 24)
        with context('situado en Initerior'):
            with it('must be TI-102V'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-102V'))
        with context('situado en Intemperie'):
            with it('must be TI-103V'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-103V'))
        with context('situado en Mobil'):
            with it('must be TI-104V'):
                self.p.situacion = 'M'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-104V'))

with description('Calculando el TI de una linia'):
    with context('si lat 17.5Kv >= tensión > 12kV'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'B'
            self.tensions = list(range(13, 17)) + [17.5]
        with context('situado en Initerior'):
            with it('must be TI-102W'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-102W'))
        with context('situado en Intemperie'):
            with it('must be TI-103W'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-103W'))
        with context('situado en Mobil'):
            with it('must be TI-104W'):
                self.p.situacion = 'M'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-104W'))

with description('Calculando el TI de una linia'):
    with context('si lat 12Kv >= tensión >= 1kV'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'B'
            self.tensions = range(1, 12)
        with context('situado en Initerior'):
            with it('must be TI-102W'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-102B'))
        with context('situado en Intemperie'):
            with it('must be TI-103B'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-103B'))
        with context('situado en Mobil'):
            with it('must be TI-104B'):
                self.p.situacion = 'M'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-104B'))

with description('Calculando el TI de una linia'):
    with context('si lat  124kV'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'C'
        with context('situado en Initerior'):
            with it('must be TI-91V'):
                self.p.situacion = 'I'
                self.p.tension = 124
                expect(self.p.tipoinstalacion).to(equal('TI-91U'))
        with context('situado en Intemperie'):
            with it('must be TI-92V'):
                self.p.situacion = 'E'
                self.p.tension = 124
                expect(self.p.tipoinstalacion).to(equal('TI-92U'))

with description('Calculando el TI de una linia'):
    with context('si lat  123kV >= tensión > 72.5Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'C'
            self.tensions = list(range(73, 123))
        with context('situado en Initerior'):
            with it('must be TI-91V'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-91V'))
        with context('situado en Intemperie'):
            with it('must be TI-92V'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-92V'))

with description('Calculando el TI de una linia'):
    with context('si lat  72.5Kv >= tensión > 52Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'C'
            self.tensions = list(range(53,72)) + [72.5]
        with context('situado en Initerior'):
            with it('must be TI-98U'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-98U'))
        with context('situado en Intemperie'):
            with it('must be TI-99U'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-99U'))

with description('Calculando el TI de una linia'):
    with context('si lat  52Kv >= tensión > 36Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'C'
            self.tensions = list(range(37, 52))
        with context('situado en Initerior'):
            with it('must be TI-99V'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-98V'))
        with context('situado en Intemperie'):
            with it('must be TI-99V'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-99V'))

with description('Calculando el TI de una linia'):
    with context('si lat  36Kv >= tensión > 24Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'C'
            self.tensions = range(25, 36)
        with context('situado en Initerior'):
            with it('must be TI-105U'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-105U'))
        with context('situado en Intemperie'):
            with it('must be TI-106U'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-106U'))

with description('Calculando el TI de una linia'):
    with context('si lat  24Kv >= tensión > 17.5Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'C'
            self.tensions = range(18, 24)
        with context('situado en Initerior'):
            with it('must be TI-105V'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-105V'))
        with context('situado en Intemperie'):
            with it('must be TI-106V'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-106V'))

with description('Calculando el TI de una linia'):
    with context('si lat  17.5Kv >= tensión > 12Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'C'
            self.tensions = list(range(13, 17)) + [17.5]
        with context('situado en Initerior'):
            with it('must be TI-105W'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-105W'))
        with context('situado en Intemperie'):
            with it('must be TI-106W'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-106W'))

with description('Calculando el TI de una linia'):
    with context('si lat  12Kv >= tensión >= 1Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'C'
            self.tensions = range(1, 12)
        with context('situado en Initerior'):
            with it('must be TI-105B'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-105B'))
        with context('situado en Intemperie'):
            with it('must be TI-106B'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-106B'))


with description('Calculando el TI de una linia'):
    with context('si lat  123Kv >= tensión'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'H'
            self.tensions = [124]
        with context('situado en Initerior'):
            with it('must be TI-93U'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-93U'))
        with context('situado en Intemperie'):
            with it('must be TI-94U'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-94U'))

with description('Calculando el TI de una linia'):
    with context('si lat  123Kv >= tensión > 73.5Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'H'
            self.tensions = list(range(73, 123))
        with context('situado en Initerior'):
            with it('must be TI-93V'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-93V'))
        with context('situado en Intemperie'):
            with it('must be TI-94V'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-94V'))

with description('Calculando el TI de una linia'):
    with context('si lat  73.5Kv >= tensión > 52Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'H'
            self.tensions = list(range(53, 72)) + [72.5]
        with context('situado en Initerior'):
            with it('must be TI-100U'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-100U'))
        with context('situado en Intemperie'):
            with it('must be TI-101U'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-101U'))

with description('Calculando el TI de una linia'):
    with context('si lat  52Kv >= tensión > 36Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'H'
            self.tensions = list(range(37, 52))
        with context('situado en Initerior'):
            with it('must be TI-100V'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-100V'))
        with context('situado en Intemperie'):
            with it('must be TI-101V'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-101V'))

with description('Calculando el TI de una linia'):
    with context('si lat  36Kv >= tensión > 24Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'H'
            self.tensions = range(25, 36)
        with context('situado en Initerior'):
            with it('must be TI-107U'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-107U'))
        with context('situado en Intemperie'):
            with it('must be TI-108U'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-108U'))

with description('Calculando el TI de una linia'):
    with context('si lat  24Kv >= tensión > 17.5Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'H'
            self.tensions = range(18, 24)
        with context('situado en Initerior'):
            with it('must be TI-107V'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-107V'))
        with context('situado en Intemperie'):
            with it('must be TI-108V'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-108V'))

with description('Calculando el TI de una linia'):
    with context('si lat  17.5Kv >= tensión > 12Kv'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'H'
            self.tensions = list(range(13, 17)) + [17.5]
        with context('situado en Initerior'):
            with it('must be TI-107W'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-107W'))
        with context('situado en Intemperie'):
            with it('must be TI-108W'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-108W'))

with description('Calculando el TI de una linia'):
    with context('si lat  12Kv >= tensión >= 1v'):
        with before.each:
            self.p = Posicion()
            self.p.tipo = 'H'
            self.tensions = range(1, 12)
        with context('situado en Initerior'):
            with it('must be TI-107B'):
                self.p.situacion = 'I'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-107B'))
        with context('situado en Intemperie'):
            with it('must be TI-108B'):
                self.p.situacion = 'E'
                for t in self.tensions:
                    self.p.tension = t
                    expect(self.p.tipoinstalacion).to(equal('TI-108B'))