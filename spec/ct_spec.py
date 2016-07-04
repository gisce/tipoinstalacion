# coding=utf-8
from tipoinstalacion.models import CT

from expects import expect, equal

with description('Calculando el TI de un CT'):

    with context('si 12kV>=tension>1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 1

            with context('si situacion es Caseta'):
                with context('si 1 máquina 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-22U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-22U'))

                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-23U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-23U'))

                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-24U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-24U'))

                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-25U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-25U'))

                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-26U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-26U'))

                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-27U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-27U'))

                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-28U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-28U'))

                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-29U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-29U'))

                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-30U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-30U'))

                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-30U'):
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
                    self.c.potencia = 15
                    with it('must be TI-22V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-22V'))

                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-23V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-23V'))

                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-24V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-24V'))

                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-25V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-25V'))

                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-26V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-26V'))

                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-27V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-27V'))

                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-28V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-28V'))

                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-29V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-29V'))

                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-30V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-30V'))

                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-31V'):
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
                    self.c.potencia = 15
                    with it('must be TI-22W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-22W'))

                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-23W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-23W'))

                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-24W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-24W'))

                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-25W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-25W'))

                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-26W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-26W'))

                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-27W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-27W'))

                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-28W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-28W'))

                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-29W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-29W'))

                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-30W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-30W'))

                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-31W'):
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
                    self.c.potencia = 15
                    with it('must be TI-22B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-22B'))

                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-23B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-23B'))

                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-24B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-24B'))

                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-25B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-25B'))

                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-26B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-26B'))

                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-27B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-27B'))

                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-28B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-28B'))

                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-29B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-29B'))

                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-30B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-30B'))

                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-31B'):
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
                    self.c.potencia = 15
                    with it('must be TI-22C'):
                        for t in range(25, 37):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-22C'))

                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-23C'):
                        for t in range(25, 37):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-23C'))

                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-24C'):
                        for t in range(25, 37):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-24C'))

                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-25C'):
                        for t in range(25, 37):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-25C'))

                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-26C'):
                         for t in range(25, 37):
                             self.c.tension = t
                             expect(self.c.tipoinstalacion).to(equal('TI-26C'))

                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-27C'):
                        for t in range(25, 37):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-27C'))

                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-28C'):
                        for t in range(25, 37):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-28C'))

                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-29C'):
                        for t in range(25, 37):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-29C'))

                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-30C'):
                        for t in range(25, 37):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-30C'))

                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-31C'):
                        for t in range(25, 37):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-31C'))

    with context('si 12kV>=tension>1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'C'
            self.c.numero_maquinas = 1

            with context('si situacion es Caseta'):
                with context('si 1 máquina 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-22D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-22D'))

                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-23D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-23D'))

                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-24D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-24D'))

                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-25D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-25D'))

                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-26D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-26D'))

                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-27D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-27D'))

                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-28D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-28D'))

                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-29D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-29D'))

                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-30D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-30D'))

                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-31D'):
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
                    self.c.potencia = 15
                    with it('must be TI-32U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-32U'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 30kVA'):
                    self.c.potencia = 30
                    with it('must be TI-33U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-33U'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-34U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-34U'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-35U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-35U'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-36U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-36U'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-37U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-37U'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-38U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-38U'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-39U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-39U'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-40U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-40U'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-41U'):
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
                    self.c.potencia = 15
                    with it('must be TI-32V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-32V'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-33V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-33V'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-34V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-34V'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-35V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-35V'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-36V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-36V'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 240kVA'):
                    self.c.potencia = 240
                    with it('must be TI-37V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-37V'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-38V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-38V'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-39V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-39V'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-40V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-40V'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-41V'):
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
                    self.c.potencia = 15
                    with it('must be TI-32W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-32W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-33W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-33W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-34W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-34W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-35W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-35W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-36W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-36W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-37W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-37W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-38W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-38W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquina2 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-38W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-38W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-39W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-39W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-40W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-40W'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-41W'):
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
                    self.c.potencia = 15
                    with it('must be TI-32B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-32B'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-33B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-33B'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-34B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-34B'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-35B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-35B'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-36B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-36B'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-37B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-37B'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-38B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-38B'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-39B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-39B'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-40B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-40B'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-41B'):
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
                    self.c.potencia = 15
                    with it('must be TI-32C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-32C'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-33C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-33C'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-34C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-34C'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-35C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-35C'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-36C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-36C'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-37C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-37C'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-38C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-38C'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-39C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-39C'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-40C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-40C'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-41C'):
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
                    self.c.potencia = 15
                    with it('must be TI-32D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-32D'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-33D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-33D'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-34D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-34D'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-35D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-35D'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-36D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-36D'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-37D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-37D'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-38D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-38D'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-39D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-39D'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-40D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-40D'))

            with context('si situacion es Caseta'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-41D'):
                        for t in range(52, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-41D'))

    with context('si 12kV>=tension>=1kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'L'
            self.c.numero_maquinas = 1

            with context('si situacion es Local'):
                with context('si 1 máquina 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-42U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-42U'))

            with context('si situacion es Local'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-43U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-43U'))

            with context('si situacion es Local'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-44U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-44U'))

            with context('si situacion es Local'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-45U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-45U'))

            with context('si situacion es Local'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-46U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-46U'))

            with context('si situacion es Local'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-47U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-47U'))

            with context('si situacion es Local'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-48U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-48U'))

            with context('si situacion es Local'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-49U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-49U'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-50U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-50U'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-51U'):
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
                    self.c.potencia = 15
                    with it('must be TI-42V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-42V'))

            with context('si situacion es Local'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-43V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-43V'))

            with context('si situacion es Local'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-44V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-44V'))

            with context('si situacion es Local'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-45V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-45V'))

            with context('si situacion es Local'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-46V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-46V'))

            with context('si situacion es Local'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-47V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-47V'))

            with context('si situacion es Local'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-48V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-48V'))

            with context('si situacion es Local'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-49V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-49V'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-50V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-50V'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-51V'):
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
                    self.c.potencia = 15
                    with it('must be TI-42W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-42W'))

            with context('si situacion es Local'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-43W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-43W'))

            with context('si situacion es Local'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-44W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-44W'))

            with context('si situacion es Local'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-45W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-45W'))

            with context('si situacion es Local'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-46W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-46W'))

            with context('si situacion es Local'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-47W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-47W'))

            with context('si situacion es Local'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-48W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-48W'))

            with context('si situacion es Local'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-49W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-49W'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-50W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-50W'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-51W'):
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
                    self.c.potencia = 15
                    with it('must be TI-42B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-42B'))

            with context('si situacion es Local'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-43B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-43B'))

            with context('si situacion es Local'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-44B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-44B'))

            with context('si situacion es Local'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-45B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-45B'))

            with context('si situacion es Local'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-46B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-46B'))

            with context('si situacion es Local'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-47B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-47B'))

            with context('si situacion es Local'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-48B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-48B'))

            with context('si situacion es Local'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-49B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-49B'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-50B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-50B'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-51B'):
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
                    self.c.potencia = 15
                    with it('must be TI-42C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-42C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-43C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-43C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-44C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-44C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-45C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-45C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-46C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-46C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-47C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-47C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-48C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-48C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-49C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-49C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-50C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-50C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-51C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-51C'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-51C'):
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
                    self.c.potencia = 15
                    with it('must be TI-42D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-42D'))

            with context('si situacion es Local'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-43D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-43D'))

            with context('si situacion es Local'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-44D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-44D'))

            with context('si situacion es Local'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-45D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-45D'))

            with context('si situacion es Local'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-46D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-46D'))

            with context('si situacion es Local'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-47D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-47D'))

            with context('si situacion es Local'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-48D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-48D'))

            with context('si situacion es Local'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-49D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-49D'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-50D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-50D'))

            with context('si situacion es Local'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-51D'):
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
                    self.c.potencia = 15
                    with it('must be TI-52U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-52U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-53U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-53U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-54U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-54U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-55U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-55U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-55U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-55U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-56U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-56U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-57U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-57U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-58U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-58U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-59U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-59U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-60U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-60U'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-61U'):
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
                    self.c.potencia = 15
                    with it('must be TI-52V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-52V'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-53V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-53V'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-54V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-54V'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-55V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-55V'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-56V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-56V'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-57V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-57V'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-58V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-58V'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-59V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-59V'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-60V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-60V'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-61V'):
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
                    self.c.potencia = 15
                    with it('must be TI-52W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-52W'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-53W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-53W'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-54W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-54W'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-55W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-55W'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-56W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-56W'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-57W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-57W'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-58W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-58W'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-59W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-59W'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-60W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-60W'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-61W'):
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
                    self.c.potencia = 15
                    with it('must be TI-52B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-52B'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-53B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-53B'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-54B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-54B'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-55B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-55B'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-56B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-56B'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-57B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-57B'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-58B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-58B'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-59B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-59B'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-60B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-60B'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-61B'):
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
                    self.c.potencia = 15
                    with it('must be TI-52C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-52C'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-53C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-53C'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-54C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-54C'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-55C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-55C'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-56C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-56C'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-57C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-57C'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-58C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-58C'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-59C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-59C'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-60C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-60C'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-61C'):
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
                    self.c.potencia = 15
                    with it('must be TI-52D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-52D'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-53D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-53D'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-54D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-54D'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-55D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-55D'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-56D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-56D'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-57D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-57D'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-58D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-58D'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-59D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-59D'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-60D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-60D'))

            with context('si situacion es Local'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-61D'):
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
                    self.c.potencia = 15
                    with it('must be TI-62U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-62U'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-63U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-63U'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-64U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-64U'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-65U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-65U'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-66U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-66U'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-67U'):
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
                    self.c.potencia = 25
                    with it('must be TI-62V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-62V'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-63V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-63V'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-64V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-64V'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-65V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-65V'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-66V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-66V'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-67V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-67V'))

    with context('si 24kV>=tension>17.5kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'I'
            self.c.numero_maquinas = 1

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-62W'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-62W'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-63W'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-63W'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-63W'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-63W'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-64W'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-64W'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-65W'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-65W'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-66W'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-66W'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-67W'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-67W'))

    with context('si 36kV>=tension>24kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'I'
            self.c.numero_maquinas = 1

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-62B'):
                        for t in range(25,36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-62B'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-63B'):
                        for t in range(25,36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-63B'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-64B'):
                        for t in range(25,36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-64B'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-65B'):
                        for t in range(25,36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-65B'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-66B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-66B'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-66B'):
                        for t in range(25, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-66B'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'I'
            self.c.numero_maquinas = 1

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-62C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-62C'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-63C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-63C'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-64C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-64C'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-65C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-65C'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-66C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-66C'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-67C'):
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
                    self.c.potencia = 15
                    with it('must be TI-62D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-62D'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-63D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-63D'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-64D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-64D'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-65D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-65D'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-66D'):
                        for t in range(53, 72) + [72.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-66D'))

            with context('si situacion es Intemprerie'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-67D'):
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
                    self.c.potencia = 15
                    with it('must be TI-68U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-68U'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-69U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-69U'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-70U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-70U'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-71U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-71U'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-72U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-72U'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-73U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-73U'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-74U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-74U'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-75U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-75U'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-76U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-76U'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-77U'):
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
                    self.c.potencia = 15
                    with it('must be TI-78U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-78U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-79U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-79U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-80U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-80U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-81U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-81U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-82U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-82U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-82U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-82U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-83U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-83U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-84U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-84U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-85U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-85U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-86U'):
                        for t in range(1, 12):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-86U'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-87U'):
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
                    self.c.potencia = 15
                    with it('must be TI-68V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-68V'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-69V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-69V'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-70V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-70V'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-71V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-71V'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-72V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-72V'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-73V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-73V'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-74V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-74V'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-75V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-75V'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-76V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-76V'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-77V'):
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
                    self.c.potencia = 15
                    with it('must be TI-78V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-78V'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-79V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-79V'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-80V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-80V'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-81V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-81V'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-82V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-82V'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-83V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-83V'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-84V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-84V'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-85V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-85V'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-86V'):
                        for t in range(13, 17) + [17.5]:
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-86V'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-87V'):
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
                    self.c.potencia = 15
                    with it('must be TI-68W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-68W'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-69W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-69W'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-70W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-70W'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-71W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-71W'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-72W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-72W'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-73W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-73W'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-74W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-74W'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-75W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-75W'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-76W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-76W'))

    with context('si 24kV>=tension>17.5kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-78W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-78W'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-79W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-79W'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-80W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-80W'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-81W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-81W'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-82W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-82W'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-83W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-83W'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-84W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-84W'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-85W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-85W'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-86W'):
                        for t in range(18, 24):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-86W'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-87W'):
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
                    self.c.potencia = 15
                    with it('must be TI-68B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-68B'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-69B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-69B'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-70B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-70B'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-71B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-71B'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-72B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-72B'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-73B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-73B'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-74B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-74B'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-75B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-75B'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-76B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-76B'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-77B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-77B'))

    with context('si 36kV>=tension>24kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-78B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-78B'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-79B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-79B'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-80B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-80B'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-81B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-81B'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-82B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-82B'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-83B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-83B'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-84B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-84B'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-85B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-85B'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-86B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-86B'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-87B'):
                        for t in range(24, 36):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-87B'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c = CT()
            self.c.situacion = 'S'
            self.c.numero_maquinas = 1

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-68C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-68C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-69C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-69C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-70C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-70C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-71C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-71C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-72C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-72C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-73C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-73C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-74C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-74C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-75C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-75C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-76C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-76C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-77C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-77C'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-77C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-77C'))

    with context('si 52kV>=tension>36kV'):
        with before.each:
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-78C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-78C'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-79C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-79C'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-80C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-80C'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-81C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-81C'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-82C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-82C'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-83C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-83C'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-84C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-84C'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-85C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-85C'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-86C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-86C'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-87C'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-87C'))

    with context('si 72.5kV>=tension>52kV'):
        with before.each:
            self.c.situacion = 'S'
            self.c.numero_maquinas = 1

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-68D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-68D'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-69D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-69D'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-70D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-70D'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-71D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-71D'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-72D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-72D'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-73D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-73D'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-74D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-74D'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-75D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-75D'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-76D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-76D'))

            with context('si situacion es Subterraneo'):
                with context('si 1 máquina 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-77D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-77D'))

    with context('si 72.5kV>=tension>52kV'):
        with before.each:
            self.c.situacion = 'S'
            self.c.numero_maquinas = 2

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 15kVA'):
                    self.c.potencia = 15
                    with it('must be TI-78D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-78D'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 25kVA'):
                    self.c.potencia = 25
                    with it('must be TI-79D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-79D'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 50kVA'):
                    self.c.potencia = 50
                    with it('must be TI-80D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-80D'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 100kVA'):
                    self.c.potencia = 100
                    with it('must be TI-81D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-81D'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 160kVA'):
                    self.c.potencia = 160
                    with it('must be TI-82D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-82D'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 250kVA'):
                    self.c.potencia = 250
                    with it('must be TI-83D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-83D'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 400kVA'):
                    self.c.potencia = 400
                    with it('must be TI-84D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-84D'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 630kVA'):
                    self.c.potencia = 630
                    with it('must be TI-85D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-85D'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1000kVA'):
                    self.c.potencia = 1000
                    with it('must be TI-86D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-86D'))

            with context('si situacion es Subterraneo'):
                with context('si 2 máquinas 1250kVA'):
                    self.c.potencia = 1250
                    with it('must be TI-87D'):
                        for t in range(37, 52):
                            self.c.tension = t
                            expect(self.c.tipoinstalacion).to(equal('TI-87D'))
