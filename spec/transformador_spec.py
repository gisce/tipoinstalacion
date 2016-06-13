# coding=utf-8
from tipoinstalacion.models import Transformador

from expects import *

with description('Calculando el TI de un transformador'):
    with before.each:
        self.t = Transformador()
        self.t.tension_p = 420

    with context('si lat tensión primario = 420 kV'):
        with context('si 245Kv >= tension de secundario > 123Kv'):
            with it('must be TI-158U'):
                for t in range(73, 123):
                    self.t.tension_s = t
                    expect(self.t.tipoinstalacion).to(equal('TI-158U'))

        with context('si 245Kv >= tension de secundario > 123Kv'):
            with it('must be TI-158V'):
                for t in range(73, 123):
                    self.t.tension_s = t
                    expect(self.t.tipoinstalacion).to(equal('TI-158V'))

        with context('si 72Kv >= tension de secundario > 36Kv'):
            with it('must be TI-158W'):
                for t in range(37, 72) + [72.5]:
                    self.t.tension_s = t
                    expect(self.t.tipoinstalacion).to(equal('TI-158W'))

with description('Calculando el TI de un transformador'):
    with before.each:
        self.t = Transformador()
        self.t.tension_p = 245

    with context('si lat tensión primario = 245 kV'):
        with context('si 245Kv >= tension de secundario > 123Kv'):
            with it('must be TI-159U'):
                for t in range(124, 245):
                    self.t.tension_s = t
                    expect(self.t.tipoinstalacion).to(equal('TI-159U'))

    with context('si lat tensión primario = 245 kV'):
        with context('si 123Kv >= tension de secundario > 72.5Kv'):
            with it('must be TI-159V'):
                for t in range(73, 123):
                    self.t.tension_s = t
                    expect(self.t.tipoinstalacion).to(equal('TI-159V'))

    with context('si lat tensión primario = 245 kV'):
        with context('si 72.5v >= tension de secundario > 36Kv'):
            with it('must be TI-160U'):
                for t in range(37, 72)+ [72.5] :
                    self.t.tension_s = t
                    expect(self.t.tipoinstalacion).to(equal('TI-160U'))

    with context('si lat tensión primario = 245 kV'):
        with context('si 36Kv >= tension de secundario > 24Kv'):
            with it('must be TI-161U'):
                for t in range(25, 36):
                    self.t.tension_s = t
                    expect(self.t.tipoinstalacion).to(equal('TI-161U'))

    with context('si lat tensión primario = 245 kV'):
        with context('si 17.5Kv >= tension de secundario > 12Kv'):
            with it('must be TI-161W'):
                for t in range(13, 17) + [17.5]:
                    self.t.tension_s = t
                    expect(self.t.tipoinstalacion).to(equal('TI-161W'))

    with context('si lat tensión primario = 245 kV'):
        with context('si 12Kv >= tension de secundario >= 1Kv'):
            with it('must be TI-161B'):
                for t in range(1, 12):
                    self.t.tension_s = t
                    expect(self.t.tipoinstalacion).to(equal('TI-161B'))

with description('Calculando el TI de un transformador'):
    with before.each:
        self.t = Transformador()
        self.tensions_p = range(73, 145)

    with context('si lat 145 >= tensión primario >=72.5 kV'):
        with context('si 72.5Kv >= tension de secundario > 52Kv'):
            with it('must be TI-162U'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(53, 72) + [72.5]:
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-162U'))

    with context('si lat 145 >= tensión primario >=72.5 kV'):
        with context('si 52Kv >= tension de secundario > 36Kv'):
            with it('must be TI-162V'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(37, 52):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-162V'))

    with context('si lat 145 >= tensión primario >=72.5 kV'):
        with context('si 36Kv >= tension de secundario > 24Kv'):
            with it('must be TI-163U'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(25, 36):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-163U'))

    with context('si lat 145 >= tensión primario >=72.5 kV'):
        with context('si 24Kv >= tension de secundario > 17.5Kv'):
            with it('must be TI-163V'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(18, 24):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-163V'))

    with context('si lat 145 >= tensión primario >=72.5 kV'):
        with context('si 17.5Kv >= tension de secundario > 12Kv'):
            with it('must be TI-163W'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(13, 16) + [17.5]:
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-163W'))

    with context('si lat 145 >= tensión primario >=72.5 kV'):
        with context('si 12KV >= tension de secundario >= 1Kv'):
            with it('must be TI-163W'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(1, 12):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-163B'))


with description('Calculando el TI de un transformador'):
    with before.each:
        self.t = Transformador()
        self.tensions_p = range(37, 72) + [72.5]

    with context('si lat 72Kv >= tensión primario >=36 kV'):
        with context('si 36Kv >= tension de secundario > 24Kv'):
            with it('must be TI-164U'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(25, 36):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-164U'))

    with context('si lat 72Kv >= tensión primario >=36 kV'):
        with context('si 24Kv >= tension de secundario >17.5Kv'):
            with it('must be TI-164V'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(18, 24):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-164V'))

    with context('si lat 72Kv >= tensión primario >=36 kV'):
        with context('si 12 >= tension de secundario >=1Kv'):
            with it('must be TI-164B'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(1, 12):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-164B'))

with description('Calculando el TI de un transformador'):
    with before.each:
        self.t = Transformador()
        self.tensions_p = range(1, 35)

    with context('si lat 36Kv >= tensión primario > 1kV'):
        with context('si 30Kv >= tension de secundario > 24Kv'):
            with it('must be TI-165U'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(25, 30):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-165U'))

    with context('si lat 36Kv >= tensión primario > 1kV'):
        with context('si 24Kv >= tension de secundario > 17.5Kv'):
            with it('must be TI-165V'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(18, 24):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-165V'))

    with context('si lat 36Kv >= tensión primario > 1kV'):
        with context('si 17.5Kv >= tension de secundario > 12Kv'):
            with it('must be TI-165W'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(13, 17) + [17.5]:
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-165W'))

    with context('si lat 36Kv >= tensión primario > 1kV'):
        with context('si 12Kv >= tension de secundario > 1Kv'):
            with it('must be TI-165B'):
                for t_p in self.tensions_p:
                    self.t.tension_p = t_p
                    for t in range(1, 12):
                        self.t.tension_s = t
                        expect(self.t.tipoinstalacion).to(equal('TI-165B'))