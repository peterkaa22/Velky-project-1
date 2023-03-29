import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 120
w = 850
h = 600
jump = False 
v_konec = 330
vyška = 550
v_dolu = 550
padani = False 
krecek_rychlost = 5
krecek_akcelerace = 0.5
krecek_behind_border = 200
srdce_behind_border= 2500
srdce_rychlost = 5
srdce_soucasna_rychlost = srdce_rychlost
krecek_soucasna_rychlost = krecek_rychlost
hrac_start_zivot = 3
bila = (255, 255, 255)
probiha_kolize = False
konec_kolize = False 
konec_hry = False 


hrac_zivot = hrac_start_zivot

screen =pygame.display.set_mode((w, h))
pygame.display.set_caption("dinosaurus")

zivot_font = pygame.font.SysFont("arialblack", 20)
font = pygame.font.SysFont("arialblack", 20)
konec_font = pygame.font.SysFont("arialblack", 40)
restart_font = pygame.font.SysFont("arialblack", 20)

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

voda = pygame.image.load("voda.png")
voda = pygame.transform.scale(voda,(1000,700))
voda_rect = voda.get_rect()
voda_rect.x = 100
voda_rect.y = 310

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
    
    if hrac_zivot < 1:
            konec_hry = True
            
    klavesa = pygame.key.get_pressed()
    if klavesa[pygame.K_LCTRL] and konec_hry:
        konec_hry = False  
        krecek_rychlost = 5
        hrac_zivot = 3
        time_left = 0
        krecek_rect.x = w + krecek_behind_border
        krecek_rect.y = 528
        srdce_rect.x = w + srdce_behind_border
        srdce_rect.y = 556
    
    if konec_hry == False:
                
        zivot_text = zivot_font.render(f"Životy: {hrac_zivot}", True, bila)
        zivot_text_rect = zivot_text.get_rect()
        zivot_text_rect.right = w - 20
        zivot_text_rect.top = 15

        timer_text = font.render(f"Čas:{time_left}", True, (255,255,255))
        
        konec_text = konec_font.render("Zemřel jsi!" , True, (255, 0, 0))                         
        
        restart_text = restart_font.render("Zmáčkni CTRL pro Restart" ,True, (255, 255, 255))
        
        screen.blit(bg, bg_rect)
        screen.blit(hero,(100,vyška))
        screen.blit(krecek_enemy, krecek_rect)
        screen.blit(zivot_text, zivot_text_rect)
        screen.blit(timer_text, (30,15))
        screen.blit(srdce, srdce_rect)
        screen.blit(voda, voda_rect) 
        
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
            krecek_rect.x = w + krecek_behind_border
            
                          
     
        if srdce_rect.x < 0:
            srdce_rect.x = w + srdce_behind_border
            srdce_rect.y = (556)
            probiha_kolize = False
        else:
            srdce_rect.x -= srdce_rychlost
                       
        if srdce_rect.x < 180 and not probiha_kolize and vyška > 470:
            probiha_kolize = True
            hrac_zivot += 1
        
        if krecek_rect.x < 600:
            krecek_rychlost = 2
        
        if krecek_rect.x < 500:
            krecek_rychlost = 5
        
        
        
        
        
        if time_left > 10:
            krecek_rychlost = 6
        if krecek_rect.x < 600:
            krecek_rychlost = 2
        if krecek_rect.x < 450:
            krecek_rychlost = 6
        
            
            
        if time_left > 20:
            krecek_rychlost = 8
            if krecek_rect.x < 600:
                krecek_rychlost = 2
            if krecek_rect.x < 450:
                krecek_rychlost = 8
        
        if time_left > 30:
            krecek_rychlost = 9
            if krecek_rect.x < 600:
                krecek_rychlost = 3
            if krecek_rect.x < 450:
                krecek_rychlost = 9
         
        if time_left > 40:
            krecek_rychlost = 10
            if krecek_rect.x < 600:
                krecek_rychlost = 3
            if krecek_rect.x < 450:
                krecek_rychlost = 10
        
        if time_left > 50:
            krecek_rychlost = 11
            if krecek_rect.x < 600:
                krecek_rychlost = 4
            if krecek_rect.x < 450:
                krecek_rychlost = 11
            
        if time_left > 60:
            krecek_rychlost = 12
            if krecek_rect.x < 600:
                krecek_rychlost = 4
            if krecek_rect.x < 450:
                krecek_rychlost = 12
                
        if time_left > 70:
            krecek_rychlost = 13
            if krecek_rect.x < 600:
                krecek_rychlost = 5
            if krecek_rect.x < 450:
                krecek_rychlost = 13
                
        if time_left > 80:
            krecek_rychlost = 14
            if krecek_rect.x < 600:
                krecek_rychlost = 5
            if krecek_rect.x < 450:
                krecek_rychlost = 14
                
        if time_left > 90:
            krecek_rychlost = 15
            if krecek_rect.x < 600:
                krecek_rychlost = 6
            if krecek_rect.x < 450:
                krecek_rychlost = 15

        if time_left > 100:
            krecek_rychlost = 16
            if krecek_rect.x < 600:
                krecek_rychlost = 6
            if krecek_rect.x < 450:
                krecek_rychlost = 16
            
        if time_left > 110:
            krecek_rychlost = 17
            if krecek_rect.x < 600:
                krecek_rychlost = 7
            if krecek_rect.x < 450:
                krecek_rychlost = 17
        
       
        
        if hrac_zivot < 1:
            screen.blit(konec_text, (315,300))
            screen.blit(restart_text, (285, 360))
        
                
            
                         
    
            
            
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()

