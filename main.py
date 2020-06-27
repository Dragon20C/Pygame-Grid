import pygame, sys, time
from pygame.locals import *

pygame.init()

screen_width, screen_height = 1024, 768
window = pygame.display.set_mode((screen_width, screen_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
clock = pygame.time.Clock()
blue = 0, 0, 255
black = 0, 0, 0


class Grid:
    def __init__(self):
        self.tile_size = 32
        self.x = screen_width / self.tile_size
        self.y = screen_height / self.tile_size

    def render(self):
        for x in range(0, screen_width, self.tile_size):
            pygame.draw.line(window, black, (x, 0), (x, screen_width), 1)
        for y in range(0, screen_height, self.tile_size):
            pygame.draw.line(window, black, (0, y), (screen_width, y), 1)


grid = Grid()


class Player:
    def __init__(self, x, y, w, h, s):
        self.x, self.y, self.width, self.height, self.speed = x, y, w, h, s
        self.x = self.x * grid.tile_size
        self.y = self.y * grid.tile_size
    def movement(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]:
            self.x -= self.speed
        elif self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]:
            self.x += self.speed
        elif self.keys[pygame.K_UP] or self.keys[pygame.K_w]:
            self.y -= self.speed
        elif self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]:
            self.y += self.speed
        if self.x % 32 != 0:
            self.x += 1
        if self.y % 32 != 0:
            self.y += 1
        if self.x <= 0:
            self.x = 0
        if self.x >= 992:
            self.x = 992
        if self.y <= 0:
            self.y = 0
        if self.y >= 736:
            self.y = 736

    def render(self):
        player.movement()
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, 32, 32))
        print("x " + str(self.x) + " y " + str(self.y))


player = Player(0, 0, 32, 32, 5)


class Walls:
    def __init__(self, x, y, w, h, s):
        self.x, self.y, self.width, self.height, self.speed = x, y, w, h, s
        self.x = self.x * grid.tile_size
        self.y = self.y * grid.tile_size

    def render(self):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 64, 32))


wall = Walls(10, 10, 0, 0, 0)

running = True

while running:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    wall.render()
    grid.render()
    player.render()
    clock.tick(60)
    pygame.display.flip()
