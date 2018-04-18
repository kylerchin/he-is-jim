#!/usr/bin/python3
import pygame
from displayText import * 
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))

#images
jimVN = pygame.image.load("assets/images/jimVN.png")
deskBG = pygame.image.load("assets/images/deskBG.png")

def gameIntro():
    done = False
    pictureCount = 0
    pictureNumber = 10
    backImage = jimVN
    jimX = 0
    jimY = 50
    sayWhat = 'i hate mondays'
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pictureCount +=1
                    print(pictureCount)
            if pictureCount > pictureNumber:
                #start game
                pass

            if pictureCount == 0:
                backImage = deskBG
                jimX = 0
                jimY = 50
                sayWhat = 'This is Jim. He screwed up and now plays the game "Frogs in the Night" every day.'
            if pictureCount == 1:
                sayWhat = ''

        screen.blit(backImage,(0,0))
        screen.blit(jimVN,(jimX,jimY))
        messageText(sayWhat,50,550,20,screen,255,255,255,"Roboto")
        pygame.display.update()

gameIntro()
