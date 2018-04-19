
import pygame
from displayText import * #KYLER DO UR CREDITS
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))
gameBG1 = pygame.image.load("assets/images/stars1BG.png")
gameBG2 = pygame.image.load("assets/images/stars2BG.png")
gameBG3 = pygame.image.load("assets/images/stars3BG.png")
gameBG4 = pygame.image.load("assets/images/stars4BG.png")
jimPic = pygame.image.load("assets/images/jim.png")
ARock = pygame.image.load("assets/images/ARock.png")
BRock = pygame.image.load("assets/images/BRock.png")
CRock = pygame.image.load("assets/images/CRock.png")
ORock = pygame.image.load("assets/images/ORock.png")
HRock = pygame.image.load("assets/images/HRock.png")
jumbi1 = pygame.image.load("assets/images/jumbiBoss.png")
jumbi2 = pygame.image.load("assets/images/jumbiBoss1.png")

#music
pygame.mixer.music.load("assets/music/HopeForADog.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


#objects
def jim(x,y):
	screen.blit(jimPic,(x,y))#Jim

def scapeRock(x,y,type):
	rockSprite = "what rock?"
	if type == "A":
		rockSprite = ARock
	elif type == "B":
		rockSprite = BRock
	elif type == "C":
		rockSprite = CRock
	elif type == "O":
		rockSprite = ORock
	elif type == "H":
		rockSprite = HRock

	screen.blit(rockSprite,(x,y))


def jumbiBoss(x,y,angery):
	if angery == True:
		screen.blit(jumbi2,(x,y))
	else:
		screen.blit(jumbi1,(x,y))



def game():
	done = False
	jimX = 350
	jimY = 470
	spaceRockX = 0
	spaceRockY = 0
	jumbiX = 0
	jumbiY = -1000
	backgroundCount = 0#fail
	enemyKillCount = 0#THIS IS USED FOR COUNTING ENEMIES KILLED. RANDOM ENEMIES YES? WHEN CERTAIN NUMBER OF ENEMIES KILLED, TRIGGER EVENT

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				pass
		# if backgroundCount == 0:
		# 	backImage = gameBG1
		# 	print(backgroundCount)
		# elif backgroundCount == 1:
		# 	backImage = gameBG2
		# 	print(backgroundCount)
		# elif backgroundCount == 2:
		# 	backImage = gameBG3
		# 	print(backgroundCount)
		# elif backgroundCount == 3:
		# 	backImage = gameBG4
		# 	print(backgroundCount)
		# elif backgroundCount == -1:
		# 	backgroundCount =3
		# 	print(backgroundCount)
		# elif backgroundCount == 4:
		# 	backgroundCount=0
		# 	print(backgroundCount)


		#controls for jim
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_LEFT] and jimX>=0:
			jimX-=7
			backgroundCount-=1
		if pressed[pygame.K_RIGHT] and jimX<=740:
			jimX+=7
			backgroundCount+=1

		screen.blit(gameBG3,(0,0))
		jim(jimX,jimY)
		scapeRock(spaceRockX,spaceRockY,"A")
		jumbiBoss(jumbiX,jumbiY,False)
		pygame.display.update()
game()
