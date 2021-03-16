import pygame

pygame.init()

# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
fgColor = pygame.Color("green")

# Draw the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))

pygame.display.flip()