import pygame
import random as r

GRAVITY = -90.8


class Entity:
    def update(self, dt):
        pass

    def draw(self, screen):
        raise NotImplementedError


class Circle(Entity):
    def __init__(self, pos, radius, color):
        self.pos = pygame.Vector2(pos)
        self.v = pygame.Vector2(0, 0)
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def update(self, dt):
        self.v.y += GRAVITY * dt
        self.pos.y -= self.v.y * dt


def random_rgb():
    c1 = r.random() * 255
    c2 = r.random() * 255
    c3 = r.random() * 255
    return pygame.Color(c1, c2, c3)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

ENTITIES = []

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    mouse = pygame.mouse.get_pressed(3)

    if mouse[0]:
        ENTITIES.append(
            Circle(pygame.mouse.get_pos(), 4, random_rgb())
        )

    for ent in ENTITIES:
        ent.draw(screen)
        ent.update(dt)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
