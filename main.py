import pygame
import random

pygame.init()

#Initial settings
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Bumper Evasion")

# Initial Player Settings
x = 390
y = 520
p_w = 20
p_h = 20
p_vel = 15

#Initian Vehicle Settings

game_loop = True

while game_loop:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

         #Movemet   
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == ord('w'):
                y-= p_vel
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y+= p_vel
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x-= p_vel
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x+= p_vel

        # Player Rect 
        screen.fill((0,0,0))       
        rect = pygame.draw.rect(screen,(255,255,255),(x,y,p_w,p_h,))
        pygame.display.update()

        #Vehicle Rect
