import pygame
import sys
import random
from platforms import Platforms
from pygame.locals import*
from player import Player
pygame.init()
screen_info=pygame.display.Info()
size = (width,height)=(int(screen_info.current_w),
int(screen_info.current_h))
screen= pygame.display.set_mode(size)
clock = pygame.time.Clock()

sprite_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()
player = ''

def getact():
  p1acts = {}
  p1acts['p1_jump']= pygame.image.load("images/p1_jump.png").convert()
  p1acts['p1_jump'].set_colorkey((0,0,0))
  p1acts['p1_hurt']= pygame.image.load("images/p1_hurt.png").convert()
  p1acts['p1_hurt'].set_colorkey((0,0,0))
  return p1acts
  
def init(p1acts):
  global player
  for i in range(height//100):
    for j in range(width//410):
      plat = Platforms((random.randint(5, (width - 50) // 10)* 10, 120 * i), 'images/grassHalf.png', 70, 40)
      platforms.add(plat)
  player = Player((platforms.sprites()[-1].rect.centerx,platforms.sprites()[-1].rect.centery-300), p1acts)
  sprite_list.add(player)
  
def main():
  global player
  p1acts = getact()
  init(p1acts)
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT: 
        sys.exit()
      if event.type==pygame.KEYDOWN: #if any key is pressed
        if event.key==pygame.K_f:
          pygame.display.set_mode(size,FULLSCREEN)
        if event.key==pygame.K_ESCAPE:
          pygame.display.set_mode(size)
    screen.fill((0,0,100))
    platforms.draw(screen)
    sprite_list.draw(screen)
    pygame.display.flip()
if __name__=="__main__":
  main()