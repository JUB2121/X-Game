import random
import pygame

pygame.init()

width, height = 800, 600
Mouse_radius = 10
radius = 20


screen = pygame.display.set_mode((800,600))
font = pygame.font.SysFont(None, 48)
title_font = pygame.font.SysFont(None, 96)
x_font = pygame.font.SysFont(None, 120)
clock = pygame.time.Clock()
pygame.display.set_caption("X-game")


title_text = title_font.render("X-Game", True, (255, 215, 0))
play_text = font.render("Play", True, (0, 200, 0))
close_text = font.render("Close", True, (220, 0, 0))
title_rect = title_text.get_rect(center = (400, 120))
play_rect = play_text.get_rect(center = (400, 250))
close_rect = close_text.get_rect(center = (400, 350))


x_text = x_font.render("X", True, (255, 255, 255))
win1_text = font.render(
     "Level 1 is complete! Click for Level 2", True, (255, 255, 255))
win1_rect = win1_text.get_rect(center=(400, 300))
win2_text = font.render(
     "Level 2 is complete!", True, (255, 255,255))
win2_text = win2_text.get_rect(center=(400,300))

def rand_x():
    rect = x_text.get_rect()
    rect.center = (random.randint(80, 720), random.randint(80, 520))
    return rect

def main():
    state = "menu"
    running = True
    x_rect = rand_x()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if state == "menu":
                         if play_rect.collidepoint(event.pos):
                              x_rect = rand_x()
                              state = "Level 1"
                         elif close_rect.collidepoint(event.pos):
                            running = False
                    elif state == "Level 1":
                        if x_rect.collidepoint(event.pos):
                              state = "Level 1 Complete!"
                    elif state == "Level 1 Complete!":
                         state = "menu"
    

    
    
        screen.fill((30, 30, 30))
        if state == "menu":
            screen.blit(title_text, title_rect)
            screen.blit(play_text, play_rect)
            screen.blit(close_text, close_rect)
        elif state == "Level 1":
            screen.blit(x_text, x_rect)
        elif state == "Level 1 Complete!":
            screen.blit(win1_text, win1_rect)
             
             
        
        mouse_position = pygame.mouse.get_pos()
        pygame.draw.circle(screen, 'red', mouse_position, 10)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
