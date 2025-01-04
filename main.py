# this allows us to use code from
# the open-source pygame library
# throughout this file
#import os
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame

from constants import *

def main():
#  print("Starting asteroids!")
#  print("Screen width:",SCREEN_WIDTH)
#  print("Screen height:",SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while True:

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return
         background_color = (0, 0, 0)
         screen.fill(background_color)
         pygame.display.flip()

         dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
