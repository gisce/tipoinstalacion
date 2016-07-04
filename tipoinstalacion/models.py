
# coding=utf-8
"""
Modelos de datos básicos para calcular los Tipos de Instalacion.
"""


class Linea(object):
    """
    Objeto que reperesenta una linea

    Podemos obtener el Tipo de Instalcion creando un objeto linea, assignando
    los

    linea = Linea()
    # TODO: Explicar dev

    """

    def __init__(self):
        self.tension = None
        """Tension en kV
        """

        self.num_circuitos = None
        """Número de circuitos
        """

        self.num_conductores = None
        """Número de conductores
        """

        self.seccion = None
        """Sección del cable en mm²
        """

        self.despliegue = None
        """Despliegue de la linea:

            - Tensada sobre postes: ``AP``
            - Apoyada sobre fachada: ``AF``
            - Subterránea: `S`
        """

    @property
    def tipoinstalacion(self):
        """
        Obtiene el tipo de instalacion de la linea

        :return:
        """

        if self.despliegue[0] == 'A':
            u = self.tension
            s = self.seccion
            if u > 123:
                if self.num_circuitos == 1:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-1UX'
                        elif 180 < s <= 300:
                            return 'TI-1UY'
                        elif 300 < s:
                            return 'TI-1UZ'
                    elif self.num_conductores == 2:
                        if 0 < s <= 180:
                            return 'TI-2UX'
                        elif 180 < s <= 300:
                            return 'TI-2UY'
                        elif 300 < s:
                            return 'TI-2UZ'
                elif self.num_circuitos == 2:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-3UX'
                        elif 180 < s <= 300:
                            return 'TI-3UY'
                        elif 300 < s:
                            return 'TI-3UZ'
                    elif self.num_conductores == 2:
                        if 0 < s <= 180:
                            return 'TI-4UX'
                        elif 180 < s <= 300:
                            return 'TI-4UY'
                        elif 300 < s:
                            return 'TI-4UZ'
                elif self.num_circuitos == 3:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-3AUX'
                        elif 180 < s <= 300:
                            return 'TI-3AUY'
                        elif 300 < s:
                            return 'TI-3AUZ'
            elif 123 >= u > 72.5:
                if self.num_circuitos == 1:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-1VX'
                        elif 180 < s <= 300:
                            return 'TI-1VY'
                        elif 300 < s:
                            return 'TI-1VZ'
                    elif self.num_conductores == 2:
                        if 0 < s <= 180:
                            return 'TI-2VX'
                        elif 180 < s <= 300:
                            return 'TI-2VY'
                        elif 300 < s:
                            return 'TI-2VZ'
                elif self.num_circuitos == 2:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-3VX'
                        elif 180 < s <= 300:
                            return 'TI-3VY'
                        elif 300 < s:
                            return 'TI-3VZ'
                    elif self.num_conductores == 2:
                        if 0 < s <= 180:
                            return 'TI-4VX'
                        elif 180 < s <= 300:
                            return 'TI-4VY'
                        elif 300 < s:
                            return 'TI-4VZ'
                elif self.num_circuitos == 3:
                    if self.num_conductores ==1:
                        if 0 < s <= 180:
                            return 'TI-3AVX'
                        elif 180 < s <= 300:
                            return 'TI-3AVY'
                        elif 300 < s:
                            return 'TI-3AVZ'
            elif 72.5 >= u > 52:
                if self.num_circuitos == 1:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-5UX'
                        elif 180 < s <= 300:
                            return 'TI-5UY'
                        elif 300 < s:
                            return 'TI-5UZ'
                    elif self.num_conductores == 2:
                        if 0 < s <= 180:
                            return 'TI-6UX'
                        elif 180 < s <= 300:
                            return 'TI-6UY'
                        elif 300 < s:
                            return 'TI-6UZ'
                elif self.num_circuitos == 2:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-7UX'
                        elif 180 < s <= 300:
                            return 'TI-7UY'
                        elif 300 < s:
                            return 'TI-7UZ'
                    elif self.num_conductores == 2:
                        if 0 < s <= 180:
                            return 'TI-8UX'
                        elif 180 < s <= 300:
                            return 'TI-8UY'
                        elif 300 < s:
                            return 'TI-8UZ'
                elif self.num_circuitos == 3:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-7AUY'
                        elif 180 < s <= 300:
                            return 'TI-7AUX'
                        elif 300 < s:
                            return 'TI-7AUZ'
            elif 52 >= u > 36:
                if self.num_circuitos == 1:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-5VX'
                        elif 180 < s <= 300:
                            return 'TI-5VY'
                        elif 300 < s:
                            return 'TI-5VZ'
                    elif self.num_conductores == 2:
                        if 0 < s <= 180:
                            return 'TI-6VX'
                        elif 180 < s <= 300:
                            return 'TI-6VY'
                        elif 300 < s:
                            return 'TI-6VZ'
                elif self.num_circuitos == 2:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-7VX'
                        elif 180 < s <= 300:
                            return 'TI-7VY'
                        elif 300 < s:
                            return 'TI-7VZ'
                    elif self.num_conductores == 2:
                        if 0 < s <= 180:
                            return 'TI-8VX'
                        elif 180 < s <= 300:
                            return 'TI-8VY'
                        elif 300 < s:
                            return 'TI-8VZ'
                elif self.num_circuitos == 3:
                    if self.num_conductores == 1:
                        if 0 < s <= 180:
                            return 'TI-7AVY'
                        elif 180 < s <= 300:
                            return 'TI-7AVX'
                        elif 300 < s:
                            return 'TI-7AVZ'
            elif 36 >= u > 24:
                if self.num_circuitos == 1:
                    if 0 < s <= 56:
                        return 'TI-9UX'
                    elif 56 < s <= 110:
                        return 'TI-9UY'
                    elif 110 < s:
                        return 'TI-9UZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 56:
                        return 'TI-10UX'
                    elif 56 < s <= 110:
                        return 'TI-10UY'
                    elif 110 < s:
                        return 'TI-10UZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 56:
                        return 'TI-10AUX'
                    elif 56 < s <= 110:
                        return 'TI-10AUY'
                    elif 110 < s:
                        return 'TI-10AUZ'
            elif 24 >= u > 17.5:
                if self.num_circuitos == 1:
                    if 0 < s <= 56:
                        return 'TI-9VX'
                    elif 56 < s <= 110:
                        return 'TI-9VY'
                    elif 110 < s:
                        return 'TI-9VZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 56:
                        return 'TI-10VX'
                    elif 56 < s <= 110:
                        return 'TI-10VY'
                    elif 110 < s:
                        return 'TI-10VZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 56:
                        return 'TI-10AVX'
                    elif 56 < s <= 110:
                        return 'TI-10AVY'
                    elif 110 < s:
                        return 'TI-10AVZ'
            elif 17.5 >= u > 12:
                if self.num_circuitos == 1:
                    if 0 < s <= 56:
                        return 'TI-9WX'
                    elif 56 < s <= 110:
                        return 'TI-9WY'
                    elif 110 < s:
                        return 'TI-9WZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 56:
                        return 'TI-10WX'
                    elif 56 < s <= 110:
                        return 'TI-10WY'
                    elif 110 < s:
                        return 'TI-10WZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 56:
                        return 'TI-10AWX'
                    elif 56 < s <= 110:
                        return 'TI-10AWY'
                    elif 110 < s:
                        return 'TI-10AWZ'
            elif 12 >= u > 1:
                if self.num_circuitos == 1:
                    if 0 < s <= 56:
                        return 'TI-9BX'
                    elif 56 < s <= 110:
                        return 'TI-9BY'
                    elif 110 < s:
                        return 'TI-9BZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 56:
                        return 'TI-10BX'
                    elif 56 < s <= 110:
                        return 'TI-10BY'
                    elif 110 < s:
                        return 'TI-10BZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 56:
                        return 'TI-10ABX'
                    elif 56 < s <= 110:
                        return 'TI-10ABY'
                    elif 110 < s:
                        return 'TI-10ABZ'
            elif 1 > u:

                if self.despliegue == 'AP':
                    if self.num_circuitos == 1:
                        if s < 75:
                            return 'TI-11X'
                        elif s >= 75:
                            return 'TI-11Y'
                    elif self.num_circuitos == 2:
                        if s < 75:
                            return 'TI-13X'
                        elif s >= 75:
                            return 'TI-13Y'
                if self.despliegue == 'AF':
                    if self.num_circuitos == 1:
                        if s < 75:
                            return 'TI-12X'
                        elif s >= 75:
                            return 'TI-12Y'
            else:
                return None

        elif self.despliegue[0] == 'S':
            u = self.tension
            s = self.seccion
            if u > 123:
                if self.num_circuitos == 1:
                    if 0 < s <= 630:
                        return 'TI-14UX'
                    elif 630 < s <= 1200:
                        return 'TI-14UY'
                    elif 1200 < s:
                        return 'TI-14UZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 630:
                        return 'TI-15UX'
                    elif 630 < s <= 1200:
                        return 'TI-15UY'
                    elif 1200 < s:
                        return 'TI-15UZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 630:
                        return 'TI-15AUX'
                    elif 630 < s <= 1200:
                        return 'TI-15AUY'
                    elif 1200 < s:
                        return 'TI-15AUZ'
            elif 123 >= u > 72.5:
                if self.num_circuitos == 1:
                    if 0 < s <= 630:
                        return 'TI-14VX'
                    elif 630 < s <= 1200:
                        return 'TI-14VY'
                    elif 1200 < s:
                        return 'TI-14VZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 630:
                        return 'TI-15VX'
                    elif 630 < s <= 1200:
                        return 'TI-15VY'
                    elif 1200 < s:
                        return 'TI-15VZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 630:
                        return 'TI-15AVX'
                    elif 630 < s <= 1200:
                        return 'TI-15AVY'
                    elif 1200 < s:
                        return 'TI-15AVZ'
            elif 72.5 >= u > 52:
                if self.num_circuitos == 1:
                    if 0 < s <= 300:
                        return 'TI-16UX'
                    elif 300 < s <= 500:
                        return 'TI-16UY'
                    elif 500 < s:
                        return 'TI-16UZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 300:
                        return 'TI-17UY'
                    elif 300 < s <= 500:
                        return 'TI-17UX'
                    elif 500 < s:
                        return 'TI-17UZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 300:
                        return 'TI-17AUX'
                    elif 300 < s <= 500:
                        return 'TI-17AUY'
                    elif 500 < s:
                        return 'TI-17AUZ'
            elif 52 >= u > 36:
                if self.num_circuitos == 1:
                    if 0 < s <= 300:
                        return 'TI-16VX'
                    elif 300 < s <= 500:
                        return 'TI-16VY'
                    elif 500 < s:
                        return 'TI-16VZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 300:
                        return 'TI-17VY'
                    elif 300 < s <= 500:
                        return 'TI-17VX'
                    elif 500 < s:
                        return 'TI-17VZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 300:
                        return 'TI-17AVX'
                    elif 300 < s <= 500:
                        return 'TI-17AVY'
                    elif 500 < s:
                        return 'TI-17AVZ'
                pass
            elif 36 >= u > 24:
                if self.num_circuitos == 1:
                    if 0 < s <= 200:
                        return 'TI-18UX'
                    elif 200 < s <= 300:
                        return 'TI-18UY'
                    elif 300 < s:
                        return 'TI-18UZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 200:
                        return 'TI-19UX'
                    elif 200 < s <= 300:
                        return 'TI-19UY'
                    elif 300 < s:
                        return 'TI-19UZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 200:
                        return 'TI-19AUX'
                    elif 200 < s <= 300:
                        return 'TI-19AUY'
                    elif 300 < s:
                        return 'TI-19AUZ'
                pass
            elif 24 >= u > 17.5:
                if self.num_circuitos == 1:
                    if 0 < s <= 200:
                        return 'TI-18VX'
                    elif 200 < s <= 300:
                        return 'TI-18VY'
                    elif 300 < s:
                        return 'TI-18VZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 200:
                        return 'TI-19VX'
                    elif 200 < s <= 300:
                        return 'TI-19VY'
                    elif 300 < s:
                        return 'TI-19VZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 200:
                        return 'TI-19AVX'
                    elif 200 < s <= 300:
                        return 'TI-19AVY'
                    elif 300 < s:
                        return 'TI-19AVZ'
                pass
            elif 17.5 >= u > 12:
                if self.num_circuitos == 1:
                    if 0 < s <= 200:
                        return 'TI-18WX'
                    elif 200 < s <= 300:
                        return 'TI-18WY'
                    elif 300 < s:
                        return 'TI-18WZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 200:
                        return 'TI-19WX'
                    elif 200 < s <= 300:
                        return 'TI-19WY'
                    elif 300 < s:
                        return 'TI-19WZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 200:
                        return 'TI-19AWX'
                    elif 200 < s <= 300:
                        return 'TI-19AWY'
                    elif 300 < s:
                        return 'TI-19AWZ'
            elif 12 >= u >= 1:
                if self.num_circuitos == 1:
                    if 0 < s <= 100:
                        return 'TI-18BX'
                    elif 100 < s <= 200:
                        return 'TI-18BY'
                    elif 200 < s:
                        return 'TI-18BZ'
                elif self.num_circuitos == 2:
                    if 0 < s <= 100:
                        return 'TI-19BX'
                    elif 100 < s <= 200:
                        return 'TI-19BY'
                    elif 200 < s:
                        return 'TI-19BZ'
                elif self.num_circuitos == 3:
                    if 0 < s <= 100:
                        return 'TI-19ABX'
                    elif 100 < s <= 200:
                        return 'TI-19ABY'
                    elif 200 < s:
                        return 'TI-19ABZ'
            elif u < 1:
                if self.num_circuitos == 1:
                    if 0 < s < 150:
                        return 'TI-20X'
                    elif 150 <= s:
                        return 'TI-20Y'
                elif self.num_circuitos == 2:
                    if 0 < s < 150:
                        return 'TI-21X'
                    elif 150 <= s:
                        return 'TI-21Y'
            return None
        return None


class Posicion(object):
    """
    Objeto de representa una posicion
    """

    def __init__(self):
        super(Posicion, self).__init__()
        self.tension = None
        self.situacion = None
        """
        Ubicación de la posición:
          - Interior: ``I``
          - Intemperie: ``E``
          - Móvil: ``M``
        """
        self.tipo = None
        """
        Tipo de posición:
          - Blindada ``B``
          - Convencional ``C``
          - Hibrida ``H``
        """

    @property
    def tipoinstalacion(self):
        """
        Obtiene el tipo de instalacion de la linea

        :return:
        """
        if self.tipo == 'B':
            if self.tension > 123:
                if self.situacion == 'I':
                    return 'TI-88U'
                elif self.situacion == 'E':
                    return 'TI-89U'
                elif self.situacion == 'M':
                    return 'TI-90U'
            elif 123 >= self.tension > 72.5:
                if self.situacion == 'I':
                    return 'TI-88V'
                elif self.situacion == 'E':
                    return 'TI-89V'
                elif self.situacion == 'M':
                    return 'TI-90V'
            elif 72.5 >= self.tension > 52:
                if self.situacion == 'I':
                    return 'TI-95U'
                elif self.situacion == 'E':
                    return 'TI-96U'
                elif self.situacion == 'M':
                    return 'TI-97U'
            elif 52 >= self.tension > 36:
                if self.situacion == 'I':
                    return 'TI-95V'
                elif self.situacion == 'E':
                    return 'TI-96V'
                elif self.situacion == 'M':
                    return 'TI-97V'
            elif 36 >= self.tension > 24:
                if self.situacion == 'I':
                    return 'TI-102U'
                elif self.situacion == 'E':
                    return 'TI-103U'
                elif self.situacion == 'M':
                    return 'TI-104U'
            elif 24 >= self.tension > 17.5:
                if self.situacion == 'I':
                    return 'TI-102V'
                elif self.situacion == 'E':
                    return 'TI-103V'
                elif self.situacion == 'M':
                    return 'TI-104V'
            elif 17.5 >= self.tension > 12:
                if self.situacion == 'I':
                    return 'TI-102W'
                elif self.situacion == 'E':
                    return 'TI-103W'
                elif self.situacion == 'M':
                    return 'TI-104W'
            elif 12 >= self.tension >= 1:
                if self.situacion == 'I':
                    return 'TI-102B'
                elif self.situacion == 'E':
                    return 'TI-103B'
                elif self.situacion == 'M':
                    return 'TI-104B'
        elif self.tipo == 'C':
            if self.tension > 123:
                if self.situacion == 'I':
                    return 'TI-91U'
                elif self.situacion == 'E':
                    return 'TI-92U'
            elif 123 >= self.tension > 72.5:
                if self.situacion == 'I':
                    return 'TI-91V'
                elif self.situacion == 'E':
                    return 'TI-92V'
            elif 72.5 >= self.tension > 52:
                if self.situacion == 'I':
                    return 'TI-98U'
                elif self.situacion == 'E':
                    return 'TI-99U'
            elif 52 >= self.tension > 36:
                if self.situacion == 'I':
                    return 'TI-98V'
                elif self.situacion == 'E':
                    return 'TI-99V'
            elif 36 >= self.tension > 24:
                if self.situacion == 'I':
                    return 'TI-105U'
                elif self.situacion == 'E':
                    return 'TI-106U'
            elif 24 >= self.tension > 17.5:
                if self.situacion == 'I':
                    return 'TI-105V'
                elif self.situacion == 'E':
                    return 'TI-106V'
            elif 17.5 >= self.tension > 12:
                if self.situacion == 'I':
                    return 'TI-105W'
                elif self.situacion == 'E':
                    return 'TI-106W'
            elif 12>=self.tension>=1:
                if self.situacion == 'I':
                    return 'TI-105B'
                elif self.situacion == 'E':
                    return 'TI-106B'
        elif self.tipo == 'H':
            if self.tension >= 123:
                if self.situacion == 'I':
                    return 'TI-93U'
                elif self.situacion == 'E':
                    return 'TI-94U'
            elif 123 >= self.tension > 72.5:
                if self.situacion == 'I':
                    return 'TI-93V'
                elif self.situacion == 'E':
                    return 'TI-94V'
            elif 72.5 >= self.tension > 52:
                if self.situacion == 'I':
                    return 'TI-100U'
                elif self.situacion == 'E':
                    return 'TI-101U'
            elif 52 >= self.tension > 36:
                if self.situacion == 'I':
                    return 'TI-100V'
                elif self.situacion == 'E':
                    return 'TI-101V'
            elif 36 >= self.tension > 24:
                if self.situacion == 'I':
                    return 'TI-107U'
                elif self.situacion == 'E':
                    return 'TI-108U'
            elif 24 >= self.tension > 17.5:
                if self.situacion == 'I':
                    return 'TI-107V'
                elif self.situacion == 'E':
                    return 'TI-108V'
            elif 17.5 >= self.tension > 12:
                if self.situacion == 'I':
                    return 'TI-107W'
                elif self.situacion == 'E':
                    return 'TI-108W'
            elif 12 >= self.tension >= 1:
                if self.situacion == 'I':
                    return 'TI-107B'
                elif self.situacion == 'E':
                    return 'TI-108B'
        return None


class Transformador(object):
    """
    Objeto que representa un transformador.
    """
    def __init__(self):
        self.tension_p = None
        """Tension primaria en kV
        """
        self.tension_s = None
        """Tension primaria en kV
        """

    @property
    def tipoinstalacion(self):
        """
        Obtiene el tipo de instalacion de la linea

        :return:
        """
        if self.tension_p == 420:
            if 245 >= self.tension_s > 123:
                return 'TI-158U'
            elif 123 >= self.tension_s > 72.5:
                return 'TI-158V'
            elif 72.5 >= self.tension_s > 36:
                return 'TI-158W'
        elif self.tension_p == 245:
            if 245 >= self.tension_s > 123:
                return 'TI-159U'
            elif 123 >= self.tension_s > 72.5:
                return 'TI-159V'
            elif 72.5 >= self.tension_s > 36:
                return 'TI-160U'
            elif 36 >= self.tension_s > 24:
                return 'TI-161U'
            elif 24 >= self.tension_s > 12:
                return 'TI-161W'
            elif 12 >= self.tension_s >= 1:
                return 'TI-161B'
        elif 145 >= self.tension_p > 72.5:
            if 72.5 >= self.tension_s > 52:
                return 'TI-162U'
            elif 52 >= self.tension_s > 36:
                return 'TI-162V'
            elif 36 >= self.tension_s > 24:
                return 'TI-163U'
            elif 24 >= self.tension_s > 17.5:
                return 'TI-163V'
            elif 17.5 >= self.tension_s > 12:
                return 'TI-163W'
            elif 12 >= self.tension_s >= 1:
                return 'TI-163B'
        elif 72.5 >= self.tension_p > 36:
            if 36 >= self.tension_s > 24:
                return 'TI-164U'
            elif 24 >= self.tension_s > 17.5:
                return 'TI-164V'
            elif 17.5 >= self.tension_s > 12:
                return 'TI-164W'
            elif 12 >= self.tension_s >= 1:
                return 'TI-164B'
        elif 36 > self.tension_p >= 1:
            if 30 >= self.tension_s > 24:
                return 'TI-165U'
            elif 24 >= self.tension_s > 17.5:
                return 'TI-165V'
            elif 175.5 >= self.tension_s > 12:
                return 'TI-165W'
            elif 12 >= self.tension_s >= 1:
                return 'TI-165B'
        return None


class Condensador(object):
    """
    Objeto que representa un condensador.
    """
    def __init__(self):
        self.tension = None
        """Tension
        """

    @property
    def tipoinstalacion(self):
        """
        Obtiene el tipo de instalacion de la linea

        :return:
        """
        if 132 >= self.tension > 66:
            return 'TI-169'
        elif 66 >= self.tension > 36:
            return 'TI-170'
        elif 36 >= self.tension > 1:
            return 'TI-171'

class Reactancia(object):
    """
    Objeto que reperesenta una reactancia

    Podemos obtener el Tipo de Instalcion creando un objeto reacancia, assignando
    los

    linea = Reactancai()
    # TODO: Explicar dev

    """

    def __init__(self):
        self.tension = None
        """Tension en kV
        """

    @property
    def tipoinstalacion(self):
        """
        Obtiene el tipo de instalacion de la reactancia

        :return:
        """
        if 145 >= self.tension > 72.5:
            return 'TI-166'
        elif 72.5 >= self.tension > 36:
            return 'TI-167'
        elif 36 >= self.tension > 1:
            return 'TI-168'
        return None

class CT(object):
    """
    Objeto que representa un centro transformador.
    """
    def __init__(self):
        self.tension = None
        """Tension primaria en kV
        """
        self.potencia = None
        """ Potencia del CT
        """
        self.numero_maquinas = None
        """ Numero de maquinas
        """

        self.situacion = None
        """ Situacion
        C - Caseta
        L - Local
        I - Intemperie
        S - Subeterraneo
        """

    @property
    def tipoinstalacion(self):
        """
        Obtiene el tipo de instalacion de la linea

        :return:
        """

        if self.situacion == 'C':
            if 12 >= self.tension >= 1:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-22U'
                    elif self.potencia == 25:
                        return 'TI-23U'
                    elif self.potencia == 50:
                        return 'TI-24U'
                    elif self.potencia == 100:
                        return 'TI-25U'
                    elif self.potencia == 160:
                        return 'TI-26U'
                    elif self.potencia == 250:
                        return 'TI-27U'
                    elif self.potencia == 400:
                        return 'TI-28U'
                    elif self.potencia == 630:
                        return 'TI-29U'
                    elif self.potencia == 1000:
                        return 'TI-30U'
                    elif self.potencia == 1250:
                        return 'TI-31U'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-32U'
                    elif self.potencia == 25:
                        return 'TI-33U'
                    elif self.potencia == 50:
                        return 'TI-34U'
                    elif self.potencia == 100:
                        return 'TI-35U'
                    elif self.potencia == 160:
                        return 'TI-36U'
                    elif self.potencia == 250:
                        return 'TI-37U'
                    elif self.potencia == 400:
                        return 'TI-38U'
                    elif self.potencia == 630:
                        return 'TI-39U'
                    elif self.potencia == 1000:
                        return 'TI-40U'
                    elif self.potencia == 1250:
                        return 'TI-41U'

            elif 17.5 >= self.tension > 12:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-22V'
                    elif self.potencia == 25:
                        return 'TI-23V'
                    elif self.potencia == 50:
                        return 'TI-24V'
                    elif self.potencia == 100:
                        return 'TI-25V'
                    elif self.potencia == 160:
                        return 'TI-26V'
                    elif self.potencia == 250:
                        return 'TI-27V'
                    elif self.potencia == 400:
                        return 'TI-28V'
                    elif self.potencia == 630:
                        return 'TI-29V'
                    elif self.potencia == 1000:
                        return 'TI-30V'
                    elif self.potencia == 1250:
                        return 'TI-31V'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-32V'
                    elif self.potencia == 25:
                        return 'TI-33V'
                    elif self.potencia == 50:
                        return 'TI-34V'
                    elif self.potencia == 100:
                        return 'TI-35V'
                    elif self.potencia == 160:
                        return 'TI-36V'
                    elif self.potencia == 250:
                        return 'TI-37V'
                    elif self.potencia == 400:
                        return 'TI-38V'
                    elif self.potencia == 630:
                        return 'TI-39V'
                    elif self.potencia == 1000:
                        return 'TI-40V'
                    elif self.potencia == 1250:
                        return 'TI-41V'
            elif 24 >= self.tension > 17.5:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-22W'
                    elif self.potencia == 25:
                        return 'TI-23W'
                    elif self.potencia == 50:
                        return 'TI-24W'
                    elif self.potencia == 100:
                        return 'TI-25W'
                    elif self.potencia == 160:
                        return 'TI-26W'
                    elif self.potencia == 250:
                        return 'TI-27W'
                    elif self.potencia == 400:
                        return 'TI-28W'
                    elif self.potencia == 630:
                        return 'TI-29W'
                    elif self.potencia == 1000:
                        return 'TI-30W'
                    elif self.potencia == 1250:
                        return 'TI-31W'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-32W'
                    elif self.potencia == 25:
                        return 'TI-33W'
                    elif self.potencia == 50:
                        return 'TI-34W'
                    elif self.potencia == 100:
                        return 'TI-35W'
                    elif self.potencia == 160:
                        return 'TI-36W'
                    elif self.potencia == 250:
                        return 'TI-37W'
                    elif self.potencia == 400:
                        return 'TI-38W'
                    elif self.potencia == 630:
                        return 'TI-39W'
                    elif self.potencia == 1000:
                        return 'TI-40W'
                    elif self.potencia == 1250:
                        return 'TI-41W'
            elif 36 >= self.tension > 24:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-22B'
                    elif self.potencia == 25:
                        return 'TI-23B'
                    elif self.potencia == 50:
                        return 'TI-24B'
                    elif self.potencia == 100:
                        return 'TI-25B'
                    elif self.potencia == 160:
                        return 'TI-26B'
                    elif self.potencia == 250:
                        return 'TI-27B'
                    elif self.potencia == 400:
                        return 'TI-28B'
                    elif self.potencia == 630:
                        return 'TI-29B'
                    elif self.potencia == 1000:
                        return 'TI-30B'
                    elif self.potencia == 1250:
                        return 'TI-31B'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-32B'
                    elif self.potencia == 25:
                        return 'TI-33B'
                    elif self.potencia == 50:
                        return 'TI-34B'
                    elif self.potencia == 100:
                        return 'TI-35B'
                    elif self.potencia == 160:
                        return 'TI-36B'
                    elif self.potencia == 250:
                        return 'TI-37B'
                    elif self.potencia == 400:
                        return 'TI-38B'
                    elif self.potencia == 630:
                        return 'TI-39B'
                    elif self.potencia == 1000:
                        return 'TI-40B'
                    elif self.potencia == 1250:
                        return 'TI-41B'
            elif 52 >= self.tension > 36:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-22C'
                    elif self.potencia == 25:
                        return 'TI-23C'
                    elif self.potencia == 50:
                        return 'TI-24C'
                    elif self.potencia == 100:
                        return 'TI-25C'
                    elif self.potencia == 160:
                        return 'TI-26C'
                    elif self.potencia == 250:
                        return 'TI-27C'
                    elif self.potencia == 400:
                        return 'TI-28C'
                    elif self.potencia == 630:
                        return 'TI-29C'
                    elif self.potencia == 1000:
                        return 'TI-30C'
                    elif self.potencia == 1250:
                        return 'TI-31C'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-32C'
                    elif self.potencia == 25:
                        return 'TI-33C'
                    elif self.potencia == 50:
                        return 'TI-34C'
                    elif self.potencia == 100:
                        return 'TI-35C'
                    elif self.potencia == 160:
                        return 'TI-36C'
                    elif self.potencia == 250:
                        return 'TI-37C'
                    elif self.potencia == 400:
                        return 'TI-38C'
                    elif self.potencia == 630:
                        return 'TI-39C'
                    elif self.potencia == 1000:
                        return 'TI-40C'
                    elif self.potencia == 1250:
                        return 'TI-41C'
            elif 72.5 >= self.tension > 52:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-22D'
                    elif self.potencia == 25:
                        return 'TI-23D'
                    elif self.potencia == 50:
                        return 'TI-24D'
                    elif self.potencia == 100:
                        return 'TI-25D'
                    elif self.potencia == 160:
                        return 'TI-26D'
                    elif self.potencia == 250:
                        return 'TI-27D'
                    elif self.potencia == 400:
                        return 'TI-28D'
                    elif self.potencia == 630:
                        return 'TI-29D'
                    elif self.potencia == 1000:
                        return 'TI-30D'
                    elif self.potencia == 1250:
                        return 'TI-31D'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-32D'
                    elif self.potencia == 25:
                        return 'TI-33D'
                    elif self.potencia == 50:
                        return 'TI-34D'
                    elif self.potencia == 100:
                        return 'TI-35D'
                    elif self.potencia == 160:
                        return 'TI-36D'
                    elif self.potencia == 250:
                        return 'TI-37D'
                    elif self.potencia == 400:
                        return 'TI-38D'
                    elif self.potencia == 630:
                        return 'TI-39D'
                    elif self.potencia == 1000:
                        return 'TI-40D'
                    elif self.potencia == 1250:
                        return 'TI-41D'

        elif self.situacion == 'L':
            if 12 >= self.tension >= 1:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-42U'
                    elif self.potencia == 25:
                        return 'TI-43U'
                    elif self.potencia == 50:
                        return 'TI-44U'
                    elif self.potencia == 100:
                        return 'TI-45U'
                    elif self.potencia == 160:
                        return 'TI-46U'
                    elif self.potencia == 250:
                        return 'TI-47U'
                    elif self.potencia == 400:
                        return 'TI-48U'
                    elif self.potencia == 630:
                        return 'TI-49U'
                    elif self.potencia == 1000:
                        return 'TI-50U'
                    elif self.potencia == 1250:
                        return 'TI-51U'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-52U'
                    elif self.potencia == 25:
                        return 'TI-53U'
                    elif self.potencia == 50:
                        return 'TI-54U'
                    elif self.potencia == 100:
                        return 'TI-55U'
                    elif self.potencia == 160:
                        return 'TI-56U'
                    elif self.potencia == 250:
                        return 'TI-57U'
                    elif self.potencia == 400:
                        return 'TI-58U'
                    elif self.potencia == 630:
                        return 'TI-59U'
                    elif self.potencia == 1000:
                        return 'TI-60U'
                    elif self.potencia == 1250:
                        return 'TI-61U'
            elif 17.5 >= self.tension > 12:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-42V'
                    elif self.potencia == 25:
                        return 'TI-43V'
                    elif self.potencia == 50:
                        return 'TI-44V'
                    elif self.potencia == 100:
                        return 'TI-45V'
                    elif self.potencia == 160:
                        return 'TI-46V'
                    elif self.potencia == 250:
                        return 'TI-47V'
                    elif self.potencia == 400:
                        return 'TI-48V'
                    elif self.potencia == 630:
                        return 'TI-49V'
                    elif self.potencia == 1000:
                        return 'TI-50V'
                    elif self.potencia == 1250:
                        return 'TI-51V'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-52V'
                    elif self.potencia == 25:
                        return 'TI-53V'
                    elif self.potencia == 50:
                        return 'TI-54V'
                    elif self.potencia == 100:
                        return 'TI-55V'
                    elif self.potencia == 160:
                        return 'TI-56V'
                    elif self.potencia == 250:
                        return 'TI-57V'
                    elif self.potencia == 400:
                        return 'TI-58V'
                    elif self.potencia == 630:
                        return 'TI-59V'
                    elif self.potencia == 1000:
                        return 'TI-60V'
                    elif self.potencia == 1250:
                        return 'TI-61V'
            elif 24 >= self.tension > 17.5:
                if self .numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-42W'
                    elif self.potencia == 25:
                        return 'TI-43W'
                    elif self.potencia == 50:
                        return 'TI-44W'
                    elif self.potencia == 100:
                        return 'TI-45W'
                    elif self.potencia == 160:
                        return 'TI-46W'
                    elif self.potencia == 250:
                        return 'TI-47W'
                    elif self.potencia == 400:
                        return 'TI-48W'
                    elif self.potencia == 630:
                        return 'TI-49W'
                    elif self.potencia == 1000:
                        return 'TI-50W'
                    elif self.potencia == 1250:
                        return 'TI-51W'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-52W'
                    elif self.potencia == 25:
                        return 'TI-53W'
                    elif self.potencia == 50:
                        return 'TI-54W'
                    elif self.potencia == 100:
                        return 'TI-55W'
                    elif self.potencia == 160:
                        return 'TI-56W'
                    elif self.potencia == 250:
                        return 'TI-57W'
                    elif self.potencia == 400:
                        return 'TI-58W'
                    elif self.potencia == 630:
                        return 'TI-59W'
                    elif self.potencia == 1000:
                        return 'TI-60W'
                    elif self.potencia == 1250:
                        return 'TI-61W'
            elif 36 >= self.tension > 24:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-42B'
                    elif self.potencia == 25:
                        return 'TI-43B'
                    elif self.potencia == 50:
                        return 'TI-44B'
                    elif self.potencia == 100:
                        return 'TI-45B'
                    elif self.potencia == 160:
                        return 'TI-46B'
                    elif self.potencia == 250:
                        return 'TI-47B'
                    elif self.potencia == 400:
                        return 'TI-48B'
                    elif self.potencia == 630:
                        return 'TI-49B'
                    elif self.potencia == 1000:
                        return 'TI-50B'
                    elif self.potencia == 1250:
                        return 'TI-51B'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-52B'
                    elif self.potencia == 25:
                        return 'TI-53B'
                    elif self.potencia == 50:
                        return 'TI-54B'
                    elif self.potencia == 100:
                        return 'TI-55B'
                    elif self.potencia == 160:
                        return 'TI-56B'
                    elif self.potencia == 250:
                        return 'TI-57B'
                    elif self.potencia == 400:
                        return 'TI-58B'
                    elif self.potencia == 630:
                        return 'TI-59B'
                    elif self.potencia == 1000:
                        return 'TI-60B'
                    elif self.potencia == 1250:
                        return 'TI-61B'
            elif 52 >= self.tension > 36:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-42C'
                    elif self.potencia == 25:
                        return 'TI-43C'
                    elif self.potencia == 50:
                        return 'TI-44C'
                    elif self.potencia == 100:
                        return 'TI-45C'
                    elif self.potencia == 160:
                        return 'TI-46C'
                    elif self.potencia == 250:
                        return 'TI-47C'
                    elif self.potencia == 400:
                        return 'TI-48C'
                    elif self.potencia == 630:
                        return 'TI-49C'
                    elif self.potencia == 1000:
                        return 'TI-50C'
                    elif self.potencia == 1250:
                        return 'TI-51C'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-52C'
                    elif self.potencia == 25:
                        return 'TI-53C'
                    elif self.potencia == 50:
                        return 'TI-54C'
                    elif self.potencia == 100:
                        return 'TI-55C'
                    elif self.potencia == 160:
                        return 'TI-56C'
                    elif self.potencia == 250:
                        return 'TI-57C'
                    elif self.potencia == 400:
                        return 'TI-58C'
                    elif self.potencia == 630:
                        return 'TI-59C'
                    elif self.potencia == 1000:
                        return 'TI-60C'
                    elif self.potencia == 1250:
                        return 'TI-61C'
            elif 72.5 >= self.tension > 52:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-42D'
                    elif self.potencia == 25:
                        return 'TI-43D'
                    elif self.potencia == 50:
                        return 'TI-44D'
                    elif self.potencia == 100:
                        return 'TI-45D'
                    elif self.potencia == 160:
                        return 'TI-46D'
                    elif self.potencia == 250:
                        return 'TI-47D'
                    elif self.potencia == 400:
                        return 'TI-48D'
                    elif self.potencia == 630:
                        return 'TI-49D'
                    elif self.potencia == 1000:
                        return 'TI-50D'
                    elif self.potencia == 1250:
                        return 'TI-51D'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-52D'
                    elif self.potencia == 25:
                        return 'TI-53D'
                    elif self.potencia == 50:
                        return 'TI-54D'
                    elif self.potencia == 100:
                        return 'TI-55D'
                    elif self.potencia == 160:
                        return 'TI-56D'
                    elif self.potencia == 250:
                        return 'TI-57D'
                    elif self.potencia == 400:
                        return 'TI-58D'
                    elif self.potencia == 630:
                        return 'TI-59D'
                    elif self.potencia == 1000:
                        return 'TI-60D'
                    elif self.potencia == 1250:
                        return 'TI-61D'
        elif self.situacion == 'I':
            if 12 >= self.tension >= 1:
                if self.potencia == 15:
                    return 'TI-62U'
                elif self.potencia == 25:
                    return 'TI-63U'
                elif self.potencia == 50:
                    return 'TI-64U'
                elif self.potencia == 100:
                    return 'TI-65U'
                elif self.potencia == 160:
                    return 'TI-66U'
                elif self.potencia == 250:
                    return 'TI-67U'
            elif 17.5 >= self.tension > 12:
                if self.potencia == 15:
                    return 'TI-62V'
                elif self.potencia == 25:
                    return 'TI-63V'
                elif self.potencia == 50:
                    return 'TI-64V'
                elif self.potencia == 100:
                    return 'TI-65V'
                elif self.potencia == 160:
                    return 'TI-66v'
                elif self.potencia == 250:
                    return 'TI-67v'
            elif 24 >= self.tension > 17.5:
                if self.potencia == 15:
                    return 'TI-62W'
                elif self.potencia == 25:
                    return 'TI-63W'
                elif self.potencia == 50:
                    return 'TI-64W'
                elif self.potencia == 100:
                    return 'TI-65W'
                elif self.potencia == 160:
                    return 'TI-66W'
                elif self.potencia == 250:
                    return 'TI-67W'
            elif 36 >= self.tension > 24:
                if self.potencia == 15:
                    return 'TI-62B'
                elif self.potencia == 25:
                    return 'TI-63B'
                elif self.potencia == 50:
                    return 'TI-64B'
                elif self.potencia == 100:
                    return 'TI-65B'
                elif self.potencia == 160:
                    return 'TI-66B'
                elif self.potencia == 250:
                    return 'TI-67B'
            elif 52 >= self.tension > 36:
                if self.potencia == 15:
                    return 'TI-62C'
                elif self.potencia == 25:
                    return 'TI-63C'
                elif self.potencia == 50:
                    return 'TI-64C'
                elif self.potencia == 100:
                    return 'TI-65C'
                elif self.potencia == 160:
                    return 'TI-66C'
                elif self.potencia == 250:
                    return 'TI-67C'
            elif 72.5 >= self.tension > 52:
                if self.potencia == 15:
                    return 'TI-62D'
                elif self.potencia == 25:
                    return 'TI-63D'
                elif self.potencia == 50:
                    return 'TI-64D'
                elif self.potencia == 100:
                    return 'TI-65D'
                elif self.potencia == 160:
                    return 'TI-66D'
                elif self.potencia == 250:
                    return 'TI-67D'
        elif self.situacion == 'S':
            if 12 >= self.tension >= 1:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-68U'
                    elif self.potencia == 25:
                        return 'TI-69U'
                    elif self.potencia == 50:
                        return 'TI-70U'
                    elif self.potencia == 100:
                        return 'TI-71U'
                    elif self.potencia == 160:
                        return 'TI-72U'
                    elif self.potencia == 250:
                        return 'TI-73U'
                    elif self.potencia == 400:
                        return 'TI-74U'
                    elif self.potencia == 630:
                        return 'TI-75U'
                    elif self.potencia == 1000:
                        return 'TI-76U'
                    elif self.potencia == 1250:
                        return 'TI-77U'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-78U'
                    elif self.potencia == 25:
                        return 'TI-79U'
                    elif self.potencia == 50:
                        return 'TI-80U'
                    elif self.potencia == 100:
                        return 'TI-81U'
                    elif self.potencia == 160:
                        return 'TI-82U'
                    elif self.potencia == 250:
                        return 'TI-83U'
                    elif self.potencia == 400:
                        return 'TI-84U'
                    elif self.potencia == 630:
                        return 'TI-85U'
                    elif self.potencia == 1000:
                        return 'TI-86U'
                    elif self.potencia == 1250:
                        return 'TI-87U'
            elif 17.5 >= self.tension > 12:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-68V'
                    elif self.potencia == 25:
                        return 'TI-69V'
                    elif self.potencia == 50:
                        return 'TI-70V'
                    elif self.potencia == 100:
                        return 'TI-71V'
                    elif self.potencia == 160:
                        return 'TI-72V'
                    elif self.potencia == 250:
                        return 'TI-73V'
                    elif self.potencia == 400:
                        return 'TI-74V'
                    elif self.potencia == 630:
                        return 'TI-75V'
                    elif self.potencia == 1000:
                        return 'TI-76V'
                    elif self.potencia == 1250:
                        return 'TI-77V'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-78V'
                    elif self.potencia == 25:
                        return 'TI-79V'
                    elif self.potencia == 50:
                        return 'TI-80V'
                    elif self.potencia == 100:
                        return 'TI-81V'
                    elif self.potencia == 160:
                        return 'TI-82V'
                    elif self.potencia == 250:
                        return 'TI-83V'
                    elif self.potencia == 400:
                        return 'TI-84V'
                    elif self.potencia == 630:
                        return 'TI-85V'
                    elif self.potencia == 1000:
                        return 'TI-86V'
                    elif self.potencia == 1250:
                        return 'TI-87V'
            elif 24 >= self.tension > 17.5:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-68W'
                    elif self.potencia == 25:
                        return 'TI-69W'
                    elif self.potencia == 50:
                        return 'TI-70W'
                    elif self.potencia == 100:
                        return 'TI-71W'
                    elif self.potencia == 160:
                        return 'TI-72W'
                    elif self.potencia == 250:
                        return 'TI-73W'
                    elif self.potencia == 400:
                        return 'TI-74W'
                    elif self.potencia == 630:
                        return 'TI-75W'
                    elif self.potencia == 1000:
                        return 'TI-76W'
                    elif self.potencia == 1250:
                        return 'TI-77W'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-78W'
                    elif self.potencia == 25:
                        return 'TI-79W'
                    elif self.potencia == 50:
                        return 'TI-80W'
                    elif self.potencia == 100:
                        return 'TI-81W'
                    elif self.potencia == 160:
                        return 'TI-82W'
                    elif self.potencia == 250:
                        return 'TI-83W'
                    elif self.potencia == 400:
                        return 'TI-84W'
                    elif self.potencia == 630:
                        return 'TI-85W'
                    elif self.potencia == 1000:
                        return 'TI-86W'
                    elif self.potencia == 1250:
                        return 'TI-87W'
            elif 36 >= self.tension > 24:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-68B'
                    elif self.potencia == 25:
                        return 'TI-69B'
                    elif self.potencia == 50:
                        return 'TI-70B'
                    elif self.potencia == 100:
                        return 'TI-71B'
                    elif self.potencia == 160:
                        return 'TI-72B'
                    elif self.potencia == 250:
                        return 'TI-73B'
                    elif self.potencia == 400:
                        return 'TI-74B'
                    elif self.potencia == 630:
                        return 'TI-75B'
                    elif self.potencia == 1000:
                        return 'TI-76B'
                    elif self.potencia == 1250:
                        return 'TI-77B'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-78B'
                    elif self.potencia == 25:
                        return 'TI-79B'
                    elif self.potencia == 50:
                        return 'TI-80B'
                    elif self.potencia == 100:
                        return 'TI-81B'
                    elif self.potencia == 160:
                        return 'TI-82B'
                    elif self.potencia == 250:
                        return 'TI-83B'
                    elif self.potencia == 400:
                        return 'TI-84B'
                    elif self.potencia == 630:
                        return 'TI-85B'
                    elif self.potencia == 1000:
                        return 'TI-86B'
                    elif self.potencia == 1250:
                        return 'TI-87B'
            elif 52 >= self.tension > 36:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-68C'
                    elif self.potencia == 25:
                        return 'TI-69C'
                    elif self.potencia == 50:
                        return 'TI-70C'
                    elif self.potencia == 100:
                        return 'TI-71C'
                    elif self.potencia == 160:
                        return 'TI-72C'
                    elif self.potencia == 250:
                        return 'TI-73C'
                    elif self.potencia == 400:
                        return 'TI-74C'
                    elif self.potencia == 630:
                        return 'TI-75C'
                    elif self.potencia == 1000:
                        return 'TI-76C'
                    elif self.potencia == 1250:
                        return 'TI-77C'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-78C'
                    elif self.potencia == 25:
                        return 'TI-79B'
                    elif self.potencia == 50:
                        return 'TI-80C'
                    elif self.potencia == 100:
                        return 'TI-81C'
                    elif self.potencia == 160:
                        return 'TI-82C'
                    elif self.potencia == 250:
                        return 'TI-83C'
                    elif self.potencia == 400:
                        return 'TI-84C'
                    elif self.potencia == 630:
                        return 'TI-85C'
                    elif self.potencia == 1000:
                        return 'TI-86C'
                    elif self.potencia == 1250:
                        return 'TI-87C'
            elif 72.5 >= self.tension > 52:
                if self.numero_maquinas == 1:
                    if self.potencia == 15:
                        return 'TI-68D'
                    elif self.potencia == 25:
                        return 'TI-69D'
                    elif self.potencia == 50:
                        return 'TI-70D'
                    elif self.potencia == 100:
                        return 'TI-71D'
                    elif self.potencia == 160:
                        return 'TI-72D'
                    elif self.potencia == 250:
                        return 'TI-73D'
                    elif self.potencia == 400:
                        return 'TI-74D'
                    elif self.potencia == 630:
                        return 'TI-75D'
                    elif self.potencia == 1000:
                        return 'TI-76D'
                    elif self.potencia == 1250:
                        return 'TI-77D'
                elif self.numero_maquinas == 2:
                    if self.potencia == 15:
                        return 'TI-78D'
                    elif self.potencia == 25:
                        return 'TI-79D'
                    elif self.potencia == 50:
                        return 'TI-80D'
                    elif self.potencia == 100:
                        return 'TI-81D'
                    elif self.potencia == 160:
                        return 'TI-82D'
                    elif self.potencia == 250:
                        return 'TI-83D'
                    elif self.potencia == 400:
                        return 'TI-84D'
                    elif self.potencia == 630:
                        return 'TI-85D'
                    elif self.potencia == 1000:
                        return 'TI-86D'
                    elif self.potencia == 1250:
                        return 'TI-87D'
        if self.numero_maquinas == 0:
            if self.situacion == 'C' and (12 >= self.tension >= 1):
                return 'TI-0CU'
            elif self.situacion == 'I' and (12 >= self.tension >= 1):
                return 'TI-OIU'
            elif self.situacion == 'L' and (12 >= self.tension >= 1):
                return 'TI-0LU'
            elif self.situacion == 'S' and (12 >= self.tension >= 1):
                return 'TI-0SU'

            if self.situacion == 'C' and (17.5 >= self.tension > 12):
                return 'TI-0CV'
            elif self.situacion == 'I' and (17.5 >= self.tension > 12):
                return 'TI-OIV'
            elif self.situacion == 'L' and (17.5 >= self.tension > 12):
                return 'TI-0LV'
            elif self.situacion == 'S' and (17.5 >= self.tension > 12):
                return 'TI-0SV'

            if self.situacion == 'C' and (24 >= self.tension > 17.5):
                return 'TI-0CW'
            elif self.situacion == 'I' and (24 >= self.tension > 17.5):
                return 'TI-OIW'
            elif self.situacion == 'L' and (24 >= self.tension > 17.5):
                return 'TI-0LW'
            elif self.situacion == 'S' and (24 >= self.tension > 17.5):
                return 'TI-0SW'

            if self.situacion == 'C' and (36 >= self.tension > 24):
                return 'TI-0CX'
            elif self.situacion == 'I' and (36 >= self.tension > 24):
                return 'TI-OIX'
            elif self.situacion == 'L' and (36 >= self.tension > 24):
                return 'TI-0LX'
            elif self.situacion == 'S' and (36 >= self.tension > 24):
                return 'TI-0SX'

            if self.situacion == 'C' and (52 >= self.tension > 36):
                return 'TI-0CY'
            elif self.situacion == 'I' and (52 >= self.tension > 36):
                return 'TI-OIY'
            elif self.situacion == 'L' and (52 >= self.tension > 36):
                return 'TI-0LY'
            elif self.situacion == 'S' and (52 >= self.tension > 36):
                return 'TI-0SY'

            if self.situacion == 'C' and (72.5 >= self.tension > 52):
                return 'TI-0CZ'
            elif self.situacion == 'I' and (72.5 >= self.tension > 52):
                return 'TI-OIZ'
            elif self.situacion == 'L' and (72.5 >= self.tension > 52):
                return 'TI-0LZ'
            elif self.situacion == 'S' and (72.5 >= self.tension > 52):
                return 'TI-0SZ'
        return None
