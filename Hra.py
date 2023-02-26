import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
FPS = 60
w = 850
h = 600

screen =pygame.display.set_mode((w, h))
pygame.display.set_caption("dinosaurus")

bg = pygame.image.load("bg.png")
bg_rect = bg.get_rect()
bg_width = bg.get_width()

hero = pygame.image.load("Troll.png")
hero = pygame.transform.scale(hero,(80,50,))


while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.blit(bg, bg_rect)
    screen.blit(hero,(100,550))
    
      
      
      
      

    pygame.display.update()
    
pygame.quit()
    
