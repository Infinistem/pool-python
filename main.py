# pygame pool and sphere collision physics project 
# I was able to find images on codingwithruss's github! so i thankfully did not have to make my own sprites or use ugly pygame circles
# for those who love geometry or physics this will be awesome as you can see things you probably learned programmaticlly encorperated

# ive tried to put helpful comments to guide anyone who comes across this on how it works so they can improve their own skills
# This software is under the MIT License and can be found here: 
#########################################################

# import all our external modules, and classes into the main program to be executed
import pygame, math, random, time

from Sphere import Sphere
from Table import Table
from Cue import Cue
from Pocket import Pocket
from Vector import Vector

def Label(font, txt, left, top, col, screen):
    textobj = font.render(txt, 1, tuple(col))
    textrect = textobj.get_rect()
    textrect.topleft = (left, top)
    screen.blit(textobj, textrect)
def Button(font, txt, left, top, col, screen):
    txt = Label()
FPS = 60 # mainloop Frames / Second
WIDTH = 1200
HEIGHT = 650
PANEL = 50
BOUNDS = 80 # margin
ROOT = '/Images' # root for image dir
gameOver = False 
shooting = True
shot = False
ticks = 0
pocketPos = [(0, 110), (600, 110), (1200, 110),(0, 650), (600, 650), (1200, 650)]
# score = points / time in minutes
def spheresCollided():
    pass
def reposcue():
    cue.position = Vector(800, 325)
pygame.init()
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT + PANEL))
pygame.display.set_caption("Play Pool! - Singleplayer")
font = pygame.font.SysFont(None, 30)
itt, z = 0, 5
sample = [x for x in range(1, 16, 1)]
balls = []
itt = 0
for x in range(5):
    for y in range(z):
        if itt >= 16:
            break 
        itt+=1
        r = random.randint(0, len(sample)-1)
        print(r)
        print(sample)
        balls.append(Sphere(screen, 5, (250 + (x * 40), 267 + (y * 40) + (x*20)), sample[r]))
        sample.remove(sample[r])
    z-=1
cue = Sphere(screen, 5, [800, 325], -1) # cue ball
cuest = Cue(screen, (270, 340))
table = Table(balls, screen, cue, cuest)
while not gameOver:
    table.draw()
    
    # check edge collision 
    spheresCollided() # after we update the position we check for the collision by calling and handeling the output of the method from the sphere class
    i = []
    for y in range(6):
        i.append( Pocket(30, pocketPos[y], screen))
        i[y].draw()
    for x in balls:
        if not x.gone:
            x.update()
            x.draw()
            for y in i:
                x.pocket(y)
    
    cue.cue()
    cue.update()
    cuest.center = (cue.position.x, cue.position.y)
    cuest.draw()
    for x in balls: # detect collision
        for y in balls:
            if x.position == y.position:
                continue
            dx, dy, dist = x.distance(y)
            if (x.position.x - y.position.x) ** 2 + (x.position.y - y.position.y) ** 2 < x.radius ** 2:
                # check collision
                print("Collided!")
                x.collide(y)
    img = pygame.image.load('Images/ball_3.png')
    pygame.display.set_icon(img)
    cuest.draw()
    Label(font, "Singleplayer Pool", 10, 10, (0,0,50), screen)
    Label(font, "Potential E:" + str(round(cue.force,2)), 800, 10, (0,0,150), screen)
    Label(font, "Angle: " + str(round(abs(cuest.angle),2)), 950, 10, (0,0,150), screen)
    Label(font, "Score: 0", 190, 10, (177,222,130), screen)
    Label(font, "Streak: 0", 280, 10, (177,222,130), screen)


    if pygame.mouse.get_pressed()[0]: # cue enegry application
        if cuest.force == 0:
            table.play(cue.position, time.time()) # start pos, start time
        if cuest.force < 10:
            cuest.force+=.05
            cue.force+=.05
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            gameOver = True
            pygame.quit()
        elif e.type == pygame.MOUSEBUTTONUP:
            table.drop(time.time())
            cue.force = 0
            shot = True
        elif e.type == pygame.MOUSEMOTION and pygame.mouse.get_pos()[1] > 80 :
            if shooting:
                pos = pygame.mouse.get_pos()
                dx = cuest.center[0] - pos[0]
                dy = cuest.center[1] - pos[1]
                cuest.dx = dx
                cuest.dy = dy
                angle = math.degrees(math.atan2(dy, dx))
                cuest.rot(angle) 
    pygame.display.update()
    mainClock.tick(FPS)

pygame.quit()
