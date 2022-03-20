#lesson 1
import pygame
pygame.init()

pygame.display.set_mode((600, 400))

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(60)