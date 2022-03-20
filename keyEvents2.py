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

x = W // 2
y = H // 2
Xspeed = 5
Yspeed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= Xspeed
    elif keys[pygame.K_RIGHT]:
        x += Xspeed
    elif keys[pygame.K_UP]:
        y -= Yspeed
    elif keys[pygame.K_DOWN]:
        y += Yspeed
    

    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)
