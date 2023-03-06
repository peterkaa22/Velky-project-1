import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
FPS = 120
w = 850
h = 600
jump = False 
v_konec = 410  
vyška = 550
v_dolu = 550
padani = False 
krecek_rychlost = 5
krecek_akcelerace = 0.5
krecek_behind_border = 100
krecek_soucasna_rychlost = krecek_rychlost




screen =pygame.display.set_mode((w, h))
pygame.display.set_caption("dinosaurus")

bg = pygame.image.load("bg.png")
bg_rect = bg.get_rect()
bg_width = bg.get_width()

hero = pygame.image.load("Troll.png")
hero = pygame.transform.scale(hero,(80,50,))

krecek_enemy = pygame.image.load("pngegg.png")
krecek_rect = krecek_enemy.get_rect()
krecek_rect.x = w + krecek_behind_border
krecek_rect.y = 568

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.blit(bg, bg_rect)
    screen.blit(hero,(100,vyška))
    screen.blit(krecek_enemy, krecek_rect)
    
    
    klavesa = pygame.key.get_pressed()
    if klavesa[pygame.K_SPACE] and not (jump or padani):
        jump = True
    
    if jump:
        vyška = vyška-5

    if vyška < v_konec:
        jump = False
        padani = True 
    
    if padani:
        vyška = vyška+5
        
        
    if v_dolu < vyška:
        padani = False 

    if krecek_rect.x < 0:
        krecek_rect.x = w + krecek_behind_border
        krecek_rect.y = (568 - 40)
        
    else:
        krecek_rect.x -= krecek_rychlost
                    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
    
