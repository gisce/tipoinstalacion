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
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-1UX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea simple circuito-Simplex'):
                with it('must be TI-1UY'):
                    for s in range(181, 300):
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-1UY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea simple circuito-Simplex'):
                with it('must be TI-1UZ'):
                    self.l.seccio = 301
                    expect(self.l.tipoinstalacion, 'TI-1UZ')

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
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-2UX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea simple circuito-Duplex'):
                with it('must be TI-2UY'):
                    for s in range(181, 300):
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-2UY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea simple circuito-Duplex'):
                with it('must be TI-2UZ'):
                    self.l.seccio = 301
                    expect(self.l.tipoinstalacion, 'TI-2UZ')

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
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-3UX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea doble circuito-Simplex'):
                with it('must be TI-3UY'):
                    for s in range(181, 300):
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-3UY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea doble circuito-Simplex'):
                with it('must be TI-3UZ'):
                    self.l.seccio = 301
                    expect(self.l.tipoinstalacion, 'TI-3UZ')

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
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-4UX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea doble circuito-Duplex'):
                with it('must be TI-4UY'):
                    for s in range(181, 300):
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-4UY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea doble circuito-Duplex'):
                with it('must be TI-4UZ'):
                    self.l.seccio = 301
                    expect(self.l.tipoinstalacion, 'TI-4UZ')

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
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-3AUX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea doble circuito-Duplex'):
                with it('must be TI-3AUY'):
                    for s in range(181, 300):
                        self.l.seccio = s
                        expect(self.l.tipoinstalacion, 'TI-3AUY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea doble circuito-Duplex'):
                with it('must be TI-3AUZ'):
                    self.l.seccio = 301
                    expect(self.l.tipoinstalacion, 'TI-3AUZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-1VX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-1VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-1VY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-1VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-1VZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-2VX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-2VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-2VY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-2VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-2VZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-3VX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-3VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-3VY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-3VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-3VZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-4VX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-4VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-4VY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Dupluex'):
                with it('must be TI-4VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-4VZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-3AVX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-3AVY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-3AVY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-3AVZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-3AVZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-5UX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-5UY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-5UZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-7UX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-7UY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-7UZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-8UX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-8UY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-8UZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-7AUY')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-8UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-7AUX')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-8UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-7AUZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-5VX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-5VY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Simplex'):
                with it('must be TI-5VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-5VZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-6VX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito simple-Duplex'):
                with it('must be TI-6VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-6VY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito simple-Duplex'):
                with it('must be TI-6VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-6VZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-7VX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-7VY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Simplex'):
                with it('must be TI-7VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-7VZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-8VX')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-8VY')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito doble-Duplex'):
                with it('must be TI-8VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-8VZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-7AVY')

        with context('si la sección 180 < s <= 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-7AVX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(180, 299):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-7AVX')

        with context('si la sección  s < 300 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-7AVZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 301
                        expect(self.l.tipoinstalacion, 'TI-7AVZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-9UX')

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9UY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-9UY')

        with context('si la sección  s < 110 '):
            with context('si la linea es Aerea circuito simple'):
                with it('must be TI-9UZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 111
                        expect(self.l.tipoinstalacion, 'TI-9UZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-10UX')

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-10UY')

        with context('si la sección  s < 110 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 111
                        expect(self.l.tipoinstalacion, 'TI-10UZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-10AUX')

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-10AUY')

        with context('si la sección  s < 110 '):
            with context('si la linea es Aerea circuito triple'):
                with it('must be TI-10AUZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 111
                        expect(self.l.tipoinstalacion, 'TI-10AUZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-9VX')

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-9VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-9VY')

        with context('si la sección  s < 110 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-9VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 111
                        expect(self.l.tipoinstalacion, 'TI-9VZ')

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
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-10VX')

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-10VY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-10VY')

        with context('si la sección  s < 110 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-10VZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 111
                        expect(self.l.tipoinstalacion, 'TI-10VZ')

    with context('si la  17,5Kv < tensión <= 24Kv'):
        with before.each:
            self.l = Linea()
            self.l.despliegue = 'AP'
            self.l.num_circuitos = 3
            self.l.num_conductores = 1
            self.tensiones = range(18, 24)

        with context('si la sección 0 < s <= 56 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-10AVX'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(1, 56):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-10AVX')

        with context('si la sección 56 < s <= 110 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-10AVY'):
                    for t in self.tensiones:
                        self.l.tension = t
                        for s in range(57, 110):
                            self.l.seccion = s
                            expect(self.l.tipoinstalacion, 'TI-10AVY')

        with context('si la sección  s < 110 '):
            with context('si la linea es Aerea circuito triple-Simplex'):
                with it('must be TI-10AVZ'):
                    for t in self.tensiones:
                        self.l.tension = t
                        self.l.seccion = 111
                        expect(self.l.tipoinstalacion, 'TI-10AVZ')

