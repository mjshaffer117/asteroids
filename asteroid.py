import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        def create_new_asteroid(self, velocity, radius):
            asteroid = Asteroid(self.position.x, self.position.y, radius)
            asteroid.velocity = velocity * ASTEROID_SPLIT_SPEED

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            create_new_asteroid(self, self.velocity.rotate(angle), new_radius)
            create_new_asteroid(self, self.velocity.rotate(-angle), new_radius)
    