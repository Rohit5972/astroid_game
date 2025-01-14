import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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
    astroable=pygame.sprite.Group()
    shots=pygame.sprite.Group()

    Asteroid.containers = (astroable, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (updatable, drawable, astroable)
    AsteroidField.containers=(updatable)

    updatable.add(player)
    drawable.add(player)

    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        delta_time=clock.tick(60)/1000
        dt+=delta_time
        print(f"Delta Time: {delta_time}")

        for i in updatable:
            i.update(delta_time)

        for astro in astroable:
            if astro.check_collision(player):
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if astro.check_collision(shot):
                    shot.kill()
                    astro.split()

        screen.fill((0,0,0))
        for j in drawable:
            j.draw(screen)
            
        pygame.display.flip()
if __name__ == "__main__":
    main()
    