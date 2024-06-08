import pygame, math, time

from Vector import Vector
sphere, startPos, endPos, startTime, endTime = None,None,None,None,None

class Table:
    def __init__(self, balls, screen, cue, stick):
        self.score = 0
        self.cuest = stick
        self.order = [] # shoot in order
        self.spheres = balls 
        self.cueBall = cue
        self.screen = screen
        self.startT = None
    def draw(self):
        self.screen.fill((80, 255, 160))
        # draw margins
        rect1 = pygame.Rect(0, 0, 1200, 80)
        pygame.draw.rect(self.screen, (0, 200, 0), rect1)
    def getPos(): # get mouse position
        pos = pygame.mouse.get_pos()
        return {x:pos[0], y:pos[1]}
        self.resetGlobals()
    def resetGlobals(self): 
        global sphere, startPos, endPos, startTime, endTime
        sphere, startPos, endPos, startTime, endTime = None,None,None,None,None
    def spheresCollide():
        for i in range(len(self.spheres)-1):
            for j in range(i+1,len(self.spheres)):
                doesCollide = self.spheres[i].collide(self.spheres[j])
                if doesCollide:
                    pass
    def play(self, startP, startT): # play the cue ball, take center point as arguments
        global sphere, startPos, endPos, startTime, endTime
        startPos = startP
        self.startT = startT
    def sign(self,a):
        if a < 0:
            return -1
        else:
            return 1
    def pointsfromlen(self, length, point, angle): # here we do some simple trigonometry to solve for the points. learn from this :D
        dy = math.sin((angle)) * length # solve for 1 leg of the right triangle
        dx = math.cos((angle)) * length
        return math.atan2(dy, dx)
    def drop(self, endT): # get sphere affected and apply impulse
        # use length of cue stick to deterime end points
        global sphere, startPos, endPos, startTime, endTime
        endTime = time.time()
        angle = -self.pointsfromlen(525, (self.cueBall.position.x, self.cueBall.position.y), self.cuest.angle)
        dt = self.startT - endTime
        print(angle)
        projlen = self.cuest.force * 5
        self.cueBall.accel = Vector(math.cos(angle) * projlen, math.sin(angle) * projlen)
        self.cueBall.accel.mult(self.sign(angle))
        self.cuest.center = (self.cueBall.position.x, self.cueBall.position.y)
        self.cuest.force = 0
        self.cuest.draw()
        self.resetGlobals()
    def showScore():
        pass

        
        
