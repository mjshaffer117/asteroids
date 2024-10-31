import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # To be overwritten by sub-classes
        pass

    def update(self, dt):
        # To be overwritten by sub-classes
        pass

    def collision_check(self, opposing):
        distance = pygame.Vector2.distance_to(self.position, opposing.position)
        return distance <= self.radius + opposing.radius
    
    
    