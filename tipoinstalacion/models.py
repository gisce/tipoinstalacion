
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
            #print 'u:{}'.format(u)
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
            elif 17.5 >= u > 12:
                pass
            elif 12 >= u > 1:
                pass
            elif 1 > u:
                pass
            else:
                return 'TI-'
        elif self.despliegue[0] == 'S':
            return 'TI-'
        return 'TI-'


class Posicion(object):
    """
    Objeto que representa una posicion


    """

    def __init__(self):
        pass
