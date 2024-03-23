# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:38:33 2024

@author: marve
"""

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Objects Example")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # Create a surface and rectangle for the player
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set initial position randomly
        self.rect.x = random.randint(0, screen_width - width)
        self.rect.y = random.randint(0, screen_height - height)
        # Set initial speed
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)

    def update(self):
        # Move the player
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Check boundaries and bounce if necessary
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.dy *= -1

# Create instances of Player class
player1 = Player(RED, 50, 50)
player2 = Player(BLUE, 50, 50)

# Group sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Clear the screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
