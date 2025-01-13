import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()

    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        delta_time=clock.tick(60)/1000
        dt+=delta_time
        print(f"Delta Time: {delta_time}")

        for i in updatable:
            i.update(delta_time)
        

        screen.fill((0,0,0))
        for j in drawable:
            j.draw(screen)
            
        pygame.display.flip()
if __name__ == "__main__":
    main()
    