# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:00:51 2024

@author: marve
"""

import pygame
""" sprite.py

"""

pygame.init()

screen = pygame.display.set_mode((640, 480))

class game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # set up the image
        self.image = pygame.image.load("game.png")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        #create the corresponding rect
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 240
        
        #create the ability to move
        self.dx = 5
        self.dy = 3
        
        
    def update(self):

        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        
        # check bounds
        if self.rect.right > screen.get_width():
            self.rect.left = 0
        if self.rect.bottom > screen.get_height():
            self.rect.top = 0

class BSU(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # set up the image
        self.image = pygame.image.load("BSU.jpg")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 20))

        #create the corresponding rect
        self.rect = self.image.get_rect()
        self.rect.centerx = 350
        self.rect.centery = 200
        
        #create the ability to move
        self.dx = 3
        self.dy = 5
        
        
    def update(self):

        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        
        # check bounds
        if self.rect.right > screen.get_width():
            self.rect.left = 0
        if self.rect.bottom > screen.get_height():
            self.rect.top = 5
            
def main():
    
    #set up screen
    pygame.display.set_caption("Basic sprite demo")
    background = pygame.image.load("state.jpg")
    background.convert_alpha() 
    background = pygame.transform.scale(background, (screen.get_size()))
    screen.blit(background, (1, 1))
    
    # instantiate game
    Game = game()
    Img = BSU()
    allSprites = pygame.sprite.Group(Game, Img)
    
    # set up timing
    clock = pygame.time.Clock()
    keepGoing = True
    while(keepGoing):
        clock.tick(30)
        
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        # clear and redraw sprites
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
    pygame.quit()   