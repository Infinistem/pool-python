import pygame, math, random, time
from Vector import Vector

class Pocket():
    def __init__(self, radius, pos, screen):
        self.radius = radius
        self.position = Vector(pos[0], pos[1])
        self.screen = screen
    def draw(self):
        pygame.draw.circle(self.screen, (0,0,0), (self.position.x, self.position.y), float(self.radius)) 