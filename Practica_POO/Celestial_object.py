import pygame
import math


class CelestialObject:

    def __init__(self, image_path=0, distance=0, orbit_speed=0, mass=0):
        self.image = pygame.load(image_path)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.distance = distance
        self.orbit_speed = orbit_speed
        self.mass = mass


    # Metodo de graficar

    def draw(self, screen):
        x = (screen.get_width() // 2) + (self.distance * math.cos(math.radians(self.angle)))
        y = (screen.get_height() // 2) + (self.distance * math.sin(math.radians(self.angle)))
        self.rect.centerx = x
        self.rect.centery = y 
        screen.blit(self.image, self.rect)

