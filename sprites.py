import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        super().__init__(self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.pos = pg.math.Vector2(x, y)
        self.rect.center = self.pos
        self.speed = 300

    def update(self):
        keys = pg.key.get_pressed()
        vel = pg.math.Vector2(0, 0)
        if keys[pg.K_LEFT]:  vel.x = -1
        if keys[pg.K_RIGHT]: vel.x = 1
        if keys[pg.K_UP]:    vel.y = -1
        if keys[pg.K_DOWN]:  vel.y = 1
        
        if vel.length() > 0:
            vel = vel.normalize()
            
        self.pos += vel * self.speed * self.game.dt
        self.rect.center = self.pos