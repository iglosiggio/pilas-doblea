# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilasengine import colores
from pilasengine.fondos.fondo import Fondo

class Fondos(object):
    """Representa la propiedad pilas.fondos

    Este objeto se encarga de hacer accesible
    la creación de fondos para las escenas.
    """

    def __init__(self, pilas):
        self.pilas = pilas

    def Plano(self):
        from pilasengine.fondos import plano
        nuevo_fondo = plano.Plano(self.pilas)
        # Importante: cuando se inicializa el actor, el método __init__
        #             realiza una llamada a pilas.actores.agregar_actor
        #             para vincular el actor a la escena.
        return nuevo_fondo

    def Galaxia(self, dx=0, dy=-1):
        from pilasengine.fondos import galaxia
        nuevo_fondo = galaxia.Galaxia(self.pilas)
        nuevo_fondo.dx = dx
        nuevo_fondo.dy = dy
        return nuevo_fondo

    def Tarde(self):
        from pilasengine.fondos import tarde
        return tarde.Tarde(self.pilas)

    def Selva(self):
        from pilasengine.fondos import selva
        return selva.Selva(self.pilas)

    def Noche(self):
        from pilasengine.fondos import noche
        return noche.Noche(self.pilas)

    def Espacio(self):
        from pilasengine.fondos import espacio
        return espacio.Espacio(self.pilas)

    def Nubes(self):
        from pilasengine.fondos import nubes
        return nubes.Nubes(self.pilas)

    def Pasto(self):
        from pilasengine.fondos import pasto
        return pasto.Pasto(self.pilas)

    def Volley(self):
        from pilasengine.fondos import volley
        return volley.Volley(self.pilas)

    def Color(self, _color=colores.blanco):
        from pilasengine.fondos import color
        return color.Color(self.pilas, _color)

    def Blanco(self):
        from pilasengine.fondos import blanco
        return blanco.Blanco(self.pilas)

    def Fondo(self, imagen=None):
        from pilasengine.fondos import fondo
        return fondo.Fondo(self.pilas, imagen)

    def FondoMozaico(self, imagen=None):
        from pilasengine.fondos import fondo_mozaico
        return fondo_mozaico.FondoMozaico(self.pilas, imagen)

    def Cesped(self):
        from pilasengine.fondos import cesped
        return cesped.Cesped(self.pilas)

    def DesplazamientoHorizontal(self):
        from pilasengine.fondos import desplazamiento_horizontal
        return desplazamiento_horizontal.DesplazamientoHorizontal(self.pilas)
