from consts import *
import sys
import random

# Creating the screen:
pygame.init()
screen = pygame.display.set_mode((500, 250))
clock = pygame.time.Clock()
pygame.display.set_caption("The Flag")

# Creating the matrix:
matrix = []
for i in range(25):
    matrix.append([])
    for j in range(50):
        matrix[i].append(0)

# Placing grass on the screen:
list_grass_index = []
index = [0, 0]
for i in range(20):
    width = random.randrange(20, 420, 40)
    length = random.randrange(0, 190, 30)
    index = [length, width]
    while index in list_grass_index:
        width = random.randrange(20, 420, 40)
        length = random.randrange(0, 190, 30)
        index = [length, width]
    list_grass_index.append(index)

# Placing mines in the matrix:
list_mine_index = []
for i in range(20):
    width = random.randrange(0, 46, 3)
    length = random.randrange(0, 22, 1)
    index = [length, width]
    index_not_flag = [length, width + 2]
    while index_not_flag in FLAG_INDEX_LIST or index in PLAYER_START_INDEX or index in list_mine_index:
        width = random.randrange(0, 46, 3)
        length = random.randrange(0, 22, 1)
        index = [length, width]
    list_mine_index.append(index)
for row in range(25):
    for col in range(50):
        for i in range(20):
            if row == list_mine_index[i][0] and col == list_mine_index[i][1]:
                matrix[row][col] = "mine"
                matrix[row][col + 1] = "mine"
                matrix[row][col + 2] = "mine"

# Data about the player:
width = 0
length = 0
progress_on_x = 0
progress_on_y = 0

# Game loop:
running = True
while running:
    pygame.display.flip()
    # Applying everything required to start the game:
    screen.fill("dark green")
    for index in list_grass_index:
        screen.blit(GRASS, (index[1], index[0]))
    screen.blit(WELCOME, (10, 0))
    screen.blit(FLAG, (460, 220))
    screen.blit(COLORFUL_PLAYER, (progress_on_x, progress_on_y))
    index_player = [width, length]
    matrix[index_player[1]][index_player[0]] = PLAYER_IN_MATRIX

    # Performing actions in the game:
    for event in pygame.event.get():
        # Clicking on the red X:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            # Pressing the right key:
            if event.key == pygame.K_RIGHT:
                if progress_on_x < 480:
                    matrix[index_player[1]][index_player[0]] = 0
                    progress_on_x += 10
                    width += 1
                    index_player = [width, length]
                    matrix[index_player[1]][index_player[0]] = PLAYER_IN_MATRIX

            # Pressing the left key:
            elif event.key == pygame.K_LEFT:
                if progress_on_x > 0:
                    matrix[index_player[1]][index_player[0]] = 0
                    progress_on_x -= 10
                    width -= 1
                    index_player = [width, length]
                    matrix[index_player[1]][index_player[0]] = PLAYER_IN_MATRIX

            # Pressing the down key:
            elif event.key == pygame.K_DOWN:
                if progress_on_y < 210:
                    matrix[index_player[1]][index_player[0]] = 0
                    progress_on_y += 10
                    length += 1
                    index_player = [width, length]
                    matrix[index_player[1]][index_player[0]] = PLAYER_IN_MATRIX

            # pressing the up key:
            elif event.key == pygame.K_UP:
                if progress_on_y > 0:
                    matrix[index_player[1]][index_player[0]] = 0
                    progress_on_y -= 10
                    length -= 1
                    index_player = [width, length]
                    matrix[index_player[1]][index_player[0]] = PLAYER_IN_MATRIX

            # Pressing the ENTER key:
            elif event.key == pygame.K_RETURN:
                # Creating a checkered game screen and placing the elements on it:
                root = pygame.display.set_mode((500, 250))
                root.fill("BLACK")
                for i in range(0, root.get_height() // 1):
                    pygame.draw.line(root, "DARK GREEN", (0, i * 10), (root.get_width(), i * 10))
                for j in range(0, root.get_width() // 1):
                    pygame.draw.line(root, "DARK GREEN", (j * 10, 0), (j * 10, root.get_height()))
                screen.blit(GREEN_PLAYER, (progress_on_x, progress_on_y))
                for index in list_mine_index:
                    screen.blit(MINE, (index[1] * 10, index[0] * 10))

                # Clicking on the red X:
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        quit()

                pygame.display.flip()
                clock.tick(100)
                # Shows the embedded screen for a second:
                pygame.time.delay(1000)

            # Pressing the number buttons 1-9 on the keyboard:
            elif event.key in NUM_KEYBOARD:
                time_down = pygame.time.get_ticks()
                need_to_run = True
                # Defining relevant variables:
                save_width = str(width) + '\n'
                save_length = str(length) + '\n'
                save_p_x = str(progress_on_x) + '\n'
                save_p_y = str(progress_on_y) + '\n'
                save_grass = str(list_grass_index) + '\n'
                save_mine = str(list_mine_index) + '\n'

                while need_to_run:
                    total_time_pressed = 0
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP and event.key == event.key:
                            time_up = pygame.time.get_ticks()
                            total_time_pressed = time_up - time_down
                            if total_time_pressed <= 1000:
                                file = open(DATABASE, 'w')
                                file.write(save_grass)
                                file.write(save_mine)
                                file.write(save_width)
                                file.write(save_length)
                                file.write(save_p_x)
                                file.write(save_p_y)
                                file.close()
                                screen.blit(SAVED, (0, 0))
                                screen_display = pygame.display
                                screen_display.update()
                                pygame.time.delay(1000)
                                running = False

                            else:
                                file = open(DATABASE, 'r')
                                list_grass_index = file.readline()
                                after_split = list_grass_index.split("], [")
                                first = after_split[0].split("[[")[1]
                                last = after_split[-1].split("]]")[0]
                                after_split[0] = first
                                after_split[-1] = last
                                new_total_list = []
                                for string in after_split:
                                    a, b = string.split(", ")
                                    new_total_list.append([int(a), int(b)])
                                list_grass_index = new_total_list
                                list_mine_index = file.readline()
                                after_split_mine = list_mine_index.split("], [")
                                first_mine = after_split_mine[0].split("[[")[1]
                                last_mine = after_split_mine[-1].split("]]")[0]
                                after_split_mine[0] = first_mine
                                after_split_mine[-1] = last_mine
                                new_total_list_mine = []
                                for string in after_split_mine:
                                    a, b = string.split(", ")
                                    new_total_list_mine.append([int(a), int(b)])
                                list_mine_index = new_total_list_mine

                                width = int(file.readline())
                                length = int(file.readline())
                                progress_on_x = int(file.readline())
                                progress_on_y = int(file.readline())
                                file.close()
                                screen.blit(LOADING, (0, 0))
                                screen_display = pygame.display
                                screen_display.update()
                                pygame.time.delay(1000)
                            need_to_run = False

            pygame.display.flip()

        # Testing for touching the mine:
        if (matrix[index_player[1] + 3][index_player[0]] == "mine"
                or matrix[index_player[1] + 3][index_player[0] + 1] == "mine"):
            screen_display = pygame.display
            screen.fill("Red")
            screen.blit(BOOM, (0, 0))
            screen_display.update()
            pygame.time.delay(1500)
            screen.blit(GAME_OVER, (0, 0))
            screen_display.update()
            pygame.time.delay(1500)
            running = False

        # Checking for touching the flag:
        elif [index_player[1] + 2, index_player[0] + 1] in FLAG_INDEX_LIST:
            screen_display = pygame.display
            screen.blit(WINNER, (0, 0))
            screen_display.update()
            pygame.time.delay(3000)
            running = False

        pygame.display.flip()
