import pygame
pygame.init()

W, H = 600, 400
sc = pygame.display.set_mode((600, 400))    # client surface
pygame.display.set_caption("Epic Window")

clock = pygame.time.Clock()
FPS = 60

BBLUE = (153, 242, 232)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0,0)
BLUE = (0, 0, 255)

# parameters left to right: surface, RGB, xy, W, H
pygame.draw.rect(sc, BBLUE, (10,10, 50, 100), 2) # second parameter is RGB (max 255 for each color)

pygame.draw.line(sc, GREEN, (200, 20), (350, 50), 5)
pygame.draw.aaline(sc, GREEN, (200, 40), (350, 70), 5)

pygame.draw.lines(sc, RED, True, [(200, 80), (250, 80), (300, 200)], 2)
pygame.draw.aalines(sc, RED, True, [(300, 80), (350 , 80), (400, 200)])

pygame.draw.polygon(sc, BBLUE, [[150, 210], [180, 250], [90, 290], [30, 230]])
pygame.draw.polygon(sc, WHITE, [[150, 310], [180, 350], [90, 390], [30, 330]], 1)

pygame.draw.circle(sc, BLUE, (300, 250), 40)
pygame.draw.ellipse(sc, BLUE, (300, 300, 100, 50), 1)

pi = 3.14
pygame.draw.arc(sc, RED, (450, 30, 50, 150), pi, pi*2, 5)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(60)