import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 120
w = 850
h = 600
jump = False 
v_konec = 320 
vyška = 550
v_dolu = 550
padani = False 
krecek_rychlost = 5
krecek_akcelerace = 0.5
krecek_behind_border = 200
srdce_behind_border= 2500
srdce_rychlost = 7
srdce_soucasna_rychlost = srdce_rychlost
krecek_soucasna_rychlost = krecek_rychlost
hrac_start_zivot = 3
bila = (255, 255, 255)
probiha_kolize = False
konec_kolize = False 


hrac_zivot = hrac_start_zivot

screen =pygame.display.set_mode((w, h))
pygame.display.set_caption("dinosaurus")

zivot_font = pygame.font.SysFont("arialblack", 20)
font = pygame.font.SysFont("arialblack", 20)

bg = pygame.image.load("bg.png")
bg_rect = bg.get_rect()
bg_width = bg.get_width()

hero = pygame.image.load("Troll.png")
hero = pygame.transform.scale(hero,(80,50,))

krecek_enemy = pygame.image.load("pngegg.png")
krecek_rect = krecek_enemy.get_rect()
krecek_rect.x = w + krecek_behind_border
krecek_rect.y = 528

srdce = pygame.image.load("srdce.png")
srdce = pygame.transform.scale(srdce,(50,50,))
srdce_rect = srdce.get_rect()
srdce_rect.x =  w + srdce_behind_border
srdce_rect.y =  556



timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
time_left = 0



while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif udalost.type == timer_event:
            time_left +=1
            
    zivot_text = zivot_font.render(f"Životy: {hrac_zivot}", True, bila)
    zivot_text_rect = zivot_text.get_rect()
    zivot_text_rect.right = w - 20
    zivot_text_rect.top = 15

    timer_text = font.render(f"Čas: {time_left}", True, (255,255,255))
                             
    
    screen.blit(bg, bg_rect)
    screen.blit(hero,(100,vyška))
    screen.blit(krecek_enemy, krecek_rect)
    screen.blit(zivot_text, zivot_text_rect)
    screen.blit(timer_text, (30,15))
    screen.blit(srdce, srdce_rect)
    
    pygame.draw.line(screen, bila, (0,60), (w, 60), 2)
    
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
        probiha_kolize = False
    else:
        krecek_rect.x -= krecek_rychlost
    
    if krecek_rect.x < 100 + 80 and not probiha_kolize and vyška > 470:
        probiha_kolize = True
        hrac_zivot -= 1
        
                      
 
    if srdce_rect.x < 0:
        srdce_rect.x = w + srdce_behind_border
        srdce_rect.y = (556)
        probiha_kolize = False
    else:
        srdce_rect.x -= srdce_rychlost
                   
    if srdce_rect.x < 180 and not probiha_kolize and vyška > 470:
        probiha_kolize = True
        hrac_zivot += 1
    
   

    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()