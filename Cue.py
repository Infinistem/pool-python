import pygame, math, random

class Cue:
    def __init__(self, screen, pos):
        self.screen = screen
        self.cue = 'Images/cue.png'
        self.image = pygame.image.load(self.cue)
        self.dx = None
        self.dy = None
        self.angle = 0
        self.force = 0
        self.pos = pos
        self.center = (820, 335) 
    def rot(self, angle):
        self.angle = angle
    def draw(self):
        new = pygame.transform.rotate(self.image, self.angle)
        rec = new.get_rect(center=self.image.get_rect(center=self.center).center)
        self.screen.blit(new, rec)
