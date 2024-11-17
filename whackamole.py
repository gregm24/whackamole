import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        grid_size = (20, 16)  
        cell_size = 32 
        mole = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    mole_rect = mole_image.get_rect(topleft = mole)
                    if mole_rect.collidepoint(mouse_pos):
                        mole = (random.randrange(grid_size[0]) * cell_size, random.randrange(grid_size[1]) * cell_size)

            screen.fill("light green")

            for i in range(20):
                pygame.draw.line(screen, "purple", (i * 32, 0), (i*32, 512))
            for i in range(16):
                pygame.draw.line(screen, "purple", (0, i * 32), (640, i * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
