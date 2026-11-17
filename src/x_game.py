import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

state = "menu"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and state == "menu":
            screen.fill((30, 30, 30))
    pygame.display.flip()
    clock.tick(60)
pygame.quit
