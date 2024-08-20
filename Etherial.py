import pygame
import sys
from pygame.locals import QUIT

import Scripts.Entity.Entity

Display_width = 1200
Display_height = 800

Surface_width = 1200
Surface_height = 800

display_ratio_x = Display_width / Surface_width
display_ratio_y = Display_height / Surface_height

FPS = 40

pygame.init()
DISPLAY = pygame.display.set_mode((Display_width, Display_height))
pygame.display.set_caption("Etherial")
SURFACE = pygame.Surface((Surface_width, Surface_height))
FPSCLOCK = pygame.time.Clock()


class Player(Scripts.Entity.Entity.Entity):
    def __init__(self, position, size, status):
        super().__init__(position, size, status)


def main():
    PLAYER = Player((0, 0), 50, {"speed": 100})
    CHANNEL = "GAME"

    while True:
        pygame_events = pygame.event.get()
        for pygame_event in pygame_events:
            if pygame_event.type == QUIT:
                pygame.quit()
                sys.exit()

        KEYS = pygame.key.get_pressed()

        if KEYS[pygame.K_w]:
            PLAYER.move(270)
        if KEYS[pygame.K_s]:
            PLAYER.move(90)
        if KEYS[pygame.K_a]:
            PLAYER.move(180)
        if KEYS[pygame.K_d]:
            PLAYER.move(0)

        SURFACE.fill((255, 255, 255))

        pygame.draw.circle(SURFACE, (255, 0, 0), PLAYER.position, PLAYER.size, 5)

        DISPLAY.blit(pygame.transform.scale(SURFACE, (Display_width, Display_height)), (0, 0))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    main()