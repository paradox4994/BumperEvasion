import pygame
import random
import os

pygame.init()

#Initial settings
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Bumper Evasion")
clock = pygame.time.Clock()
FPS = 30

# Assets
truck = pygame.image.load(os.path.join("Assets","tr.png")).convert()

# Initial Player Settings
x = 390
y = 520
p_w = 20
p_h = 20
p_vel = 15

class creator:
    def __init__(self):
        pass
    
    def gen(self):
        veh_list_x = [30]
        veh_list_width = []
        x = 30
        while x < 790:
            width = random.choice([30,40,50,60,70])
            x += width+50
            veh_list_x.append(x)
            veh_list_width.append(width)
        return veh_list_x,veh_list_width
            

#Initian Vehicle Settings
def treq():
    tya = [430, 400, 370, 340]
    ty= random.choice(tya)
    return ty

def draw(xlist,wlist,y,randsub):
    for i in range(len(wlist)): 
        if xlist[i]< 10:
            xlist[i] = 790
        xlist[i] = xlist[i] - randsub
        pygame.draw.rect(screen,(0,255,0),(xlist[i],y,wlist[i],20))

game_loop = True

xlist1,wlist1 = creator().gen()
xlist2,wlist2 = creator().gen()
xlist3,wlist3 = creator().gen()
xlist4,wlist4 = creator().gen()
while game_loop:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    draw(xlist1,wlist1,400,3)
    draw(xlist2,wlist2,370,2)
    draw(xlist3,wlist3,330,1)
    draw(xlist4,wlist4,300,4)
    pygame.display.update()
        
        

        
