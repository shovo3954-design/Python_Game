import pygame
import random
import time
 

WIDTH, HEIGHT = 1000, 630
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space dodge")

BG = pygame.transform.scale(pygame.image.load("background_image.jpeg"), (WIDTH, HEIGHT))
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40

PLAYER_VEL = 5

def draw(player):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, (255, 0, 0), player)

    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_HEIGHT, PLAYER_WIDTH)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL

        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL



        draw(player)
    pygame.quit()

if __name__ == "__main__":
    main()
