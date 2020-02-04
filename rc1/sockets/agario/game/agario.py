from pygame.locals import *
import pygame

from game.settings import *
from game.blob import Blob

class Agario:
    def __init__(self):
        self.size = self.width, self.height = WIDTH, HEIGHT
        self.running = False
        self._disp_window = None

    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 20)
        self.running = True
        self._disp_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Agario")
        self.blob = Blob(WIDTH//2, HEIGHT//2, 64)

    def on_cleanup(self):
        pygame.quit()
        pygame.font.quit()

    def on_render(self):
        self.blob.show(self._disp_window)

    def on_loop(self):
        pass

    def on_execute(self):
        self.on_init()

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self._disp_window.fill((0,0,0))
            self.on_loop()
            self.on_render()
            pygame.display.flip()
            #self.clock.tick(60)

        self.on_cleanup()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False