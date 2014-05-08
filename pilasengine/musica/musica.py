# -*- encoding: utf-8 -*-
import os
import pygame

class Musica(object):
    deshabilitado = False

    def __init__(self, ruta):
        self.ruta = ruta
        self.musica = pygame.mixer.Sound(ruta)

    def reproducir(self, repetir=False):
        if repetir:
            self.musica.play(-1)
        else:
            self.musica.play()

    def detener(self):
        "Detiene el audio."
        self.musica.stop()

    def pausar(self):
        "Hace una pausa del audio."
        self.musica.stop()

    def continuar(self):
        "Continúa reproduciendo el audio."
        self.musica.play()

    def __repr__(self):
        nombre = os.path.basename(self.ruta)
        return "<%s del archivo '%s'>" % (self.__class__.__name__, nombre)