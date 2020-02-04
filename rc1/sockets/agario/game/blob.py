from pygame.locals import *
import pygame

class Blob:
    def __init__(self, x, y, r):
        self.pos = self.x, self.y = x, y
        self.r = r

    def show(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.pos, self.r)

    def update(self):
        pass