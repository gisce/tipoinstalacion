
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
                if 0 < s <= 180:
                    return 'TI-1UX'
                elif 180 < s <= 300:
                    return 'TI-1UY'
                elif 300 < s:
                    return 'TI-1UZ'
            elif 123 >= u > 72.5:
                pass
            elif 72.5 >= u > 52:
                pass
            elif 52 >= u > 36:
                pass
            elif 36 >= u > 24:
                pass
            elif 24 >= u > 17.5:
                pass
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

