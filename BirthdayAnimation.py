import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Birthday Greeting Card')

img = pygame.image.load('background1.png')
image = pygame.transform.scale(img,(WIDTH,HEIGHT))

while True:
    img = pygame.image.load('background1.png')
    image = pygame.transform.scale(img,(WIDTH,HEIGHT))
    font = pygame.font.SysFont('Times New Roman',72)
    text = font.render('Happy',True,(0,0,0))
    text2 = font.render('Birthday',True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(210,180))
    display_surface.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)
    img = pygame.image.load('background2.png')
    image = pygame.transform.scale(img,(WIDTH,HEIGHT))
    font = pygame.font.SysFont('Times New Roman',40)
    text = font.render('Wish you well for the next year',True,(0,0,0))
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(50,50))
    pygame.display.update()
    time.sleep(2)
    img = pygame.image.load('background3.png')
    image = pygame.transform.scale(img,(WIDTH,HEIGHT))
    display_surface.blit(image,(0,0))
    pygame.display.update()
    time.sleep(2)
