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

# Assets
truckr = pygame.image.load(os.path.join("Assets","tr.png")).convert_alpha()
truckl = pygame.image.load(os.path.join("Assets","tl.png")).convert_alpha()
p_spr = pygame.image.load(os.path.join("Assets","player.png")).convert_alpha()
11
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

class enemy:
    def __init__(self,y,w):
        self.enemy_height = 20
        self.enemy_width = w
        self.y = y
        self.x = random.randint(10,780)

    def drawr(self,screen):
        if self.x < 10:
            self.x = 780
        screen.blit(truckr,(self.x,self.y))
        #pygame.draw.rect(screen,(255,0,255),(self.x,self.y,self.enemy_width,self.enemy_height))
        self.x = self.x - 4
    def drawl(self,screen):
        if self.x > 780:
            self.x = 10
        screen.blit(truckl,(self.x,self.y))
        #pygame.draw.rect(screen,(255,0,255),(self.x,self.y,self.enemy_width,self.enemy_height))
        self.x = self.x + 4

# Main Code

e11 = enemy(400,70)
e12 = enemy(380,70)
e13 = enemy(360,70)
e14 = enemy(340,70)
e15 = enemy(320,70)
e16 = enemy(300,70)
e17 = enemy(280,70)
e18 = enemy(260,70)
e19 = enemy(240,70)
player = Player()

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
    e11.drawl(screen)
    e12.drawr(screen)
    e13.drawl(screen)
    e14.drawr(screen)
    e15.drawr(screen)
    e16.drawl(screen)
    e17.drawl(screen)
    e18.drawr(screen)
    e19.drawl(screen)
    player.draw()

    
    pygame.display.update()
        
        

        
