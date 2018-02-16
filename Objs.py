import pygame

SmallTextSize = 40
SmallText = pygame.font.Font("PressStart2P-Regular.ttf", SmallTextSize)

LargeTextSize = 100
LargeText = pygame.font.Font("PressStart2P-Regular.ttf", LargeTextSize)

Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)

Tier1_1 = pygame.image.load("Sprites\\Enemies\\Tier1Invader_Instance1.png")
Tier1_2 = pygame.image.load("Sprites\\Enemies\\Tier1Invader_Instance2.png")
Tier2_1 = pygame.image.load("Sprites\\Enemies\\Tier2Invader_Instance1.png")
Tier2_2 = pygame.image.load("Sprites\\Enemies\\Tier2Invader_Instance2.png")
Tier3_1 = pygame.image.load("Sprites\\Enemies\\Tier3Invader_Instance1.png")
Tier3_2 = pygame.image.load("Sprites\\Enemies\\Tier3Invader_Instance2.png")
MotherShip = pygame.image.load("Sprites\\Enemies\\MotherShip.png")

Player = pygame.image.load("Sprites\\Player\\Player.png")

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

Tier1Width = 12
Tier1Height = 9

Tier2Width = 11
Tier2Height = 8

Tier3Width = 8
Tier3Height = 8

MotherShipWidth = 18
MotherShipHeight = 7

ShieldBlockWidth = 8
ShieldBlockHeight = 8
ShieldTopWidth = 7
ShieldTopHeight = 7
ShieldBottomWidth = 6
SheildBottomHeight = 6

PlayerWidth = 25
PlayerHeight = 13

ButtonWidth = 200
ButtonHeight = SmallTextSize + 10
