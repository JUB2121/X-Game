import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.SysFont(None, 48)
title_font = pygame.font.SysFont(None, 96)
clock = pygame.time.Clock()
pygame.display.set_caption("X-game")


title_text = title_font.render("X-Game", True, (255, 215, 0))
play_text = font.render("Play", True, (0, 200, 0))
close_text = font.render("Close", True, (220, 0, 0))
title_rect = title_text.get_rect(center = (400, 120))
play_rect = play_text.get_rect(center = (400, 250))
close_rect= play_text.get_rect(center = (400, 350))

def main():
    state = "menu"
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN and state == "menu":
            if play_rect.collidepoint(event.pos):
                state = "playing"
            elif close_rect.collidepoint(event.pos):
                running = False
    
    
        screen.fill((30, 30, 30))

        if state == "menu":
            screen.blit(title_text, title_rect)
            screen.blit(play_text, play_rect)
            screen.blit(close_text, close_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
