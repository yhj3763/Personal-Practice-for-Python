import pygame
import random

###############################################################
# Basic initialzation(Must) 

#initialize 
pygame.init()

# setting up for screen size
screen_width = 400
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Quiz")

#FPS
clock = pygame.time.Clock()
#################################################################

# 1. User game initialzation(Background, Game Image, Cordinate, Speed, Fontt)
background = pygame.image.load("C:/Users/yaj37/Desktop/pythonworkplace/pygame_basic/background.png")


character = pygame.image.load("C:/Users/yaj37/Desktop/pythonworkplace/pygame_basic/character.png") 
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 10

#enemy
enemy = pygame.image.load("C:/Users/yaj37/Desktop/pythonworkplace/pygame_basic/enemy.png") 
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 10


running = True
while running:
    dt = clock.tick(30)

    # 2. Event dealing(Keyboard, Mouse, etc..)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when we clsoe the window
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    
    # 3. Game Character position Definition
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width-enemy_width)
  
    # 4. Collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos


    if character_rect.colliderect(enemy_rect):
        print("Crushed")
        running = False


    # 5. Drawing on the screen
    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos,character_y_pos) )
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() #drawing screen again.
