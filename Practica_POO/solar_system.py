# Clase Main

from planeta import Planet
from asteroid import Asteroid
from star import Star
import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sistea solar")

sun = Star(image_path="sol.png", mass=2000, nucleo_status= "Active")
mercure = Planet(image_path="mercure.png", distance=100,orbit_speed=2,mass=2000, nucleo_status= "Inactive")
mars = Planet(image_path="marte.png", distance=180,orbit_speed=2,mass=250, nucleo_status= "Inactive")
asteroid = Asteroid(image_path="asteroid.png", distance=210,orbit_speed=2,mass=250)

background_image = pygame.image.load("fondo.png").convert
background_rect = background_image.get_rect()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, background_rect)
    sun.draw(screen)
    mercure.draw(screen)
    mars.draw(screen)
    asteroid.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()