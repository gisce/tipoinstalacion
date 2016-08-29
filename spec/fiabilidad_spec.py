from tipoinstalacion.models import Fiabilidad

from expects import expect, equal


with description('Calculando el TI de un elemento de fibilidad'):
    with before.each:
        self.f = Fiabilidad()
    with context('si tipo Seccionador (de cuchillas)'):
        with it('must be TI-174'):
            self.f.tipoelemento = 'S'
            expect(self.f.tipoinstalacion).to(equal('TI-174'))

    with context('si tipo Reconectador'):
        with it('must be TI-177'):
            self.f.tipoelemento = 'R'
            expect(self.f.tipoinstalacion).to(equal('TI-177'))

    with context('si tipo Reconectador - Seccionador'):
        with it('must be TI-179'):
            self.f.tipoelemento = 'RS'
            expect(self.f.tipoinstalacion).to(equal('TI-179'))

    with context('si tipo Seccionador - Fusible (XS-SXS)'):
        with it('must be TI-181'):
            self.f.tipoelemento = 'SF'
            expect(self.f.tipoinstalacion).to(equal('TI-181'))

    with context('si tipo Autoseccionador/Seccionalizador'):
        with it('must be TI-182'):
            self.f.tipoelemento = 'AS'
            expect(self.f.tipoinstalacion).to(equal('TI-182'))

    with context('si tipo Interruptor'):
        with it('must be TI-183'):
            self.f.tipoelemento = 'I'
            expect(self.f.tipoinstalacion).to(equal('TI-183'))

    with context('si tipo Interruptor-seccionador'):
        with it('must be TI-187'):
            self.f.tipoelemento = 'IS'
            expect(self.f.tipoinstalacion).to(equal('TI-187'))

    with context('si tipo Interruptor-seccionador telecontrolado'):
        with it('must be TI-187A'):
            self.f.tipoelemento = 'IST'
            expect(self.f.tipoinstalacion).to(equal('TI-187A'))