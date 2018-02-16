import random
import time

from Objs import *

DisplayWidth = 800
DisplayHeight = 600

pygame.init()
GameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))
pygame.display.set_caption("Space Invaders")
Clock = pygame.time.Clock()

Paused = False

def TextObjs(Text, Font, Colour):
    TextSurface = Font.render(Text, True, Colour)
    return TextSurface, TextSurface.get_rect()  ##  Returns text and the rectangle around it


def ButtonGen(Text, Font, ButtonX, ButtonY, InactiveColour, ActiveColour, Function):
    Mouse = pygame.mouse.get_pos()
    Click = pygame.mouse.get_pressed()

    if ButtonX < Mouse[0] < ButtonX + ButtonWidth and ButtonY < Mouse[1] < ButtonY + ButtonHeight:
        TextSurf, TextRect = TextObjs(Text, Font, ActiveColour)
        if Click[0] == 1:
            Function()

    else:
        TextSurf, TextRect = TextObjs(Text, Font, InactiveColour)

    pygame.draw.rect(GameDisplay, Black, [ButtonX, ButtonY, ButtonWidth, ButtonHeight])
    TextRect.center = (ButtonX + (ButtonWidth / 2), ButtonY + (ButtonHeight / 2))
    GameDisplay.blit(TextSurf, TextRect)


def InvaderGen():
    pass

def EnemyFireGen():
    pass


def PlayerFireGen():
    pass


def WriteText(Text, Font, Colour, Location):
    TextSurf, TextRect = TextObjs(Text, Font, Colour)
    TextRect.center = Location
    GameDisplay.blit(TextSurf, TextRect)


def PauseScreen():
    TextSurf, TextRect = TextObjs("Paused", SmallText, White)  ##  Surface is the text Rect is the rectangle around the text when generated
    TextRect.center = (DisplayWidth / 2, DisplayHeight / 2)

    while Paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    UnPause()

        GameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()

        time.sleep(0.1)

        pygame.draw.rect(GameDisplay, Black, TextRect)
        pygame.display.update()

        time.sleep(0.1)

        Clock.tick(60)


def UnPause():
    pygame.mixer.music.unpause()

    global Paused
    Paused = False


def Exit():
    pygame.quit()
    quit()


def MainMenu():
    Menu = True

    while Menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit()

        WriteText("Space", LargeText, White, (DisplayWidth / 2, LargeTextSize / 2 + 10))
        WriteText("Invaders", LargeText, White, (DisplayWidth / 2, LargeTextSize * 1.5 + 10))

        ButtonGen("Play", SmallText, DisplayWidth / 2 - ButtonWidth / 2, DisplayHeight / 2, White, Green, GameLoop)
        pygame.display.update()
        Clock.tick(60)


def GameLoop():
    PlayerX = DisplayWidth / 2 - PlayerWidth / 2
    PlayerY = DisplayHeight - PlayerHeight - 10
    PlayerMovePoints = 0

    global Paused

    GameExit = False

    while not GameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    PlayerMovePoints = -5

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    PlayerMovePoints = 5

                if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                    PlayerFireGen()

                if event.key == pygame.K_p:
                    Paused = True
                    PauseScreen()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    PlayerMovePoints = 0

        if PlayerX <= 20:
            PlayerX = 20

        elif PlayerX >= DisplayWidth - PlayerWidth - 20:
            PlayerX = DisplayWidth - PlayerWidth - 20

        PlayerX += PlayerMovePoints
        GameDisplay.fill(Black)
        GameDisplay.blit(Player, (PlayerX, PlayerY))

        pygame.display.update()
        Clock.tick(60)


MainMenu()
