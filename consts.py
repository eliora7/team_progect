import pygame

pygame.init()

# All game images:
GRASS = pygame.image.load("grass.png")
GRASS = pygame.transform.scale(GRASS, (40, 30), )
FLAG = pygame.image.load("flag.png")
FLAG = pygame.transform.scale(FLAG, (40, 30), )
MINE = pygame.image.load("mine.png")
MINE = pygame.transform.scale(MINE, (30, 10), )
GREEN_PLAYER = pygame.image.load("green_player.png")
GREEN_PLAYER = pygame.transform.scale(GREEN_PLAYER, (20, 40), )
COLORFUL_PLAYER = pygame.image.load("colorful_player.png")
COLORFUL_PLAYER = pygame.transform.scale(COLORFUL_PLAYER, (20, 40), )
BOOM = pygame.image.load("boom_effect.png")
BOOM = pygame.transform.scale(BOOM, (500, 250), )
GAME_OVER = pygame.image.load("game_over.png")
GAME_OVER = pygame.transform.scale(GAME_OVER, (500, 250), )
WINNER = pygame.image.load("winner.png")
WINNER = pygame.transform.scale(WINNER, (500, 250), )
WELCOME = pygame.image.load("welcome.png")
WELCOME = pygame.transform.scale(WELCOME, (300, 40), )

# Constants:
FLAG_INDEX_LIST = [[24, 49], [24, 48], [24, 47], [24, 46], [23, 49], [23, 48], [23, 47], [23, 46], [22, 49], [22, 48],
                   [22, 47], [22, 46]]
PLAYER_START_INDEX = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [3, 0], [3, 1]]
PLAYER_IN_MATRIX = "player"
# PART 2:
NUM_KEYBOARD = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                pygame.K_8, pygame.K_9]
DATABASE = "file.txt"
