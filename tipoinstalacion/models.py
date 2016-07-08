
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
        from tipoinstalacion import nearest

        if self.situacion == 'C':
            if 12 >= self.tension >= 1:
                if self.numero_maquinas == 1:
                    values = {
                        15: '22',
                        25: '23',
                        50: '24',
                        100: '25',
                        160: '26',
                        250: '27',
                        400: '28',
                        630: '29',
                        1000: '30',
                        1250: '31'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}U'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '32',
                        25: '33',
                        50: '34',
                        100: '35',
                        160: '36',
                        250: '37',
                        400: '38',
                        630: '39',
                        1000: '40',
                        1250: '41'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}U'.format(values[key])
            elif 17.5 >= self.tension > 12:
                if self.numero_maquinas == 1:
                    values = {
                        15: '22',
                        25: '23',
                        50: '24',
                        100: '25',
                        160: '26',
                        250: '27',
                        400: '28',
                        630: '29',
                        1000: '30',
                        1250: '31'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}V'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '32',
                        25: '33',
                        50: '34',
                        100: '35',
                        160: '36',
                        250: '37',
                        400: '38',
                        630: '39',
                        1000: '40',
                        1250: '41'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}V'.format(values[key])
            elif 24 >= self.tension > 17.5:
                if self.numero_maquinas == 1:
                    values = {
                        15: '22',
                        25: '23',
                        50: '24',
                        100: '25',
                        160: '26',
                        250: '27',
                        400: '28',
                        630: '29',
                        1000: '30',
                        1250: '31'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}W'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '32',
                        25: '33',
                        50: '34',
                        100: '35',
                        160: '36',
                        250: '37',
                        400: '38',
                        630: '39',
                        1000: '40',
                        1250: '41'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}W'.format(values[key])
            elif 36 >= self.tension > 24:
                if self.numero_maquinas == 1:
                    values = {
                        15: '22',
                        25: '23',
                        50: '24',
                        100: '25',
                        160: '26',
                        250: '27',
                        400: '28',
                        630: '29',
                        1000: '30',
                        1250: '31'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}B'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '32',
                        25: '33',
                        50: '34',
                        100: '35',
                        160: '36',
                        250: '37',
                        400: '38',
                        630: '39',
                        1000: '40',
                        1250: '41'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}B'.format(values[key])
            elif 52 >= self.tension > 36:
                if self.numero_maquinas == 1:
                    values = {
                        15: '22',
                        25: '23',
                        50: '24',
                        100: '25',
                        160: '26',
                        250: '27',
                        400: '28',
                        630: '29',
                        1000: '30',
                        1240: '31'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}C'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '32',
                        25: '33',
                        50: '34',
                        100: '35',
                        160: '36',
                        250: '37',
                        400: '38',
                        630: '39',
                        1000: '40',
                        1250: '41'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}C'.format(values[key])
            elif 72.5 >= self.tension > 52:
                if self.numero_maquinas == 1:
                    values = {
                        15: '22',
                        25: '23',
                        50: '24',
                        100: '25',
                        160: '26',
                        250: '27',
                        400: '28',
                        630: '29',
                        1000: '30',
                        1250: '31',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}D'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '32',
                        25: '33',
                        50: '34',
                        100: '35',
                        160: '36',
                        250: '37',
                        400: '38',
                        630: '39',
                        1000: '40',
                        1250: '41',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}D'.format(values[key])
        elif self.situacion == 'L':
            if 12 >= self.tension >= 1:
                if self.numero_maquinas == 1:
                    values = {
                        15: '42',
                        25: '43',
                        50: '44',
                        100: '45',
                        160: '46',
                        250: '47',
                        400: '48',
                        630: '49',
                        1000: '50',
                        1250: '51',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}U'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '52',
                        25: '53',
                        50: '54',
                        100: '55',
                        160: '56',
                        250: '57',
                        400: '58',
                        630: '59',
                        1000: '60',
                        1250: '61',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}U'.format(values[key])
            elif 17.5 >= self.tension > 12:
                if self.numero_maquinas == 1:
                    values = {
                        15: '42',
                        25: '43',
                        50: '44',
                        100: '45',
                        160: '46',
                        250: '47',
                        400: '48',
                        630: '49',
                        1000: '50',
                        1250: '51',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}V'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '52',
                        25: '53',
                        50: '54',
                        100: '55',
                        160: '56',
                        250: '57',
                        400: '58',
                        630: '59',
                        1000: '60',
                        1250: '61',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}V'.format(values[key])
            elif 24 >= self.tension > 17.5:
                if self .numero_maquinas == 1:
                    values = {
                        15: '42',
                        25: '43',
                        50: '44',
                        100: '45',
                        160: '46',
                        250: '47',
                        400: '48',
                        630: '49',
                        1000: '50',
                        1250: '51',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}W'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '52',
                        25: '53',
                        50: '54',
                        100: '55',
                        160: '56',
                        250: '57',
                        400: '58',
                        630: '59',
                        1000: '60',
                        1250: '61',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}W'.format(values[key])
            elif 36 >= self.tension > 24:
                if self.numero_maquinas == 1:
                    values = {
                        15: '42',
                        25: '43',
                        50: '44',
                        100: '45',
                        160: '46',
                        250: '47',
                        400: '48',
                        630: '49',
                        1000: '50',
                        1250: '51',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}B'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '52',
                        25: '53',
                        50: '54',
                        100: '55',
                        160: '56',
                        250: '57',
                        400: '58',
                        630: '59',
                        1000: '60',
                        1250: '61',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}B'.format(values[key])
            elif 52 >= self.tension > 36:
                if self.numero_maquinas == 1:
                    values = {
                        15: '42',
                        25: '43',
                        50: '44',
                        100: '45',
                        160: '46',
                        250: '47',
                        400: '48',
                        630: '49',
                        1000: '50',
                        1250: '51',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}C'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '52',
                        25: '53',
                        50: '54',
                        100: '55',
                        160: '56',
                        250: '57',
                        400: '58',
                        630: '59',
                        1000: '60',
                        1250: '61',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}C'.format(values[key])
            elif 72.5 >= self.tension > 52:
                if self.numero_maquinas == 1:
                    values = {
                        15: '42',
                        25: '43',
                        50: '44',
                        100: '45',
                        160: '46',
                        250: '47',
                        400: '48',
                        630: '49',
                        1000: '50',
                        1250: '51',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}D'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '52',
                        25: '53',
                        50: '54',
                        100: '55',
                        160: '56',
                        250: '57',
                        400: '58',
                        630: '59',
                        1000: '60',
                        1250: '61',
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}D'.format(values[key])
        elif self.situacion == 'I':
            if 12 >= self.tension >= 1:
                values = {
                    15: '62',
                    25: '63',
                    50: '64',
                    100: '65',
                    160: '66',
                    250: '67'
                }
                key = nearest(self.potencia, *values.keys())
                return 'TI-{0}U'.format(values[key])
            elif 17.5 >= self.tension > 12:
                values = {
                    15: '62',
                    25: '63',
                    50: '64',
                    100: '65',
                    160: '66',
                    250: '67'
                }
                key = nearest(self.potencia, *values.keys())
                return 'TI-{0}V'.format(values[key])
            elif 24 >= self.tension > 17.5:
                values = {
                    15: '62',
                    25: '63',
                    50: '64',
                    100: '65',
                    160: '66',
                    250: '67'
                }
                key = nearest(self.potencia, *values.keys())
                return 'TI-{0}W'.format(values[key])
            elif 36 >= self.tension > 24:
                values = {
                    15: '62',
                    25: '63',
                    50: '64',
                    100: '65',
                    160: '66',
                    250: '67'
                }
                key = nearest(self.potencia, *values.keys())
                return 'TI-{0}B'.format(values[key])
            elif 52 >= self.tension > 36:
                values = {
                    15: '62',
                    25: '63',
                    50: '64',
                    100: '65',
                    160: '66',
                    250: '67'
                }
                key = nearest(self.potencia, *values.keys())
                return 'TI-{0}C'.format(values[key])
            elif 72.5 >= self.tension > 52:
                values = {
                    15: '62',
                    25: '63',
                    50: '64',
                    100: '65',
                    160: '66',
                    250: '67'
                }
                key = nearest(self.potencia, *values.keys())
                return 'TI-{0}D'.format(values[key])
        elif self.situacion == 'S':
            if 12 >= self.tension >= 1:
                if self.numero_maquinas == 1:
                    values = {
                        15: '68',
                        25: '69',
                        50: '70',
                        100: '71',
                        160: '72',
                        250: '73',
                        400: '74',
                        630: '75',
                        1000: '76',
                        1250: '77'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}U'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '78',
                        25: '79',
                        50: '80',
                        100: '81',
                        160: '82',
                        250: '83',
                        400: '84',
                        630: '85',
                        1000: '86',
                        1250: '87'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}U'.format(values[key])
            elif 17.5 >= self.tension > 12:
                if self.numero_maquinas == 1:
                    values = {
                        15: '68',
                        25: '69',
                        50: '70',
                        100: '71',
                        160: '72',
                        250: '73',
                        400: '74',
                        630: '75',
                        1000: '76',
                        1250: '77'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}V'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '78',
                        25: '79',
                        50: '80',
                        100: '81',
                        160: '82',
                        250: '83',
                        400: '84',
                        630: '85',
                        1000: '86',
                        1250: '87'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}V'.format(values[key])
            elif 24 >= self.tension > 17.5:
                if self.numero_maquinas == 1:
                    values = {
                        15: '68',
                        25: '69',
                        50: '70',
                        100: '71',
                        160: '72',
                        250: '73',
                        400: '74',
                        630: '75',
                        1000: '76',
                        1250: '77'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}W'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '78',
                        25: '79',
                        50: '80',
                        100: '81',
                        160: '82',
                        250: '83',
                        400: '84',
                        630: '85',
                        1000: '86',
                        1250: '87'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}W'.format(values[key])
            elif 36 >= self.tension > 24:
                if self.numero_maquinas == 1:
                    values = {
                        15: '68',
                        25: '69',
                        50: '70',
                        100: '71',
                        160: '72',
                        250: '73',
                        400: '74',
                        630: '75',
                        1000: '76',
                        1250: '77'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}B'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '78',
                        25: '79',
                        50: '80',
                        100: '81',
                        160: '82',
                        250: '83',
                        400: '84',
                        630: '85',
                        1000: '86',
                        1250: '87'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}B'.format(values[key])
            elif 52 >= self.tension > 36:
                if self.numero_maquinas == 1:
                    values = {
                        15: '68',
                        25: '69',
                        50: '70',
                        100: '71',
                        160: '72',
                        250: '73',
                        400: '74',
                        630: '75',
                        1000: '76',
                        1250: '77'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}C'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '78',
                        25: '79',
                        50: '80',
                        100: '81',
                        160: '82',
                        250: '83',
                        400: '84',
                        630: '85',
                        1000: '86',
                        1250: '87'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}C'.format(values[key])
            elif 72.5 >= self.tension > 52:
                if self.numero_maquinas == 1:
                    values = {
                        15: '68',
                        25: '69',
                        50: '70',
                        100: '71',
                        160: '72',
                        250: '73',
                        400: '74',
                        630: '75',
                        1000: '76',
                        1250: '77'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}C'.format(values[key])
                elif self.numero_maquinas == 2:
                    values = {
                        15: '78',
                        25: '79',
                        50: '80',
                        100: '81',
                        160: '82',
                        250: '83',
                        400: '84',
                        630: '85',
                        1000: '86',
                        1250: '87'
                    }
                    key = nearest(self.potencia, *values.keys())
                    return 'TI-{0}D'.format(values[key])

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


class Fiabilidad(object):
    """
    Objeto que representa un elemento de fiabilidad
    """
    def __init__(self):
        self.tipoelemento = None
        """Tipo de elemento:

        - Seccionador de cuchillas: ``S``
        - Reconectador: ``R``
        - Reconectador: ``RS``
        - Seccionador - Fusible (XS-SXS): ``SF``
        - Autoseccionador/Seccionalizador: ``AS``
        - Interruptor: ``I``
        - Interruptor - seccionador: ``IS``
        - Interruptor - seccionador telecontorlado: ``IST``

        """

    @property
    def tipoinstalacion(self):
        if self.tipoelemento == 'S':
            return 'TI-174'
        elif self.tipoelemento == 'R':
            return 'TI-177'
        elif self.tipoelemento == 'RS':
            return 'TI-179'
        elif self.tipoelemento == 'SF':
            return 'TI-181'
        elif self.tipoelemento == 'AS':
            return 'TI-182'
        elif self.tipoelemento == 'I':
            return 'TI-183'
        elif self.tipoelemento == 'IS':
            return 'TI-187'
        elif self.tipoelemento == 'IST':
            return 'TI-187A'
