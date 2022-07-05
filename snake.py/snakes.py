# import pygame
# import pygame, sys, time, random


# # Difficulty settings
# # Easy      ->  10
# # Medium    ->  25
# # Hard      ->  40
# # Harder    ->  60
# # Impossible->  120
# difficulty = 25

# # Window size
# frame_size_x = 720
# frame_size_y = 480

# # Checks for errors encountered
# check_errors = pygame.init()
# # pygame.init() example output -> (6, 0)
# # second number in tuple gives number of errors
# if check_errors[1] > 0:
#     print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
#     sys.exit(-1)
# else:
#     print('[+] Game successfully initialised')


# # Initialise game window
# pygame.display.set_caption('Snake Eater')
# game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# # Colors (R, G, B)
# black = pygame.Color(0, 0, 0)
# white = pygame.Color(255, 255, 255)
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 255, 0)
# blue = pygame.Color(0, 0, 255)


# # FPS (frames per second) controller
# fps_controller = pygame.time.Clock()


# # Game variables
# snake_pos = [100, 50]
# snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

# food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
# food_spawn = True

# direction = 'RIGHT'
# change_to = direction

# score = 0


# # Game Over
# def game_over():
#     my_font = pygame.font.SysFont('times new roman', 90)
#     game_over_surface = my_font.render('YOU DIED', True, red)
#     game_over_rect = game_over_surface.get_rect()
#     game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
#     game_window.fill(black)
#     game_window.blit(game_over_surface, game_over_rect)
#     show_score(0, red, 'times', 20)
#     pygame.display.flip()
#     time.sleep(3)
#     pygame.quit()
#     sys.exit()


# # Score
# def show_score(choice, color, font, size):
#     score_font = pygame.font.SysFont(font, size)
#     score_surface = score_font.render('Score : ' + str(score), True, color)
#     score_rect = score_surface.get_rect()
#     if choice == 1:
#         score_rect.midtop = (frame_size_x/10, 15)
#     else:
#         score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
#     game_window.blit(score_surface, score_rect)
#     # pygame.display.flip()


# # Main logic
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         # Whenever a key is pressed down
#         elif event.type == pygame.KEYDOWN:
#             # W -> Up; S -> Down; A -> Left; D -> Right
#             if event.key == pygame.K_UP or event.key == ord('w'):
#                 change_to = 'UP'
#             if event.key == pygame.K_DOWN or event.key == ord('s'):
#                 change_to = 'DOWN'
#             if event.key == pygame.K_LEFT or event.key == ord('a'):
#                 change_to = 'LEFT'
#             if event.key == pygame.K_RIGHT or event.key == ord('d'):
#                 change_to = 'RIGHT'
#             # Esc -> Create event to quit the game
#             if event.key == pygame.K_ESCAPE:
#                 pygame.event.post(pygame.event.Event(pygame.QUIT))

#     # Making sure the snake cannot move in the opposite direction instantaneously
#     if change_to == 'UP' and direction != 'DOWN':
#         direction = 'UP'
#     if change_to == 'DOWN' and direction != 'UP':
#         direction = 'DOWN'
#     if change_to == 'LEFT' and direction != 'RIGHT':
#         direction = 'LEFT'
#     if change_to == 'RIGHT' and direction != 'LEFT':
#         direction = 'RIGHT'

#     # Moving the snake
#     if direction == 'UP':
#         snake_pos[1] -= 10
#     if direction == 'DOWN':
#         snake_pos[1] += 10
#     if direction == 'LEFT':
#         snake_pos[0] -= 10
#     if direction == 'RIGHT':
#         snake_pos[0] += 10

#     # Snake body growing mechanism
#     snake_body.insert(0, list(snake_pos))
#     if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
#         score += 1
#         food_spawn = False
#     else:
#         snake_body.pop()

#     # Spawning food on the screen
#     if not food_spawn:
#         food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
#     food_spawn = True
# # GFX
#     game_window.fill(black)
#     for pos in snake_body:
#         # Snake body
#         # .draw.rect(play_surface, color, xy-coordinate)
#         # xy-coordinate -> .Rect(x, y, size_x, size_y)
#         pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

#     # Snake food
#     pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

#     # Game Over conditions
#     # Getting out of bounds
#     if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
#         game_over()
#     if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
#         game_over()
#     # Touching the snake body
#     for block in snake_body[1:]:
#         if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
#             game_over()

#     show_score(1, white, 'consolas', 20)
#     # Refresh game screen
#     pygame.display.update()
#     # Refresh rate
#     fps_controller.tick(difficulty)
















# import pygame

# SIZE_BLOCK = 20
# FRAME_COLOR = (0, 255, 204)
# WHITE = (255,255,255)
# BLUE = (204, 255, 255)
# HEADER_COLOR = (0, 204, 153)
# SNAKE_COLOR = (0, 102, 0)
# COUNT_BLOCK = 20
# HEADER_MARGIN = 70
# MARGIN = 1
# size = [SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCK, SIZE_BLOCK * COUNT_BLOCK + 2*SIZE_BLOCK + MARGIN * COUNT_BLOCK + HEADER_MARGIN]

# print(size)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Змейка")

# class SnakeBlock:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# def draw_block(color, row, column):
#     pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1), HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK, SIZE_BLOCK])

# snake_block = [SnakeBlock(9,8), SnakeBlock(9,9 ), SnakeBlock(9,10)]
# d_row = 0
# d_col = 1

# while True:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print("exit")
#             pygame.quit()
        
#     screen.fill(FRAME_COLOR)
#     pygame.draw.rect(screen, HEADER_COLOR, [0,0, size[0], HEADER_MARGIN])

#     for row in range(COUNT_BLOCK):
#         for column in range(COUNT_BLOCK):
#             if (row + column) % 2 == 0:
#                 color = BLUE
#             else:
#                 color = WHITE
#             draw_block(color, row, column)
#             # pygame.draw.rect(screen,color,[10+column*SIZE_BLOCK + MARGIN*(column+1),20+row*SIZE_BLOCK + MARGIN*(row+1), SIZE_BLOCK, SIZE_BLOCK])
#     for block in snake_block:
#         draw_block(SNAKE_COLOR, block.x, block.y)

#     head = snake_block[-1]
#     new_head = SnakeBlock(head.x + d_row, head.y + d_col)
#     snake_block.append(new_head)
#     snake_block.pop(0)

#     pygame.display.flip()
#     timer.tick(2)


# import pygame
# from random import randrange

# RES = 800
# SIZE = 50

# x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
# apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
# length = 1
# snake = [(x, y)]
# dx, dy = 0, 0
# fps = 60
# dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
# score = 0
# speed_count, snake_speed = 0, 10

# pygame.init()
# surface = pygame.display.set_mode([RES, RES])
# clock = pygame.time.Clock()
# font_score = pygame.font.SysFont('Arial', 26, bold=True)
# font_end = pygame.font.SysFont('Arial', 66, bold=True)
# img = pygame.image.load('1.jpg').convert()

# def close_game():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()

# while True:
#     surface.blit(img, (0, 0))
#     # drawing snake, apple
#     [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
#     pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
#     # show score
#     render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
#     surface.blit(render_score, (5, 5))
#     # snake movement
#     speed_count += 1
#     if not speed_count % snake_speed:
# 	    x += dx * SIZE
# 	    y += dy * SIZE
# 	    snake.append((x, y))
# 	    snake = snake[-length:]
#     # eating food
#     if snake[-1] == apple:
#         apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
#         length += 1
#         score += 1
#         snake_speed -= 1
#         snake_speed = max(snake_speed, 4)
#     # game over
#     if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
#         while True:
#             render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
#             surface.blit(render_end, (RES // 2 - 200, RES // 3))
#             pygame.display.flip()
#             close_game()

#     pygame.display.flip()
#     clock.tick(fps)
#     close_game()
#     # controls
#     key = pygame.key.get_pressed()
#     if key[pygame.K_w]:
#         if dirs['W']:
#             dx, dy = 0, -1
#             dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
#     elif key[pygame.K_s]:
#         if dirs['S']:
#             dx, dy = 0, 1
#             dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
#     elif key[pygame.K_a]:
#         if dirs['A']:
#             dx, dy = -1, 0
#             dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
#     elif key[pygame.K_d]:
#         if dirs['D']:
#             dx, dy = 1, 0
#             dirs = {'W': True, 'S': True, 'A': False, 'D': True, }

# //////////////////////////////////////////////////////////////////////////////////
# import pygame
# import time
# import random
 
# pygame.init()
 
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
 
# dis_width = 600
# dis_height = 400
 
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game by Pythonist')
 
# clock = pygame.time.Clock()
 
# snake_block = 10
# snake_speed = 15
 
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)
 
 
# def Your_score(score):
#     value = score_font.render("Your Score: " + str(score), True, yellow)
#     dis.blit(value, [0, 0])
 
 
 
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
# def gameLoop():
#     game_over = False
#     game_close = False
 
#     x1 = dis_width / 2
#     y1 = dis_height / 2
 
#     x1_change = 0
#     y1_change = 0
 
#     snake_List = []
#     Length_of_snake = 1
 
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
#     while not game_over:
 
#         while game_close == True:
#             dis.fill(blue)
#             message("You Lost! Press C-Play Again or Q-Quit", red)
#             Your_score(Length_of_snake - 1)
#             pygame.display.update()
 
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
 
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
 
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
 
#         our_snake(snake_block, snake_List)
#         Your_score(Length_of_snake - 1)
 
#         pygame.display.update()
 
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
 
#         clock.tick(snake_speed)
 
#     pygame.quit()
#     quit()
 
 
# gameLoop()



# 2222222////////////////////////////////////////////////////////////////

# # importing libraries
# import pygame
# import time
# import random
 
# snake_speed = 15
 
# # Window size
# window_x = 720
# window_y = 480
 
# # defining colors
# black = pygame.Color(0, 0, 0)
# white = pygame.Color(255, 255, 255)
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 255, 0)
# blue = pygame.Color(0, 0, 255)

# # Initialising pygame
# pygame.init()
 
# # Initialise game window
# pygame.display.set_caption('GeeksforGeeks Snakes')
# game_window = pygame.display.set_mode((window_x, window_y))
 
# # FPS (frames per second) controller
# fps = pygame.time.Clock()

# # defining snake default position
# snake_position = [100, 50]
 
# # defining first 4 blocks of snake
# # body
# snake_body = [  [100, 50],
#                 [90, 50],
#                 [80, 50],
#                 [70, 50]
#             ]
# # fruit position
# fruit_position = [random.randrange(1, (window_x//10)) * 10,
#                   random.randrange(1, (window_y//10)) * 10]
# fruit_spawn = True
 
# # setting default snake direction
# # towards right
# direction = 'RIGHT'
# change_to = direction

# # initial score
# score = 0
 
# # displaying Score function
# def show_score(choice, color, font, size):
   
#     # creating font object score_font
#     score_font = pygame.font.SysFont(font, size)
     
#     # create the display surface object
#     # score_surface
#     score_surface = score_font.render('Score : ' + str(score), True, color)
     
#     # create a rectangular object for the
#     # text surface object
#     score_rect = score_surface.get_rect()
     
#     # displaying text
#     game_window.blit(score_surface, score_rect)


# # game over function
# def game_over():
   
#     # creating font object my_font
#     my_font = pygame.font.SysFont('times new roman', 50)
     
#     # creating a text surface on which text
#     # will be drawn
#     game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
     
#     # create a rectangular object for the text
#     # surface object
#     game_over_rect = game_over_surface.get_rect()
     
#     # setting position of the text
#     game_over_rect.midtop = (window_x/2, window_y/4)
     
#     # blit will draw the text on screen
#     game_window.blit(game_over_surface, game_over_rect)
#     pygame.display.flip()
     
#     # after 2 seconds we will quit the
#     # program
#     time.sleep(2)
     
#     # deactivating pygame library
#     pygame.quit()
     
#     # quit the program
#     quit()

# # Main Function
# while True:
   
#     # handling key events
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 change_to = 'UP'
#             if event.key == pygame.K_DOWN:
#                 change_to = 'DOWN'
#             if event.key == pygame.K_LEFT:
#                 change_to = 'LEFT'
#             if event.key == pygame.K_RIGHT:
#                 change_to = 'RIGHT'
 
#     # If two keys pressed simultaneously
#     # we don't want snake to move into two directions
#     # simultaneously
#     if change_to == 'UP' and direction != 'DOWN':
#         direction = 'UP'
#     if change_to == 'DOWN' and direction != 'UP':
#         direction = 'DOWN'
#     if change_to == 'LEFT' and direction != 'RIGHT':
#         direction = 'LEFT'
#     if change_to == 'RIGHT' and direction != 'LEFT':
#         direction = 'RIGHT'
 
#     # Moving the snake
#     if direction == 'UP':
#         snake_position[1] -= 10
#     if direction == 'DOWN':
#         snake_position[1] += 10
#     if direction == 'LEFT':
#         snake_position[0] -= 10
#     if direction == 'RIGHT':
#         snake_position[0] += 10
 
#     # Snake body growing mechanism
#     # if fruits and snakes collide then scores will be
#     # incremented by 10
#     snake_body.insert(0, list(snake_position))
#     if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
#         score += 10
#         fruit_spawn = False
#     else:
#         snake_body.pop()
         
#     if not fruit_spawn:
#         fruit_position = [random.randrange(1, (window_x//10)) * 10,
#                           random.randrange(1, (window_y//10)) * 10]
         
#     fruit_spawn = True
#     game_window.fill(black)
     
#     for pos in snake_body:
#         pygame.draw.rect(game_window, green, pygame.Rect(
#           pos[0], pos[1], 10, 10))
         
#     pygame.draw.rect(game_window, white, pygame.Rect(
#       fruit_position[0], fruit_position[1], 10, 10))
 
#     # Game Over conditions
#     if snake_position[0] < 0 or snake_position[0] > window_x-10:
#         game_over()
#     if snake_position[1] < 0 or snake_position[1] > window_y-10:
#         game_over()
     
#     # Touching the snake body
#     for block in snake_body[1:]:
#         if snake_position[0] == block[0] and snake_position[1] == block[1]:
#             game_over()
     
#     # displaying score countinuously
#     show_score(1, white, 'times new roman', 20)
     
#     # Refresh game screen
#     pygame.display.update()
 
#     # Frame Per Second /Refresh Rate
#     fps.tick(snake_speed)


# 33333333333333333333333333/////////////////////////////////////

import pygame

screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((0, 0, 0)) # 0, 0, 0 is RGB code for the colour black (0 red, 0 green, 0 blue)
pygame.display.flip()
snake_speed = 30
clock = pygame.time.Clock()
running = True
# While "running" is true
# (always true unless user quits):
while running:
    screen.fill((0,0,0))

    pygame.display.flip()
    clock.tick(snake_speed)

    # Get the next events from the queue
    # For each event returned from get(),
    for event in pygame.event.get():
        # If the event is "QUIT"
        if event.type == pygame.QUIT:
            # Set running to False, stop event loop
            running = False

blue = (0, 0, 255) # RGB code for blue
pygame.draw.rect(screen, blue, [200, 150, 10, 10])

# Set the snake in the middle of the screen
snake_x = screen_width / 2
snake_y = screen_height / 2
speed_x = 0
speed_y = 2

   # Handling key events
   for event in pygame.event.get():
    # If the event is "KEYDOWN"
       if event.type == pygame.KEYDOWN:
        # Go up on arrow key UP
           if event.key == pygame.K_UP:
            speed_x = 0
                speed_y = -2
        # Go down on arrow key DOWN
           if event.key == pygame.K_DOWN:
            speed_x = 0
                speed_y = 2
        # Go left on arrow key LEFT
           if event.key == pygame.K_LEFT:
            speed_y = 0
                speed_x = -2
        # Go right on arrow key RIGHT
           if event.key == pygame.K_RIGHT:
            speed_y = 0
                speed_x = 2