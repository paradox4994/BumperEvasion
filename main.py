import pygame
import random
import os

pygame.init()

#Initial settings
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Bumper Evasion")
clock = pygame.time.Clock()
FPS = 30
game_loop = True
red = (255,0,0)
lblue = (102,255,255)
level = 1
espeed = 4

# Assets
truckr = pygame.image.load(os.path.join("Assets","tr.png")).convert_alpha()
truckl = pygame.image.load(os.path.join("Assets","tl.png")).convert_alpha()
p_spr = pygame.image.load(os.path.join("Assets","player.png")).convert_alpha()

# Initial Player Settings
class Player:
    def __init__(self):
        self.x = 390
        self.y = 520
        self.p_w = 20
        self.p_h = 20
        self.p_vel = 15

    def draw(self):
        screen.blit(p_spr,(self.x,self.y))
        self.hitboxp = (self.x,self.y,self.p_w,self.p_h)
        self.prect = pygame.draw.rect(screen,(255,0,255),self.hitboxp,2)
        

class enemy:
    def __init__(self,y,w):
        self.enemy_height = 20
        self.enemy_width = w
        self.y = y
        self.x = random.randint(10,780)

    def drawr(self,screen):
        if self.x < -80:
            self.x = 780
        screen.blit(truckr,(self.x,self.y))
        self.x = self.x - espeed
        self.hitboxr = (self.x,self.y,self.enemy_width,self.enemy_height)
        self.rectr = pygame.draw.rect(screen,(255,0,255),self.hitboxr,1)

    def drawl(self,screen):
        if self.x > 780:
            self.x = 10
        screen.blit(truckl,(self.x,self.y))
        self.x = self.x + espeed
        self.hitboxl = (self.x,self.y,self.enemy_width,self.enemy_height)
        self.rectl = pygame.draw.rect(screen,(255,0,255),self.hitboxl,1)


# Main Code

font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 18)
text = font.render('Level:', True, red, lblue)
texth = font.render('Bumper Evasion', True, red, lblue)
textg = font2.render('github.com/paradox4994', True, red, lblue)


e1 = enemy(430,70)
e2 = enemy(400,70)
e3 = enemy(370,70)
e4 = enemy(340,70)
e5 = enemy(310,70)
e6 = enemy(280,70)
e7 = enemy(250,70)
e8 = enemy(220,70)
e9 = enemy(190,70)
e10 = enemy(160,70)
e11 = enemy(130,70)
player = Player()

def collide(rectl):
    if rectl.colliderect(player.prect):
        player.x = 390
        player.y = 520
    

while game_loop:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x-=player.p_vel
            if event.key == pygame.K_RIGHT:
                player.x+=player.p_vel
            if event.key == pygame.K_UP:
                player.y-=player.p_vel
            if event.key == pygame.K_DOWN:
                player.y+=player.p_vel
    screen.fill((102,255,255))
    winrect = pygame.draw.rect(screen,(0,255,0),(10,10,780,110),5)
    pygame.draw.rect(screen,(0,100,0),(10,120,780,10))
    screen.blit(text,(50,50,50,50))
    screen.blit(texth,(300,50,50,50))
    screen.blit(textg,(580,580,80,80))
    e1.drawl(screen)
    e2.drawr(screen)
    e3.drawl(screen)
    e4.drawr(screen)
    e5.drawr(screen)
    e6.drawl(screen)
    e7.drawl(screen)
    e8.drawr(screen)
    e9.drawl(screen)
    e10.drawr(screen)
    e11.drawl(screen)
    player.draw()
    collide(e1.rectl)
    collide(e2.rectr)
    collide(e3.rectl)
    collide(e4.rectr)
    collide(e5.rectr)
    collide(e6.rectl)
    collide(e7.rectl)
    collide(e8.rectr)
    collide(e9.rectl)
    collide(e10.rectr)
    collide(e11.rectl)
    if winrect.colliderect(player.prect):
        player.x = 390
        player.y = 520
        level += 1
        espeed += 1
    textl = font.render(str(level), True, red, lblue)
    screen.blit(textl,(150,50,50,50))
        

    
    pygame.display.update()
        
        

        
