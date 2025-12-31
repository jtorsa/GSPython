import pygame as pg
import sys
from settings import *
from tilemap import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        # IMPORTANTE: La ruta debe ser correcta
        self.map = TiledMap('assets/island.tmx')
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.camera = Camera(self.map.width, self.map.height)
        self.player = Player(self, WIDTH/2, HEIGHT/2)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill(BLACK)
        # Dibujar mapa con cámara
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # Dibujar sprites con cámara
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

g = Game()
g.new()
g.run()