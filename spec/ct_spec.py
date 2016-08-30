# coding=utf-8
from tipoinstalacion.models import CT

from expects import expect, equal

with description('Calculando el TI de un CT'):
    with context('si valores Nulos'):
        with before.each:
            self.c = CT()
            expect(self.c.tipoinstalacion).to(equal(None))

    with context('si 12kV>=tension>1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 1

        with context('si situacion es Caseta'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-22U'):
                    self.c.potencia = 15
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-22U'))

            with context('si 1 máquina 25kVA'):
                with it('must be TI-23U'):
                    self.c.potencia = 25
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-23U'))

            with context('si 1 máquina 50kVA'):
                with it('must be TI-24U'):
                    self.c.potencia = 50
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-24U'))

            with context('si 1 máquina 100kVA'):
                with it('must be TI-25U'):
                    self.c.potencia = 100
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-25U'))

            with context('si 1 máquina 160kVA'):
                with it('must be TI-26U'):
                    self.c.potencia = 160
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-26U'))

            with context('si 1 máquina 250kVA'):
                with it('must be TI-27U'):
                    self.c.potencia = 250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-27U'))

            with context('si 1 máquina 400kVA'):
                with it('must be TI-28U'):
                    self.c.potencia = 400
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-28U'))

            with context('si 1 máquina 630kVA'):
                with it('must be TI-29U'):
                    self.c.potencia = 630
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-29U'))

            with context('si 1 máquina 1000kVA'):
                with it('must be TI-30U'):
                    self.c.potencia = 1000
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-30U'))

            with context('si 1 máquina 1250kVA'):
                with it('must be TI-30U'):
                    self.c.potencia = 1250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-31U'))

    with context('si 17.5kV>=tension>12kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 1

        with context('si situacion es Caseta'):
            with context('si 1 máquina 15kVA'):

                with it('must be TI-22V'):
                    self.c.potencia = 15
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-22V'))

            with context('si 1 máquina 25kVA'):
                with it('must be TI-23V'):
                    self.c.potencia = 25
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-23V'))

            with context('si 1 máquina 50kVA'):
                with it('must be TI-24V'):
                    self.c.potencia = 50
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-24V'))

            with context('si 1 máquina 100kVA'):
                with it('must be TI-25V'):
                    self.c.potencia = 100
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-25V'))

            with context('si 1 máquina 160kVA'):
                with it('must be TI-26V'):
                    self.c.potencia = 160
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-26V'))

            with context('si 1 máquina 250kVA'):
                with it('must be TI-27V'):
                    self.c.potencia = 250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-27V'))

            with context('si 1 máquina 400kVA'):
                with it('must be TI-28V'):
                    self.c.potencia = 400
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-28V'))

            with context('si 1 máquina 630kVA'):
                with it('must be TI-29V'):
                    self.c.potencia = 630
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-29V'))

            with context('si 1 máquina 1000kVA'):
                with it('must be TI-30V'):
                    self.c.potencia = 1000
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-30V'))

            with context('si 1 máquina 1250kVA'):
                with it('must be TI-31V'):
                    self.c.potencia = 1250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-31V'))

    with context('si 24kV>=tension>17.5kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 1

        with context('si situacion es Caseta'):
            with context('si 1 máquina 15kVA'):

                with it('must be TI-22W'):
                    self.c.potencia = 15
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-22W'))

            with context('si 1 máquina 25kVA'):
                with it('must be TI-23W'):
                    self.c.potencia = 25
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-23W'))

            with context('si 1 máquina 50kVA'):
                with it('must be TI-24W'):
                    self.c.potencia = 50
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-24W'))

            with context('si 1 máquina 100kVA'):
                with it('must be TI-25W'):
                    self.c.potencia = 100
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-25W'))

            with context('si 1 máquina 160kVA'):
                with it('must be TI-26W'):
                    self.c.potencia = 160
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-26W'))

            with context('si 1 máquina 250kVA'):
                with it('must be TI-27W'):
                    self.c.potencia = 250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-27W'))

            with context('si 1 máquina 400kVA'):
                with it('must be TI-28W'):
                    self.c.potencia = 400
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-28W'))

            with context('si 1 máquina 630kVA'):
                with it('must be TI-29W'):
                    self.c.potencia = 630
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-29W'))

            with context('si 1 máquina 1000kVA'):
                with it('must be TI-30W'):
                    self.c.potencia = 1000
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-30W'))

            with context('si 1 máquina 1250kVA'):
                with it('must be TI-31W'):
                    self.c.potencia = 1250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-31W'))

    with context('si 36kV>=tension>24kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 1

        with context('si situacion es Caseta'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-22B'):
                    self.c.potencia = 15
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-22B'))

            with context('si 1 máquina 25kVA'):
                with it('must be TI-23B'):
                    self.c.potencia = 25
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-23B'))

            with context('si 1 máquina 50kVA'):
                with it('must be TI-24B'):
                    self.c.potencia = 50
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-24B'))

            with context('si 1 máquina 100kVA'):
                with it('must be TI-25B'):
                    self.c.potencia = 100
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-25B'))

            with context('si 1 máquina 160kVA'):
                with it('must be TI-26B'):
                    self.c.potencia = 160
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-26B'))

            with context('si 1 máquina 250kVA'):
                with it('must be TI-27B'):
                    self.c.potencia = 250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-27B'))

            with context('si 1 máquina 400kVA'):
                with it('must be TI-28B'):
                    self.c.potencia = 400
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-28B'))

            with context('si 1 máquina 630kVA'):
                with it('must be TI-29B'):
                    self.c.potencia = 630
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-29B'))

            with context('si 1 máquina 1000kVA'):
                with it('must be TI-30B'):
                    self.c.potencia = 1000
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-30B'))

            with context('si 1 máquina 1250kVA'):
                with it('must be TI-31B'):
                    self.c.potencia = 1250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-31B'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 1

        with context('si situacion es Caseta'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-22C'):
                    self.c.potencia = 15
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-22C'))

            with context('si 1 máquina 25kVA'):
                with it('must be TI-23C'):
                    self.c.potencia = 25
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-23C'))

            with context('si 1 máquina 50kVA'):
                with it('must be TI-24C'):
                    self.c.potencia = 50
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-24C'))

            with context('si 1 máquina 100kVA'):
                with it('must be TI-25C'):
                    self.c.potencia = 100
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-25C'))

            with context('si 1 máquina 160kVA'):
                with it('must be TI-26C'):
                    self.c.potencia = 160
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-26C'))

            with context('si 1 máquina 250kVA'):
                with it('must be TI-27C'):
                    self.c.potencia = 250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-27C'))

            with context('si 1 máquina 400kVA'):
                with it('must be TI-28C'):
                    self.c.potencia = 400
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-28C'))

            with context('si 1 máquina 630kVA'):
                with it('must be TI-29C'):
                    self.c.potencia = 630
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-29C'))

            with context('si 1 máquina 1000kVA'):
                with it('must be TI-30C'):
                    self.c.potencia = 1000
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-30C'))

            with context('si 1 máquina 1250kVA'):
                with it('must be TI-31C'):
                    self.c.potencia = 1250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-31C'))

    with context('si 12kV>=tension>1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 1

        with context('si situacion es Caseta'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-22D'):
                    self.c.potencia = 15
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-22D'))

            with context('si 1 máquina 25kVA'):
                with it('must be TI-23D'):
                    self.c.potencia = 25
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-23D'))

            with context('si 1 máquina 50kVA'):
                with it('must be TI-24D'):
                    self.c.potencia = 50
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-24D'))

            with context('si 1 máquina 100kVA'):
                with it('must be TI-25D'):
                    self.c.potencia = 100
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-25D'))

            with context('si 1 máquina 160kVA'):
                with it('must be TI-26D'):
                    self.c.potencia = 160
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-26D'))

            with context('si 1 máquina 250kVA'):
                with it('must be TI-27D'):
                    self.c.potencia = 250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-27D'))

            with context('si 1 máquina 400kVA'):
                with it('must be TI-28D'):
                    self.c.potencia = 400
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-28D'))

            with context('si 1 máquina 630kVA'):
                with it('must be TI-29D'):
                    self.c.potencia = 630
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-29D'))

            with context('si 1 máquina 1000kVA'):
                with it('must be TI-30D'):
                    self.c.potencia = 1000
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-30D'))

            with context('si 1 máquina 1250kVA'):
                with it('must be TI-31D'):
                    self.c.potencia = 1250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-31D'))

    with context('si 12kV>=tension>1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 2

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-32U'):
                    self.c.potencia = 15
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-32U'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 30kVA'):
                with it('must be TI-33U'):
                    self.c.potencia = 30
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-33U'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-34U'):
                    self.c.potencia = 50
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-34U'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-35U'):
                    self.c.potencia = 100
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-35U'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-36U'):
                    self.c.potencia = 160
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-36U'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-37U'):
                    self.c.potencia = 250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-37U'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-38U'):
                    self.c.potencia = 400
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-38U'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-39U'):
                    self.c.potencia = 630
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-39U'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-40U'):
                    self.c.potencia = 1000
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-40U'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-41U'):
                    self.c.potencia = 1250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-41U'))

    with context('si 17.5kV>=tension>12kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 2

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-32V'):
                    self.c.potencia = 15
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-32V'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-33V'):
                    self.c.potencia = 25
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-33V'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-34V'):
                    self.c.potencia = 50
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-34V'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-35V'):
                    self.c.potencia = 100
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-35V'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-36V'):
                    self.c.potencia = 160
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-36V'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 240kVA'):
                with it('must be TI-37V'):
                    self.c.potencia = 240
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-37V'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-38V'):
                    self.c.potencia = 400
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-38V'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-39V'):
                    self.c.potencia = 630
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-39V'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-40V'):
                    self.c.potencia = 1000
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-40V'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-41V'):
                    self.c.potencia = 1250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-41V'))

    with context('si 24kV>=tension>17.5kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 2

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-32W'):
                    self.c.potencia = 15
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-32W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-33W'):
                    self.c.potencia = 25
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-33W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-34W'):
                    self.c.potencia = 50
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-34W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-35W'):
                    self.c.potencia = 100
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-35W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-36W'):
                    self.c.potencia = 160
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-36W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-37W'):
                    self.c.potencia = 250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-37W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-38W'):
                    self.c.potencia = 400
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-38W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquina2 400kVA'):
                with it('must be TI-38W'):
                    self.c.potencia = 400
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-38W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-39W'):
                    self.c.potencia = 630
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-39W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-40W'):
                    self.c.potencia = 1000
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-40W'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-41W'):
                    self.c.potencia = 1250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-41W'))

    with context('si 36kV>=tension>24kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 2

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-32B'):
                    self.c.potencia = 15
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-32B'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-33B'):
                    self.c.potencia = 25
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-33B'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-34B'):
                    self.c.potencia = 50
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-34B'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-35B'):
                    self.c.potencia = 100
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-35B'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-36B'):
                    self.c.potencia = 160
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-36B'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-37B'):
                    self.c.potencia = 250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-37B'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-38B'):
                    self.c.potencia = 400
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-38B'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-39B'):
                    self.c.potencia = 630
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-39B'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-40B'):
                    self.c.potencia = 1000
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-40B'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-41B'):
                    self.c.potencia = 1250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-41B'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 2

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-32C'):
                    self.c.potencia = 15
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-32C'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-33C'):
                    self.c.potencia = 25
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-33C'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-34C'):
                    self.c.potencia = 50
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-34C'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-35C'):
                    self.c.potencia = 100
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-35C'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-36C'):
                    self.c.potencia = 160
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-36C'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-37C'):
                    self.c.potencia = 250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-37C'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-38C'):
                    self.c.potencia = 400
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-38C'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-39C'):
                    self.c.potencia = 630
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-39C'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-40C'):
                    self.c.potencia = 1000
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-40C'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-41C'):
                    self.c.potencia = 1250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-41C'))

    with context('si 72.5kV>=tension>52kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 2

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-32D'):
                    self.c.potencia = 15
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-32D'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-33D'):
                    self.c.potencia = 25
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-33D'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-34D'):
                    self.c.potencia = 50
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-34D'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-35D'):
                    self.c.potencia = 100
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-35D'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-36D'):
                    self.c.potencia = 160
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-36D'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-37D'):
                    self.c.potencia = 250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-37D'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-38D'):
                    self.c.potencia = 400
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-38D'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-39D'):
                    self.c.potencia = 630
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-39D'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-40D'):
                    self.c.potencia = 1000
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-40D'))

        with context('si situacion es Caseta'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-41D'):
                    self.c.potencia = 1250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-41D'))

    with context('si 12kV>=tension>=1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 1

        with context('si situacion es Local'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-42U'):
                    self.c.potencia = 15
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-42U'))

        with context('si situacion es Local'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-43U'):
                    self.c.potencia = 25
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-43U'))

        with context('si situacion es Local'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-44U'):
                    self.c.potencia = 50
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-44U'))

        with context('si situacion es Local'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-45U'):
                    self.c.potencia = 100
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-45U'))

        with context('si situacion es Local'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-46U'):
                    self.c.potencia = 160
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-46U'))

        with context('si situacion es Local'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-47U'):
                    self.c.potencia = 250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-47U'))

        with context('si situacion es Local'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-48U'):
                    self.c.potencia = 400
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-48U'))

        with context('si situacion es Local'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-49U'):
                    self.c.potencia = 630
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-49U'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-50U'):
                    self.c.potencia = 1000
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-50U'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-51U'):
                    self.c.potencia = 1250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-51U'))

    with context('si 17.5kV>=tension>12kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 1

        with context('si situacion es Local'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-42V'):
                    self.c.potencia = 15
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-42V'))

        with context('si situacion es Local'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-43V'):
                    self.c.potencia = 25
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-43V'))

        with context('si situacion es Local'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-44V'):
                    self.c.potencia = 50
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-44V'))

        with context('si situacion es Local'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-45V'):
                    self.c.potencia = 100
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-45V'))

        with context('si situacion es Local'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-46V'):
                    self.c.potencia = 160
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-46V'))

        with context('si situacion es Local'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-47V'):
                    self.c.potencia = 250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-47V'))

        with context('si situacion es Local'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-48V'):
                    self.c.potencia = 400
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-48V'))

        with context('si situacion es Local'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-49V'):
                    self.c.potencia = 630
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-49V'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-50V'):
                    self.c.potencia = 1000
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-50V'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-51V'):
                    self.c.potencia = 1250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-51V'))

    with context('si 24kV>=tension>17.5kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 1

        with context('si situacion es Local'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-42W'):
                    self.c.potencia = 15
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-42W'))

        with context('si situacion es Local'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-43W'):
                    self.c.potencia = 25
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-43W'))

        with context('si situacion es Local'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-44W'):
                    self.c.potencia = 50
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-44W'))

        with context('si situacion es Local'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-45W'):
                    self.c.potencia = 100
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-45W'))

        with context('si situacion es Local'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-46W'):
                    self.c.potencia = 160
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-46W'))

        with context('si situacion es Local'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-47W'):
                    self.c.potencia = 250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-47W'))

        with context('si situacion es Local'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-48W'):
                    self.c.potencia = 400
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-48W'))

        with context('si situacion es Local'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-49W'):
                    self.c.potencia = 630
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-49W'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-50W'):
                    self.c.potencia = 1000
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-50W'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-51W'):
                    self.c.potencia = 1250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-51W'))

    with context('si 36kV>=tension>24kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 1

        with context('si situacion es Local'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-42B'):
                    self.c.potencia = 15
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-42B'))

        with context('si situacion es Local'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-43B'):
                    self.c.potencia = 25
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-43B'))

        with context('si situacion es Local'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-44B'):
                    self.c.potencia = 50
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-44B'))

        with context('si situacion es Local'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-45B'):
                    self.c.potencia = 100
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-45B'))

        with context('si situacion es Local'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-46B'):
                    self.c.potencia = 160
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-46B'))

        with context('si situacion es Local'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-47B'):
                    self.c.potencia = 250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-47B'))

        with context('si situacion es Local'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-48B'):
                    self.c.potencia = 400
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-48B'))

        with context('si situacion es Local'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-49B'):
                    self.c.potencia = 630
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-49B'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-50B'):
                    self.c.potencia = 1000
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-50B'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-51B'):
                    self.c.potencia = 1250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-51B'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 1

        with context('si situacion es Local'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-42C'):
                    self.c.potencia = 15
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-42C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-43C'):
                    self.c.potencia = 25
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-43C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-44C'):
                    self.c.potencia = 50
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-44C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-45C'):
                    self.c.potencia = 100
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-45C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-46C'):
                    self.c.potencia = 160
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-46C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-47C'):
                    self.c.potencia = 250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-47C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-48C'):
                    self.c.potencia = 400
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-48C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-49C'):
                    self.c.potencia = 630
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-49C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-50C'):
                    self.c.potencia = 1000
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-50C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-51C'):
                    self.c.potencia = 1250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-51C'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-51C'):
                    self.c.potencia = 1250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-51C'))

    with context('si 72.5kV>=tension>52V'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 1

        with context('si situacion es Local'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-42D'):
                    self.c.potencia = 15
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-42D'))

        with context('si situacion es Local'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-43D'):
                    self.c.potencia = 25
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-43D'))

        with context('si situacion es Local'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-44D'):
                    self.c.potencia = 50
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-44D'))

        with context('si situacion es Local'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-45D'):
                    self.c.potencia = 100
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-45D'))

        with context('si situacion es Local'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-46D'):
                    self.c.potencia = 160
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-46D'))

        with context('si situacion es Local'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-47D'):
                    self.c.potencia = 250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-47D'))

        with context('si situacion es Local'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-48D'):
                    self.c.potencia = 400
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-48D'))

        with context('si situacion es Local'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-49D'):
                    self.c.potencia = 630
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-49D'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-50D'):
                    self.c.potencia = 1000
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-50D'))

        with context('si situacion es Local'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-51D'):
                    self.c.potencia = 1250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-51D'))

    with context('si 12kV>=tension>=1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 2

        with context('si situacion es Local'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-52U'):
                    self.c.potencia = 15
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-52U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-53U'):
                    self.c.potencia = 25
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-53U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-54U'):
                    self.c.potencia = 50
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-54U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-55U'):
                    self.c.potencia = 100
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-55U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-55U'):
                    self.c.potencia = 100
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-55U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-56U'):
                    self.c.potencia = 160
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-56U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-57U'):
                    self.c.potencia = 250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-57U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-58U'):
                    self.c.potencia = 400
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-58U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-59U'):
                    self.c.potencia = 630
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-59U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-60U'):
                    self.c.potencia = 1000
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-60U'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-61U'):
                    self.c.potencia = 1250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-61U'))

    with context('si 17.5kV>=tension>12kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 2

        with context('si situacion es Local'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-52V'):
                    self.c.potencia = 15
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-52V'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-53V'):
                    self.c.potencia = 25
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-53V'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-54V'):
                    self.c.potencia = 50
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-54V'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-55V'):
                    self.c.potencia = 100
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-55V'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-56V'):
                    self.c.potencia = 160
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-56V'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-57V'):
                    self.c.potencia = 250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-57V'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-58V'):
                    self.c.potencia = 400
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-58V'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-59V'):
                    self.c.potencia = 630
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-59V'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-60V'):
                    self.c.potencia = 1000
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-60V'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-61V'):
                    self.c.potencia = 1250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-61V'))

    with context('si 24kV>=tension>17.5kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 2

        with context('si situacion es Local'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-52W'):
                    self.c.potencia = 15
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-52W'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-53W'):
                    self.c.potencia = 25
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-53W'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-54W'):
                    self.c.potencia = 50
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-54W'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-55W'):
                    self.c.potencia = 100
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-55W'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-56W'):
                    self.c.potencia = 160
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-56W'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-57W'):
                    self.c.potencia = 250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-57W'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-58W'):
                    self.c.potencia = 400
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-58W'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-59W'):
                    self.c.potencia = 630
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-59W'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-60W'):
                    self.c.potencia = 1000
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-60W'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-61W'):
                    self.c.potencia = 1250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-61W'))

    with context('si 36kV>=tension>24kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 2

        with context('si situacion es Local'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-52B'):
                    self.c.potencia = 15
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-52B'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-53B'):
                    self.c.potencia = 25
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-53B'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-54B'):
                    self.c.potencia = 50
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-54B'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-55B'):
                    self.c.potencia = 100
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-55B'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-56B'):
                    self.c.potencia = 160
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-56B'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-57B'):
                    self.c.potencia = 250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-57B'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-58B'):
                    self.c.potencia = 400
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-58B'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-59B'):
                    self.c.potencia = 630
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-59B'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-60B'):
                    self.c.potencia = 1000
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-60B'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-61B'):
                    self.c.potencia = 1250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-61B'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 2

        with context('si situacion es Local'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-52C'):
                    self.c.potencia = 15
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-52C'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-53C'):
                    self.c.potencia = 25
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-53C'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-54C'):
                    self.c.potencia = 50
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-54C'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-55C'):
                    self.c.potencia = 100
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-55C'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-56C'):
                    self.c.potencia = 160
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-56C'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-57C'):
                    self.c.potencia = 250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-57C'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-58C'):
                    self.c.potencia = 400
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-58C'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-59C'):
                    self.c.potencia = 630
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-59C'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-60C'):
                    self.c.potencia = 1000
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-60C'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-61C'):
                    self.c.potencia = 1250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-61C'))

    with context('si 72.5kV>=tension>52kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 2

        with context('si situacion es Local'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-52D'):
                    self.c.potencia = 15
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-52D'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-53D'):
                    self.c.potencia = 25
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-53D'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-54D'):
                    self.c.potencia = 50
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-54D'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-55D'):
                    self.c.potencia = 100
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-55D'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-56D'):
                    self.c.potencia = 160
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-56D'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-57D'):
                    self.c.potencia = 250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-57D'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-58D'):
                    self.c.potencia = 400
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-58D'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-59D'):
                    self.c.potencia = 630
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-59D'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-60D'):
                    self.c.potencia = 1000
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-60D'))

        with context('si situacion es Local'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-61D'):
                    self.c.potencia = 1250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-61D'))

    with context('si 12kV>=tension>=1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'I'
            self.c.numero_maquinas = 1

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-62U'):
                    self.c.potencia = 15
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-62U'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-63U'):
                    self.c.potencia = 25
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-63U'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-64U'):
                    self.c.potencia = 50
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-64U'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-65U'):
                    self.c.potencia = 100
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-65U'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-66U'):
                    self.c.potencia = 160
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-66U'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-67U'):
                    self.c.potencia = 250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-67U'))

    with context('si 17.5kV>=tension>12kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'I'
            self.c.numero_maquinas = 1

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-62V'):
                    self.c.potencia = 15
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-62V'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-63V'):
                    self.c.potencia = 25
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-63V'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-64V'):
                    self.c.potencia = 50
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-64V'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-65V'):
                    self.c.potencia = 100
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-65V'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-66V'):
                    self.c.potencia = 160
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-66V'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-67V'):
                    self.c.potencia = 250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-67V'))

    with context('si 24kV>=tension>17.5kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'I'

        with context('si situacion es Intemprerie'):
            with context('si máquinas 15kVA'):
                with it('must be TI-62W'):
                    self.c.potencia = 15
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-62W'))

        with context('si situacion es Intemprerie'):
            with context('si máquinas 25kVA'):
                with it('must be TI-63W'):
                    self.c.potencia = 25
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-63W'))

        with context('si situacion es Intemprerie'):
            with context('si máquinas 100kVA'):
                with it('must be TI-64W'):
                    self.c.potencia = 50
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-64W'))

        with context('si situacion es Intemprerie'):
            with context('si máquinas 160kVA'):
                with it('must be TI-65W'):
                    self.c.potencia = 100
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-65W'))

        with context('si situacion es Intemprerie'):
            with context('si máquinas 160kVA'):
                with it('must be TI-66W'):
                    self.c.potencia = 160
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-66W'))

        with context('si situacion es Intemprerie'):
            with context('si máquinas 250kVA'):
                with it('must be TI-67W'):
                    self.c.potencia = 250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-67W'))

    with context('si 36kV>=tension>24kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'I'
            self.c.numero_maquinas = 2

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-62B'):
                    self.c.potencia = 15
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-62B'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-63B'):
                    self.c.potencia = 25
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-63B'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-64B'):
                    self.c.potencia = 50
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-64B'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-65B'):
                    self.c.potencia = 100
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-65B'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-66B'):
                    self.c.potencia = 160
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-66B'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-66B'):
                    self.c.potencia = 250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-67B'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'I'
            self.c.numero_maquinas = 1

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-62C'):
                    self.c.potencia = 15
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-62C'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-63C'):
                    self.c.potencia = 25
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-63C'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-64C'):
                    self.c.potencia = 50
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-64C'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-65C'):
                    self.c.potencia = 100
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-65C'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-66C'):
                    self.c.potencia = 160
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-66C'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-67C'):
                    self.c.potencia = 250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-67C'))

    with context('si 72.5kV>=tension>52kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'I'
            self.c.numero_maquinas = 1

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-62D'):
                    self.c.potencia = 15
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-62D'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-63D'):
                    self.c.potencia = 25
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-63D'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-64D'):
                    self.c.potencia = 50
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-64D'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-65D'):
                    self.c.potencia = 100
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-65D'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-66D'):
                    self.c.potencia = 160
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-66D'))

        with context('si situacion es Intemprerie'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-67D'):
                    self.c.potencia = 250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-67D'))

    with context('si 12kV>=tension>=1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 1

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-68U'):
                    self.c.potencia = 15
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-68U'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-69U'):
                    self.c.potencia = 25
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-69U'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-70U'):
                    self.c.potencia = 50
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-70U'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-71U'):
                    self.c.potencia = 100
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-71U'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-72U'):
                    self.c.potencia = 160
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-72U'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-73U'):
                    self.c.potencia = 250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-73U'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-74U'):
                    self.c.potencia = 400
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-74U'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-75U'):
                    self.c.potencia = 630
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-75U'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-76U'):
                    self.c.potencia = 1000
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-76U'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-77U'):
                    self.c.potencia = 1250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-77U'))

    with context('si 12kV>=tension>=1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-78U'):
                    self.c.potencia = 15
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-78U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-79U'):
                    self.c.potencia = 25
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-79U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-80U'):
                    self.c.potencia = 50
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-80U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-81U'):
                    self.c.potencia = 100
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-81U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-82U'):
                    self.c.potencia = 160
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-82U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-82U'):
                    self.c.potencia = 160
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-82U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-83U'):
                    self.c.potencia = 250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-83U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-84U'):
                    self.c.potencia = 400
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-84U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-85U'):
                    self.c.potencia = 630
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-85U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-86U'):
                    self.c.potencia = 1000
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-86U'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-87U'):
                    self.c.potencia = 1250
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-87U'))

    with context('si 17.5kV>=tension>12kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 1

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-68V'):
                    self.c.potencia = 15
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-68V'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-69V'):
                    self.c.potencia = 25
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-69V'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-70V'):
                    self.c.potencia = 50
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-70V'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-71V'):
                    self.c.potencia = 100
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-71V'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-72V'):
                    self.c.potencia = 160
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-72V'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-73V'):
                    self.c.potencia = 250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-73V'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-74V'):
                    self.c.potencia = 400
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-74V'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-75V'):
                    self.c.potencia = 630
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-75V'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-76V'):
                    self.c.potencia = 1000
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-76V'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-77V'):
                    self.c.potencia = 1250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-77V'))

    with context('si 17.5kV>=tension>12kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-78V'):
                    self.c.potencia = 15
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-78V'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-79V'):
                    self.c.potencia = 25
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-79V'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-80V'):
                    self.c.potencia = 50
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-80V'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-81V'):
                    self.c.potencia = 100
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-81V'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-82V'):
                    self.c.potencia = 160
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-82V'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-83V'):
                    self.c.potencia = 250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-83V'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-84V'):
                    self.c.potencia = 400
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-84V'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-85V'):
                    self.c.potencia = 630
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-85V'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-86V'):
                    self.c.potencia = 1000
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-86V'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-87V'):
                    self.c.potencia = 1250
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-87V'))

    with context('si 24kV>=tension>17.5kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 1

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-68W'):
                    self.c.potencia = 15
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-68W'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-69W'):
                    self.c.potencia = 25
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-69W'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-70W'):
                    self.c.potencia = 50
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-70W'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-71W'):
                    self.c.potencia = 100
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-71W'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-72W'):
                    self.c.potencia = 160
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-72W'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-73W'):
                    self.c.potencia = 250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-73W'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-74W'):
                    self.c.potencia = 400
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-74W'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-75W'):
                    self.c.potencia = 630
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-75W'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-76W'):
                    self.c.potencia = 1000
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-76W'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-77W'):
                    self.c.potencia = 1250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-77W'))

    with context('si 24kV>=tension>17.5kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-78W'):
                    self.c.potencia = 15
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-78W'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-79W'):
                    self.c.potencia = 25
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-79W'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-80W'):
                    self.c.potencia = 50
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-80W'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-81W'):
                    self.c.potencia = 100
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-81W'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-82W'):
                    self.c.potencia = 160
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-82W'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-83W'):
                    self.c.potencia = 250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-83W'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-84W'):
                    self.c.potencia = 400
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-84W'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-85W'):
                    self.c.potencia = 630
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-85W'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-86W'):
                    self.c.potencia = 1000
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-86W'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-87W'):
                    self.c.potencia = 1250
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-87W'))

    with context('si 36kV>=tension>24kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 1

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-68B'):
                    self.c.potencia = 15
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-68B'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-69B'):
                    self.c.potencia = 25
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-69B'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-70B'):
                    self.c.potencia = 50
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-70B'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-71B'):
                    self.c.potencia = 100
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-71B'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-72B'):
                    self.c.potencia = 160
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-72B'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-73B'):
                    self.c.potencia = 250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-73B'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-74B'):
                    self.c.potencia = 400
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-74B'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-75B'):
                    self.c.potencia = 630
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-75B'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-76B'):
                    self.c.potencia = 1000
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-76B'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-77B'):
                    self.c.potencia = 1250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-77B'))

    with context('si 36kV>=tension>24kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-78B'):
                    self.c.potencia = 15
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-78B'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-79B'):
                    self.c.potencia = 25
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-79B'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-80B'):
                    self.c.potencia = 50
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-80B'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-81B'):
                    self.c.potencia = 100
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-81B'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-82B'):
                    self.c.potencia = 160
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-82B'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-83B'):
                    self.c.potencia = 250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-83B'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-84B'):
                    self.c.potencia = 400
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-84B'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-85B'):
                    self.c.potencia = 630
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-85B'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-86B'):
                    self.c.potencia = 1000
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-86B'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-87B'):
                    self.c.potencia = 1250
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-87B'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 1

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-68C'):
                    self.c.potencia = 15
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-68C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-69C'):
                    self.c.potencia = 25
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-69C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-70C'):
                    self.c.potencia = 50
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-70C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-71C'):
                    self.c.potencia = 100
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-71C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-72C'):
                    self.c.potencia = 160
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-72C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-73C'):
                    self.c.potencia = 250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-73C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-74C'):
                    self.c.potencia = 400
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-74C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-75C'):
                    self.c.potencia = 630
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-75C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-76C'):
                    self.c.potencia = 1000
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-76C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-77C'):
                    self.c.potencia = 1250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-77C'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-77C'):
                    self.c.potencia = 1250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-77C'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-78C'):
                    self.c.potencia = 15
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-78C'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-79C'):
                    self.c.potencia = 25
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-79C'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-80C'):
                    self.c.potencia = 50
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-80C'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-81C'):
                    self.c.potencia = 100
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-81C'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-82C'):
                    self.c.potencia = 160
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-82C'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-83C'):
                    self.c.potencia = 250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-83C'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-84C'):
                    self.c.potencia = 400
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-84C'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-85C'):
                    self.c.potencia = 630
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-85C'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-86C'):
                    self.c.potencia = 1000
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-86C'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-87C'):
                    self.c.potencia = 1250
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-87C'))

    with context('si 72.5kV>=tension>52kV'):
        with before.each:
            self.c.situacion = 'S'
            self.c.numero_maquinas = 1

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 15kVA'):
                with it('must be TI-68D'):
                    self.c.potencia = 15
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-68D'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 25kVA'):
                with it('must be TI-69D'):
                    self.c.potencia = 25
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-69D'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 50kVA'):
                with it('must be TI-70D'):
                    self.c.potencia = 50
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-70D'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 100kVA'):
                with it('must be TI-71D'):
                    self.c.potencia = 100
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-71D'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 160kVA'):
                with it('must be TI-72D'):
                    self.c.potencia = 160
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-72D'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 250kVA'):
                with it('must be TI-73D'):
                    self.c.potencia = 250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-73D'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 400kVA'):
                with it('must be TI-74D'):
                    self.c.potencia = 400
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-74D'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 630kVA'):
                with it('must be TI-75D'):
                    self.c.potencia = 630
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-75D'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1000kVA'):
                with it('must be TI-76D'):
                    self.c.potencia = 1000
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-76D'))

        with context('si situacion es Subterraneo'):
            with context('si 1 máquina 1250kVA'):
                with it('must be TI-77D'):
                    self.c.potencia = 1250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-77D'))

    with context('si 72.5kV>=tension>52kV'):
        with before.each:
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 15kVA'):
                with it('must be TI-78D'):
                    self.c.potencia = 15
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-78D'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 25kVA'):
                with it('must be TI-79D'):
                    self.c.potencia = 25
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-79D'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 50kVA'):
                with it('must be TI-80D'):
                    self.c.potencia = 50
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-80D'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 100kVA'):
                with it('must be TI-81D'):
                    self.c.potencia = 100
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-81D'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 160kVA'):
                with it('must be TI-82D'):
                    self.c.potencia = 160
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-82D'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 250kVA'):
                with it('must be TI-83D'):
                    self.c.potencia = 250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-83D'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 400kVA'):
                with it('must be TI-84D'):
                    self.c.potencia = 400
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-84D'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 630kVA'):
                with it('must be TI-85D'):
                    self.c.potencia = 630
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-85D'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1000kVA'):
                with it('must be TI-86D'):
                    self.c.potencia = 1000
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-86D'))

        with context('si situacion es Subterraneo'):
            with context('si 2 máquinas 1250kVA'):
                with it('must be TI-87D'):
                    self.c.potencia = 1250
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-87D'))

    with context('si Centor de reparto,seccionamiento o de reflexion sin transformacion'):
        with before.each:
            self.c = CT()
            self.c.numero_maquinas = 0

        with context('si situacion es Caseta'):
            with context('si 12kV>= tension >=1kV'):
                with it('must be TI-0CU'):
                    self.c.situacion = 'C'
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0CU'))

        with context('si situacion es Intemperie'):
            with context('si 12kV>= tension >=1kV'):
                with it('must be TI-0IU'):
                    self.c.situacion = 'I'
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0IU'))

        with context('si situacion es Local'):
            with context('si 12kV>= tension >=1kV'):
                with it('msut be TI-0LU'):
                    self.c.situacion = 'L'
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0LU'))

        with context('si situacion es Subterraneo'):
            with context('si 12kV>= tension >=1kV'):
                with it('must be TI-0SU'):
                    self.c.situacion = 'S'
                    for t in range(1, 12):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0SU'))

        with context('si situacion es Caseta'):
            with context('si 17.5kV>= tension >12kV'):
                with it('must be TI-0CV'):
                    self.c.situacion = 'C'
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0CV'))

        with context('si situacion es Intemperie'):
            with context('si 17.5kV>= tension >12kV'):
                with it('must be TI-0IV'):
                    self.c.situacion = 'I'
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0IV'))

        with context('si situacion es Local'):
            with context('si 17.5kV>= tension >12kV'):
                with it('must be TI-0LV'):
                    self.c.situacion = 'L'
                    for t in range(13, 17) +[17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0LV'))

        with context('si situacion es Subterraneo'):
            with context('si 17.5kV>= tension >12kV'):
                with it('must be TI-0SV'):
                    self.c.situacion = 'S'
                    for t in range(13, 17) + [17.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0SV'))


        with context('si situacion es Caseta'):
            with context('si 24V>= tension >17.5kV'):
                with it('must be TI-0CW'):
                    self.c.situacion = 'C'
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0CW'))

        with context('si situacion es Intemperie'):
            with context('si 24kV>= tension >17.5kV'):
                with it('must be TI-0IW'):
                    self.c.situacion = 'I'
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0IW'))

        with context('si situacion es Local'):
            with context('si 24kV>= tension >17.5kV'):
                with it('must be TI-0LW'):
                    self.c.situacion = 'L'
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0LW'))

        with context('si situacion es Subterraneo'):
            with context('si 24kV>= tension >17.5kV'):
                with it('must be TI-0SW'):
                    self.c.situacion = 'S'
                    for t in range(18, 24):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0SW'))


        with context('si situacion es Caseta'):
            with context('si 36kV>= tension >24kV'):
                with it('must be TI-0CX'):
                    self.c.situacion = 'C'
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0CX'))

        with context('si situacion es Intemperie'):
            with context('si 36kV>= tension >24kV'):
                with it('must be TI-0IX'):
                    self.c.situacion = 'I'
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0IX'))

        with context('si situacion es Local'):
            with context('si 36kV>= tension >24kV'):
                with it('must be TI-0LX'):
                    self.c.situacion = 'L'
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0LX'))

        with context('si situacion es Subterraneo'):
            with context('si 36kV>= tension >24kV'):
                with it('must be TI-0SX'):
                    self.c.situacion = 'S'
                    for t in range(25, 36):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0SX'))

        with context('si situacion es Caseta'):
            with context('si 52kV>= tension >36kV'):
                with it('must be TI-0CY'):
                    self.c.situacion = 'C'
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0CY'))

        with context('si situacion es Intemperie'):
            with context('si 52kV>= tension >36kV'):
                with it('must be TI-0IY'):
                    self.c.situacion = 'I'
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0IY'))

        with context('si situacion es Local'):
            with context('si 52kV>= tension >36kV'):
                with it('must be TI-0LY'):
                    self.c.situacion = 'L'
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0LY'))

        with context('si situacion es Subterraneo'):
            with context('si 52kV>= tension >36kV'):
                with it('must be TI-0SY'):
                    self.c.situacion = 'S'
                    for t in range(37, 52):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0SY'))

        with context('si situacion es Caseta'):
            with context('si 72.5kV>= tension >52kV'):
                with it('must be TI-0CZ'):
                    self.c.situacion = 'C'
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0CZ'))

        with context('si situacion es Intemperie'):
            with context('si 72.5kV>= tension >52kV'):
                with it('must be TI-0IZ'):
                    self.c.situacion = 'I'
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0IZ'))

        with context('si situacion es Local'):
            with context('si 72.5kV>= tension >52kV'):
                with it('must be TI-0LZ'):
                    self.c.situacion = 'L'
                    for t in range(53, 72) + [72.5]:
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0LZ'))

        with context('si situacion es Subterraneo'):
            with context('si 72.5kV>= tension >52kV'):
                with it('must be TI-0SZ'):
                    self.c.situacion = 'S'
                    for t in range(53, 72):
                        self.c.tension = t
                        expect(self.c.tipoinstalacion).to(equal('TI-0SZ'))