import pygame, math, random, time
from datetime import datetime
from Vector import Vector
w = 1200 # redeclare width and height constants. (didnt find it nessisary to make a constants file)
h = 650
class Sphere: # represents a spherical object on the physical space (table)
    def __init__(self,screen, radius, position, number):
        self.radius = radius
        self.screen = screen
        self.position = Vector(position[0], position[1])
        self.number = number
        self.force = 0
        self.accel = Vector(0, 0)
        self.vel = Vector(0, 0)
        self.gone = False
        # init collision handler
    def draw(self): 
        image = pygame.image.load(f"Images/ball_{self.number}.png")
        self.screen.blit(image, (self.position.x, self.position.y))
    def cue(self): # cue ball
        image = pygame.image.load("Images/ball_16.png")
        self.screen.blit(image, (self.position.x, self.position.y))
    def distance(self, sphere): # distance between two spheres
        dy, dx = (self.position.x - sphere.position.x), (self.position.y - sphere.position.y)
        return dx, dy, Vector(dx, dy).length()
    def update(self):
        self.vel.add(self.accel)
        self.position.add(self.vel)
        self.accel.assign(0, 0) # acceleration is set to zero
        self.vel.mult(.98)
        self.edge()
        
    def collide(self,sphere):
        dx, dy, distance = self.distance(sphere)
        if distance <= sphere.radius + self.radius: # spheres are colliding!
            dx /= distance # apply impulse i think its called? basiclly they bounce off of eachother. Idk i havnt taken physics yet (though i want to and will learn it for my website)
            dy /= distance 
            self.position.x += dx
            self.position.y += dy
            sphere.position.x -= dx
            sphere.position.y -= dy
            calcpy1, calcpy2 = self.vel.dupe(), sphere.vel.dupe()
            calcpy1.add(Vector.projectUontoV(sphere.vel, Vector.minusO(sphere.pos, self.pos)))
            calcpy1.sub(Vector.projectUontoV(self.vel, Vector.minusO(self.pos, sphere.pos)))
            self.vel = calcpy1
            sphere.vel = calcpy2
            return calcpy1.length() / 7
        return None

    def edge(self):
        if(self.position.x - self.radius < 0 or self.position.x + self.radius > w):
            self.position.x = min(max(self.position.x, self.radius), w-self.radius)
            self.vel.x = -self.vel.x
        if(self.position.y - self.radius < 0 or self.position.y + self.radius > h):
            self.y = min(max(self.position.y, self.radius), h-self.radius)
            self.vel.y = -self.vel.y
    def pocket(self, pocket): # call when pocket collides. Takes a pocket class
        dx, dy, dist = self.distance(pocket)
        if not self.number == -1:
            if dist < self.radius + self.radius/2 :
                self.gone = True
                self.vel.assign(0, 0)
                self.accel.assign(0, 0)
        elif self.number == -1 and dist < self.radius + self.radius/2:
            self.position = Vector(800, 325)
        
