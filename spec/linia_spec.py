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

with description('Calculando el TI de una linia'):
    with context('si lat tensión > 123 kV'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.l.tension = 124
        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea simple circuito-Simplex'):
                with it('must be TI-1UX'):
                    for s in range(1, 180):
                        self.l.seccion = s   
                        expect(self.l.tipoinstalacion).to(equal('TI-1UX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea simple circuito-Simplex'):
                with it('must be TI-1UY'):
                    for s in range(181, 300):
                        self.l.seccion = s
                        expect(self.l.tipoinstalacion).to(equal('TI-1UY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea simple circuito-Simplex'):
                with it('must be TI-1UZ'):
                    self.l.seccion = 301
                    expect(self.l.tipoinstalacion).to(equal('TI-1UZ'))

    with context('si lat tensión > 123 kV'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 2
            self.l.tension = 124
        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea simple circuito-Duplex'):
                with it('must be TI-2UX'):
                    for s in range(1, 180):
                        self.l.seccion = s
                        expect(self.l.tipoinstalacion).to(equal('TI-2UX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea simple circuito-Duplex'):
                with it('must be TI-2UY'):
                    for s in range(181, 300):
                        self.l.seccion = s
                        expect(self.l.tipoinstalacion).to(equal('TI-2UY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea simple circuito-Duplex'):
                with it('must be TI-2UZ'):
                    self.l.seccion = 301
                    expect(self.l.tipoinstalacion).to(equal('TI-2UZ'))

    with context('si lat tensión > 123 kV'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.l.tension = 124
        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea doble circuito-Simplex'):
                with it('TI-3UX'):
                    for s in range(1, 180):
                        self.l.seccion = s
                        expect(self.l.tipoinstalacion).to(equal('TI-3UX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea doble circuito-Simplex'):
                with it('must be TI-3UY'):
                    for s in range(181, 300):
                        self.l.seccion = s
                        expect(self.l.tipoinstalacion).to(equal('TI-3UY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea doble circuito-Simplex'):
                with it('must be TI-3UZ'):
                    self.l.seccion = 301
                    expect(self.l.tipoinstalacion).to(equal('TI-3UZ'))

    with context('si lat tensión > 123 kV'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 2
            self.l.tension = 124
        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea doble circuito-Duplex'):
                with it('must be TI-4UX'):
                    for s in range(1, 180):
                        self.l.seccion = s
                        expect(self.l.tipoinstalacion).to(equal('TI-4UX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea doble circuito-Duplex'):
                with it('must be TI-4UY'):
                    for s in range(181, 300):
                        self.l.seccion = s
                        expect(self.l.tipoinstalacion).to(equal('TI-4UY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea doble circuito-Duplex'):
                with it('must be TI-4UZ'):
                    self.l.seccion = 301
                    expect(self.l.tipoinstalacion).to(equal( 'TI-4UZ'))

    with context('si lat tensión > 123 kV'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.l.tension = 124
        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea triple circuito-Simplex'):
                with it('must be TI-3AUX'):
                    for s in range(1, 180):
                        self.l.seccion = s
                        expect(self.l.tipoinstalacion).to(equal( 'TI-3AUX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea doble circuito-Duplex'):
                with it('must be TI-3AUY'):
                    for s in range(181, 300):
                        self.l.seccion = s
                        expect(self.l.tipoinstalacion).to(equal( 'TI-3AUY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea doble circuito-Duplex'):
                with it('must be TI-3AUZ'):
                    self.l.seccion = 301
                    expect(self.l.tipoinstalacion).to(equal('TI-3AUZ'))

    with context('si la 72,5Kv < tensión<=123Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(73, 123) + [72.6]

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-1VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal( 'TI-1VX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-1VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal( 'TI-1VY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-1VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal( 'TI-1VZ'))

    with context('si la 72,5Kv < tensión<=123Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 2
            self.tensiones = range(73, 123) + [72.6]

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-2VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-2VX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-2VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-2VY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-2VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-2VZ'))

    with context('si la 72,5Kv < tensión<=123Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(73, 123) + [72.6]

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-3VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal( 'TI-3VX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-3VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-3VY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-3VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal( 'TI-3VZ'))

    with context('si la 72,5Kv < tensión<=123Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 2
            self.tensiones = range(73, 123) + [72.6]

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-4VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal( 'TI-4VX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-4VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-4VY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Dupluex'):
                with it('must be TI-4VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal( 'TI-4VZ'))

    with context('si la 72,5Kv < tensión<=123Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(73, 123) + [72.6]

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-3AVX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-3AVX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-3AVY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-3AVY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-3AVZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal( 'TI-3AVZ'))

    with context('si la 52Kv < tensión<=72,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(52, 72) + [72.5]

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-5UX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-5UY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-5UZ'))

    with context('si la 52Kv < tensión<=72,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(52, 72) + [72.5]

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal( 'TI-7UX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-7UY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-7UZ'))

    with context('si la 52Kv < tensión<=72,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 2
            self.tensiones = range(52, 72) + [72.5]

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-8UX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-8UY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-8UZ'))

    with context('si la 52Kv < tensión<=72,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 3
            self.l.num_conductores = 2
            self.tensiones = range(52, 72) + [72.5]

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-7AUZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-7AUY'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-8UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-7AUX'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-8UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-7AUZ'))

    with context('si la  36Kv < tensión <= 52Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(37, 52)

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal( 'TI-5VX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-5VY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-5VZ'))

    with context('si la  36Kv < tensión <= 52Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 2
            self.tensiones = range(37, 52)

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito simple-Duplex'):
                with it('must be TI-6VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal( 'TI-6VX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Duplex'):
                with it('must be TI-6VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-6VY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Duplex'):
                with it('must be TI-6VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-6VZ'))

    with context('si la  36Kv < tensión <= 52Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(37, 52)

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-7VX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal( 'TI-7VY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-7VZ'))

    with context('si la  36Kv < tensión <= 52Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 2
            self.tensiones = range(37, 52)

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal( 'TI-8VX'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-8VY'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-8VZ'))

    with context('si la  36Kv < tensión <= 52Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(37, 52)

        with context('si la sección 0 < s < 180 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-7AVY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 179):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-7AVY'))

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-7AVX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-7AVX'))

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-7AVZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-7AVZ'))

    with context('si la  24Kv < tensión <= 36Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(25, 36)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-9UX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-9UY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-9UZ'))

    with context('si la  24Kv < tensión <= 36Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(25, 36)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10UX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10UY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-10UZ'))

    with context('si la  24Kv < tensión <= 36Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(25, 36)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10AUX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10AUY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-10AUZ'))

    with context('si la  17,5Kv < tensión <= 24Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(18, 24)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-9VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-9VX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-9VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-9VY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-9VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-9VZ'))

    with context('si la  17,5Kv < tensión <= 24Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(18, 24)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-10VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10VX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-10VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10VY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-10VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-10VZ'))

    with context('si la 12Kv < tensión <= 17,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(18, 24)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9WX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-9WX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9WY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-9WY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9WZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-9WZ'))

    with context('si la 12Kv < tensión <= 17,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(18, 24)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito doble'):
                with it('must be TI-10WX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10WX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito doble'):
                with it('must be TI-10WY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10WY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito doble'):
                with it('must be TI-10WZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-10WZ'))

    with context('si la 12Kv < tensión <= 17,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(18, 24)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AWX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10AWX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AWY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10AWY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AWZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-10AWZ'))

    with context('si la 1Kv < tensión <= 12Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(2, 12)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9BX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-9BX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9BY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-9BY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9BZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-9BZ'))

    with context('si la 1Kv < tensión <= 12Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(2, 12)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito doble'):
                with it('must be TI-10BX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10BX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito doble'):
                with it('must be TI-10BY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10BY'))

        with context('si la sección  110 < s '):
            with context('si la linea es Aerea circuito doble'):
                with it('must be TI-10BZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-10BZ'))

    with context('si la 1Kv < tensión <= 12Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(2, 12)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10ABX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10ABX'))

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10ABY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-10ABY'))

        with context('si la sección  110 < s'):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10ABZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 111
                        expect(self.l.tipoinstalacion).to(equal('TI-10ABZ'))

    with context('si la tensión < 1Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.l.tension = 0

        with context('si la sección s < 75 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-11X'):
                    self.l.seccionn = 76
                    expect(self.l.tipoinstalacion).to(equal('TI-11X'))

        with context('si la sección s >= 75'):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-11Y'):
                    for s in range(0, 75):
                        self.l.seccionn = s
                        expect(self.l.tipoinstalacion).to(equal('TI-11Y'))

    with context('si la tensión < 1Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.l.tension = 0

        with context('si la sección s < 75 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-13X'):
                    self.l.seccionn = 76
                    expect(self.l.tipoinstalacion).to(equal('TI-13X'))

        with context('si la sección s >= 75'):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-13Y'):
                    for s in range(0, 75):
                        self.l.seccionn = s
                        expect(self.l.tipoinstalacion).to(equal('TI-13Y'))

    with context('si la tensión < 1Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AF'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.l.tension = 0

        with context('si la sección s < 75 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-12X'):
                    self.l.seccionn = 76
                    expect(self.l.tipoinstalacion).to(equal('TI-12X'))

        with context('si la sección s >= 75'):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-12Y'):
                    for s in range(0, 75):
                        self.l.seccionn = s
                        expect(self.l.tipoinstalacion).to(equal('TI-12Y'))

    with context('si la 123Kv < tensión '):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = [124]

        with context('si la sección 0 < s <= 630 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-14UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 630):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-14UX'))

        with context('si la sección 630 < s <= 1200 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-14UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(631, 1200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-14UY'))

        with context('si la sección  1200 < s  '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-14UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 1201
                        expect(self.l.tipoinstalacion).to(equal('TI-14UZ'))

    with context('si la 123Kv < tensión '):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = [124]

        with context('si la sección 0 < s <= 630 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-15UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 630):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-15UX'))

        with context('si la sección 630 < s <= 1200 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-15UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(631, 1200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-15UY'))

        with context('si la sección  1200 < s '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-15UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 1201
                        expect(self.l.tipoinstalacion).to(equal('TI-15UZ'))

    with context('si la 123Kv < tensión '):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = [124]

        with context('si la sección 0 < s <= 630 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-15UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 630):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-15UX'))

        with context('si la sección 630 < s <= 1200 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-15UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(631, 1200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-15UY'))

        with context('si la sección  1200 < s '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-15UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 1201
                        expect(self.l.tipoinstalacion).to(equal('TI-15UZ'))

    with context('si la 72,5Kv < tensión =<123Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(73, 123)

        with context('si la sección 0 < s <= 630 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-14VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 630):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-14VX'))

        with context('si la sección 630 < s <= 1200 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-14VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(631, 1200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-14VY'))

        with context('si la sección 1200 < s '):
            with context('si la linea es Subterranea circuito simpe'):
                with it('must be TI-14VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 1201
                        expect(self.l.tipoinstalacion).to(equal('TI-14VZ'))

    with context('si la 72,5Kv < tensión =<123Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(73, 123)

        with context('si la sección 0 < s <= 630 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-15VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 630):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-15VX'))

        with context('si la sección 630 < s <= 1200 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-15VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(631, 1200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-15VY'))

        with context('si la sección  1200 < s '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-15VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 1201
                        expect(self.l.tipoinstalacion).to(equal('TI-15VZ'))

    with context('si la 72,5Kv < tensión =<123Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(73, 123)

        with context('si la sección 0 < s <= 630 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-15AVX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 630):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-15AVX'))

        with context('si la sección 0 < s <= 630 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-15AVY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(631, 1200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-15AVY'))

        with context('si la sección  s <= 630 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-15AVZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 1201
                        expect(self.l.tipoinstalacion).to(equal('TI-15AVZ'))

    with context('si la  52Kv < tensión =<72,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(73, 123) + [72.5]

        with context('si la sección 0 < s <= 300 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-16UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-16UX'))

        with context('si la sección 300 < s <= 500 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-16UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(301, 500):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-16UY'))

        with context('si la sección  500 < s '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-16UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 1201
                        expect(self.l.tipoinstalacion).to(equal('TI-16UZ'))

    with context('si la  52Kv < tensión =<72,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(73, 123) + [72.5]

        with context('si la sección 0 < s <= 300 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-17UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-17UY'))

        with context('si la sección 300 < s <= 500 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-17UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(301, 500):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-17UX'))

        with context('si la sección  500 < s '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-17UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 1201
                        expect(self.l.tipoinstalacion).to(equal('TI-17UZ'))

    with context('si la  52Kv < tensión =<72,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(73, 123) + [72.5]

        with context('si la sección 0 < s <= 300 '):
            with context('si la linea es Subterranea circuito tripe'):
                with it('must be TI-17AUX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-17AUX'))

        with context('si la sección 300 < s <= 500 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-17AUY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(301, 500):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-17AUY'))

        with context('si la sección  500 < s '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-17AUZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 1201
                        expect(self.l.tipoinstalacion).to(equal('TI-17AUZ'))

    with context('si la   36Kv < tensión =<52Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(37, 52)

        with context('si la sección 0 < s <= 300 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-16VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-16VX'))

        with context('si la sección 300 < s <= 500 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-16VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(301, 500):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-16VY'))

        with context('si la sección  500 < s '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-16VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 501
                        expect(self.l.tipoinstalacion).to(equal('TI-16VZ'))

    with context('si la   36Kv < tensión =<52Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(37, 52)

        with context('si la sección 0 < s <= 300 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-17VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-17VY'))

        with context('si la sección 300 < s <= 500 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-17VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(301, 500):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion, 'TI-17VX')

        with context('si la sección  500 < s '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-17VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 501
                        expect(self.l.tipoinstalacion).to(equal('TI-17VZ'))

    with context('si la   36Kv < tensión =<52Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(37, 52)

        with context('si la sección 0 < s <= 300 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-17AVX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-17AVX'))

        with context('si la sección 300 < s <= 500 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-17AVY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(301, 500):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-17AVY'))

        with context('si la sección  500 < s '):
            with context('si la linea es Subterranea circuito tripl'):
                with it('must be TI-17AVZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 501
                        expect(self.l.tipoinstalacion).to(equal('TI-17AVZ'))

    with context('si la   24Kv < tensión =<36Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(24, 36)

        with context('si la sección 0 < s <= 200 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18UX'))

        with context('si la sección 200 < s <= 300 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18UY'))

        with context('si la sección  300 < s '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-18UZ'))

    with context('si la   24Kv < tensión =<36Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(24, 36)

        with context('si la sección 0 < s <= 200 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-19UX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19UX'))

        with context('si la sección 200 < s <= 300 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-19UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19UY'))

        with context('si la sección  300 < s '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-19UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-19UZ'))

    with context('si la   24Kv < tensión =<36Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(24, 36)

        with context('si la sección 0 < s <= 200 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-19AUX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19AUX'))

        with context('si la sección 200 < s <= 300 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-19AUY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19AUY'))

        with context('si la sección  300 < s '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-19AUZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-19AUZ'))

    with context('si la  17,5Kv < tensión =<24Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(18, 24)

        with context('si la sección 0 < s <= 200 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18VX'))

        with context('si la sección 200 < s <= 300 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18VY'))

        with context('si la sección  300 < s '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-18Z'))

    with context('si la  17,5Kv < tensión =<24Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(18, 24)

        with context('si la sección 0 < s <= 200 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-19VX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19VX'))

        with context('si la sección 200 < s <= 300 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-19VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19VY'))

        with context('si la sección  300 < s '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-19VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-19VZ'))

    with context('si la  17,5Kv < tensión =<24Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(18, 24)

        with context('si la sección 0 < s <= 200 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-19AVX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19AVX'))

        with context('si la sección 200 < s <= 300 '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-19AVY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19AVY'))

        with context('si la sección  300 < s '):
            with context('si la linea es Subterranea circuito triple'):
                with it('must be TI-19AVZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-19AVZ'))

    with context('si la  12Kv < tensión =<17,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(12, 17) + [17.5]

        with context('si la sección 0 < s <= 200 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18WX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18WX'))

        with context('si la sección 200 < s <= 300 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18WY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18WY'))

        with context('si la sección  300 < s '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18WZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-18WZ'))

    with context('si la  12Kv < tensión =<17,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(12, 17) + [17.5]

        with context('si la sección 0 < s <= 200 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-19WX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19WX'))

        with context('si la sección 200 < s <= 300 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-19WY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19WY'))

        with context('si la sección  300 < s '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-19WZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-19WZ'))

    with context('si la  12Kv < tensión =<17,5Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(12, 17) + [17.5]

        with context('si la sección 0 < s <= 200 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-19AWX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19AWX'))

        with context('si la sección 200 < s <= 300 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-19AWY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19AWY'))

        with context('si la sección  300 < s '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-19AWZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-19AWZ'))

    with context('si la 1Kv < tensión =<12Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = range(2, 12)

        with context('si la sección 0 < s <= 100 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18BX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18BX'))

        with context('si la sección 100 < s <= 200 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18BY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18BY'))

        with context('si la sección  200 < s '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-18BZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-18BZ'))

    with context('si la 1Kv < tensión =<12Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = range(2, 12)

        with context('si la sección 0 < s <= 100 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-18BX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18BX'))

        with context('si la sección 100 < s <= 200 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-18BY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-18BY'))

        with context('si la sección  200 < s '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-18BZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-18BZ'))

    with context('si la 1Kv < tensión =<12Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(2, 12)

        with context('si la sección 0 < s <= 100 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-19ABX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 200):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19ABX'))

        with context('si la sección 100 < s <= 200 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-19ABY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(201, 300):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-19ABY'))

        with context('si la sección  200 < s '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-19ABZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 301
                        expect(self.l.tipoinstalacion).to(equal('TI-19ABZ'))

    with context('si la tensión =<1Kv '):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 1
            self.l.num_conductores = 1
            self.tensiones = [0]

        with context('si la sección 0 < s <= 150 '):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-20X'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 150):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-20X'))

        with context('si la sección  s > 150'):
            with context('si la linea es Subterranea circuito simple'):
                with it('must be TI-20Y'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 151
                        expect(self.l.tipoinstalacion).to(equal('TI-20Y'))

    with context('si la tensión =<1Kv '):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'S'
            self.l.num_circuitos = 2
            self.l.num_conductores = 1
            self.tensiones = [0]

        with context('si la sección 0 < s <= 150 '):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-21X'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 150):
                            self.l.seccionn = s
                            expect(self.l.tipoinstalacion).to(equal('TI-20X'))

        with context('si la sección  s > 150'):
            with context('si la linea es Subterranea circuito doble'):
                with it('must be TI-21Y'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccionn = 151
                        expect(self.l.tipoinstalacion).to(equal('TI-20Y'))