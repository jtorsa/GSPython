from settings import *
import pygame as pg

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Desplaza la entidad según la posición de la cámara
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        # Para el mapa (que es un Rect solo)
        return rect.move(self.camera.topleft)

    def update(self, target):
        # Centra la cámara en el jugador (target)
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        # Limitar el scroll al tamaño del mapa
        x = min(0, x) # Izquierda
        y = min(0, y) # Arriba
        x = max(-(self.width - WIDTH), x) # Derecha
        y = max(-(self.height - HEIGHT), y) # Abajo
        self.camera = pg.Rect(x, y, self.width, self.height)