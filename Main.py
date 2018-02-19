import pygame
import random
import time

DisplayWidth = 800
DisplayHeight = 600

pygame.init()
GameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))
pygame.display.set_caption("Space Invaders")
Clock = pygame.time.Clock()

SmallTextSize = 40
SmallText = pygame.font.Font("PressStart2P-Regular.ttf", SmallTextSize)

LargeTextSize = 100
LargeText = pygame.font.Font("PressStart2P-Regular.ttf", LargeTextSize)

Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)

FPS = 120

Tier1_1 = pygame.image.load("Sprites\\Enemies\\Tier1Invader_Instance1.png")
Tier1_2 = pygame.image.load("Sprites\\Enemies\\Tier1Invader_Instance2.png")
Tier2_1 = pygame.image.load("Sprites\\Enemies\\Tier2Invader_Instance1.png")
Tier2_2 = pygame.image.load("Sprites\\Enemies\\Tier2Invader_Instance2.png")
Tier3_1 = pygame.image.load("Sprites\\Enemies\\Tier3Invader_Instance1.png")
Tier3_2 = pygame.image.load("Sprites\\Enemies\\Tier3Invader_Instance2.png")
MotherShip = pygame.image.load("Sprites\\Enemies\\MotherShip.png")

Player = pygame.image.load("Sprites\\Player\\Player.png")
PlayerFire = pygame.image.load("Sprites\\Player\\PlayerFire.png")

ShieldBlockHP4 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBlockHP4.png")
ShieldBlockHP3 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBlockHP3.png")
ShieldBlockHP2 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBlockHP2.png")
ShieldBlockHP1 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBlockHP1.png")

ShieldTopLeftHP4 = pygame.image.load("Sprites\\ShieldPieces\\ShieldTopLeftHP4.png")
ShieldTopLeftHP3 = pygame.image.load("Sprites\\ShieldPieces\\ShieldTopLeftHP3.png")
ShieldTopLeftHP2 = pygame.image.load("Sprites\\ShieldPieces\\ShieldTopLeftHP2.png")
ShieldTopLeftHP1 = pygame.image.load("Sprites\\ShieldPieces\\ShieldTopLeftHP1.png")

ShieldTopRightHP4 = pygame.image.load("Sprites\\ShieldPieces\\ShieldTopRightHP4.png")
ShieldTopRightHP3 = pygame.image.load("Sprites\\ShieldPieces\\ShieldTopRightHP3.png")
ShieldTopRightHP2 = pygame.image.load("Sprites\\ShieldPieces\\ShieldTopRightHP2.png")
ShieldTopRightHP1 = pygame.image.load("Sprites\\ShieldPieces\\ShieldTopRightHP1.png")

ShieldBottomLeftHP4 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBottomLeftHP4.png")
ShieldBottomLeftHP3 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBottomLeftHP3.png")
ShieldBottomLeftHP2 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBottomLeftHP2.png")
ShieldBottomLeftHP1 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBottomLeftHP1.png")

ShieldBottomRightHP4 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBottomRightHP4.png")
ShieldBottomRightHP3 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBottomRightHP3.png")
ShieldBottomRightHP2 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBottomRightHP2.png")
ShieldBottomRightHP1 = pygame.image.load("Sprites\\ShieldPieces\\ShieldBottomRightHP1.png")

PlayerFireSound = pygame.mixer.Sound("Sound\\PlayerFireSound.wav")
InvaderFireSound = pygame.mixer.Sound("Sound\\InvaderFireSound.wav")
MotherShipSound = pygame.mixer.Sound("Sound\\MotherShipSound.wav")
InvaderKilledSound = pygame.mixer.Sound("Sound\\InvaderKilledSound.wav")
PlayerDeathSound = pygame.mixer.Sound("Sound\\PlayerDeathSound.wav")

BackgroundSound1 = pygame.mixer.Sound("Sound\\BackgroundSound1.wav")
BackgroundSound2 = pygame.mixer.Sound("Sound\\BackgroundSound2.wav")
BackgroundSound3 = pygame.mixer.Sound("Sound\\BackgroundSound3.wav")
BackgroundSound4 = pygame.mixer.Sound("Sound\\BackgroundSound4.wav")

Tier1Width = 24
Tier1Height = 18

Tier2Width = 22
Tier2Height = 16

Tier3Width = 16
Tier3Height = 16

MotherShipWidth = 36
MotherShipHeight = 14

ShieldBlockWidth = 16
ShieldBlockHeight = 16
ShieldTopWidth = 14
ShieldTopHeight = 14
ShieldBottomWidth = 12
SheildBottomHeight = 12

PlayerWidth = 50
PlayerHeight = 26
PlayerFireWidth = 2
PlayerFireHeight = 20

ButtonWidth = 200
ButtonHeight = SmallTextSize + 10

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

        GameDisplay.fill(Black)
        pygame.display.update()

        time.sleep(0.1)

        Clock.tick(FPS)


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
        Clock.tick(FPS)


def GameLoop():
    PlayerX = DisplayWidth / 2 - PlayerWidth / 2
    PlayerY = DisplayHeight - PlayerHeight - 10
    PlayerMovePoints = 0

    PlayerFireX = -100
    PlayerFireY = -100
    PlayerFireSpeed = -5
    PlayerBulletsX = [PlayerFireX]
    PlayerBulletsY = [PlayerFireY]
    PlayerBullets = [PlayerBulletsX, PlayerBulletsY]
    ShotFired = False

    InvaderX = []
    InvaderY = []
    Tier = []
    Invaders = [InvaderX, InvaderY, Tier]

    InvaderNum = 100

    Type = 0
    SoundType = 0
    InvaderMoveType = 0
    InvaderDir = "Right"
    InvaderSpeed = Tier3Width
    Moved = 6

    ##  Invader Initialisation
    for i in range(InvaderNum):

        if 0 <= i < 20:
            InvaderY.append(40)
            if i == 0:
                InvaderX.append(100)
            else:
                InvaderX.append(InvaderX[i - 1] + 30)

            Tier.append(3)

        elif 20 <= i < 40:
            InvaderY.append(80)
            if i == 20:
                InvaderX.append(100)
            else:
                InvaderX.append(InvaderX[i - 1] + 30)

            Tier.append(2)

        elif 40 <= i < 60:
            InvaderY.append(120)
            if i == 40:
                InvaderX.append(100)
            else:
                InvaderX.append(InvaderX[i - 1] + 30)

            Tier.append(2)

        elif 60 <= i < 80:
            InvaderY.append(160)
            if i == 60:
                InvaderX.append(100)
            else:
                InvaderX.append(InvaderX[i - 1] + 30)

            Tier.append(1)

        elif 80 <= i <= 100:
            InvaderY.append(200)
            if i == 80:
                InvaderX.append(100)
            else:
                InvaderX.append(InvaderX[i - 1] + 30)

            Tier.append(1)

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

                ##  Bullet Gen
                if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                    if not ShotFired:
                        PlayerFireX = PlayerX + PlayerWidth / 2 - 1
                        PlayerFireY = PlayerY + 2 - PlayerFireHeight
                        PlayerBullets[0].append(PlayerFireX)
                        PlayerBullets[1].append(PlayerFireY)
                        ShotFired = True
                        pygame.mixer.Sound.play(PlayerFireSound)

                if event.key == pygame.K_p:
                    Paused = True
                    PauseScreen()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    PlayerMovePoints = 0

        ##  Bounce
        if PlayerX <= 20:
            PlayerX = 20

        elif PlayerX >= DisplayWidth - PlayerWidth - 20:
            PlayerX = DisplayWidth - PlayerWidth - 20

        PlayerX += PlayerMovePoints
        GameDisplay.fill(Black)
        GameDisplay.blit(Player, (PlayerX, PlayerY))

        ##  Bullet out of bounds
        for i in range(len(PlayerBullets[1])):
            try:

                GameDisplay.blit(PlayerFire, (PlayerBulletsX[i], PlayerBulletsY[i]))
                PlayerBulletsY[i] += PlayerFireSpeed

                if PlayerBulletsY[i] < 0 - PlayerFireHeight:
                    ShotFired = False
                    PlayerBulletsY.pop(i)
                    PlayerBulletsX.pop(i)

            except IndexError:
                pass

        ##  Invader Gen
        for i in range(InvaderNum):
            try:
                if Tier[i] == 3 and Type < FPS:
                    GameDisplay.blit(Tier3_1, (Invaders[0][i], Invaders[1][i]))
                elif Tier[i] == 3 and Type < FPS * 2:
                    GameDisplay.blit(Tier3_2, (Invaders[0][i], Invaders[1][i]))

                elif Tier[i] == 2 and Type < FPS:
                    GameDisplay.blit(Tier2_1, (Invaders[0][i], Invaders[1][i]))
                elif Tier[i] == 2 and Type < FPS * 2:
                    GameDisplay.blit(Tier2_2, (Invaders[0][i], Invaders[1][i]))

                elif Tier[i] == 1 and Type < FPS:
                    GameDisplay.blit(Tier1_1, (Invaders[0][i], Invaders[1][i]))
                elif Tier[i] == 1 and Type < FPS * 2:
                    GameDisplay.blit(Tier1_2, (Invaders[0][i], Invaders[1][i]))

            except IndexError:
                pass

        ##  Moves Invaders
        InvaderMoveType += 1
        if InvaderMoveType > FPS:
            InvaderMoveType = 0

            if InvaderDir == "Right":
                if Moved < 12:
                    for i in range(len(Invaders[0])):
                        Invaders[0][i] += InvaderSpeed
                    Moved += 1
                else:
                    InvaderDir = "Left"
                    Moved = 0
                    for x in range(len(Invaders[1])):
                        Invaders[1][x] += Tier1Height + 10

            elif InvaderDir == "Left":
                if Moved < 12:
                    for i in range(len(Invaders[0])):
                        Invaders[0][i] -= InvaderSpeed
                    Moved += 1
                else:
                    InvaderDir = "Right"
                    Moved = 0
                    for x in range(len(Invaders[1])):
                        Invaders[1][x] += Tier1Height + 10

        ##  Collision detection
        for i in range(len(Invaders[0])):
            for n in range(len(PlayerBullets[0])):
                try:

                    if InvaderX[i] < PlayerBulletsX[n] < InvaderX[i] + Tier1Width:
                        if PlayerBulletsY[n] <= InvaderY[i] + Tier1Height:
                            InvaderX.pop(i)
                            InvaderY.pop(i)
                            Tier.pop(i)
                            PlayerBulletsX.pop(n)
                            PlayerBulletsY.pop(n)
                            ShotFired = False
                            InvaderNum -= 1
                            pygame.mixer.Sound.play(InvaderKilledSound)

                except IndexError:
                    pass

        Type += 1
        if Type > FPS * 2:
            Type = 0

        SoundType += 1
        if SoundType > FPS * 4:
            SoundType = 0

        elif SoundType == FPS:
            pygame.mixer.Sound.play(BackgroundSound4)
        elif SoundType == FPS * 2:
            pygame.mixer.Sound.play(BackgroundSound2)
        elif SoundType == FPS * 3:
            pygame.mixer.Sound.play(BackgroundSound1)
        elif SoundType == FPS * 4:
            pygame.mixer.Sound.play(BackgroundSound3)

        pygame.display.update()
        Clock.tick(FPS)


MainMenu()
