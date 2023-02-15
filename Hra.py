import pygame
import math
import sys
import random
pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("dinosaurus")


bg = pygame.image.load("bg.png").convert()
bg_width = bg.get_width()

hero = pygame.image.load("Troll.png")
hero = pygame.transform.scale(hero,(80,50,))

scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1

run = True
while run:

  clock.tick(FPS)

  for i in range(0, tiles):
    screen.blit(bg, (i * bg_width + scroll, 0))
    
  scroll -= 5

  if abs(scroll) > bg_width:
    scroll = 0

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      
  screen.blit(hero,(300,550))


  pygame.display.update()

pygame.quit()
    
