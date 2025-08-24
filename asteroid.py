import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        split_ast_1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        split_ast_2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)

        split_ast_1.velocity = self.velocity.rotate(split_angle) * 1.2
        split_ast_2.velocity = self.velocity.rotate(-split_angle) * 1.2

        self.kill()
        