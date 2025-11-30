import pygame
import random
import time
pygame.font.init()
 

WIDTH, HEIGHT = 1000, 630
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space dodge")

BG = pygame.transform.scale(pygame.image.load("background_image.jpeg"), (WIDTH, HEIGHT))
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40

PLAYER_VEL = 5

FONT = pygame.font.SysFont("Comicsans", 31)

def draw(player, elapsed_time):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"time: {round(elapsed_time)}s", 1, "white")

    pygame.draw.rect(WIN, (255, 0, 0), player)

    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_HEIGHT, PLAYER_WIDTH)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time =  0

    while run:
        clock.tick(60)
        elapsed_time = time.time - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL

        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL



        draw(player, elapsed_time)
    pygame.quit()

if __name__ == "__main__":
    main()
