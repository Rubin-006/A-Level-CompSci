import pygame
import matplotlib.pyplot as plt


WIDTH, HEIGHT = 1250 , 800
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Creates Window
pygame.display.set_caption("Doqtor") # Names window Doqtor


FPS = 30
clock = pygame.time.Clock()

while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()