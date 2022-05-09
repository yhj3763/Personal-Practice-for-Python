import pygame

#initialize 
pygame.init()

# setting up for screen size
screen_width = 400
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My Game")

#FPS
clock = pygame.time.Clock()


#loading background
background = pygame.image.load("C:/Users/yaj37/Desktop/pythonworkplace/pygame_basic/background.png")



#loading sprite
character = pygame.image.load("C:/Users/yaj37/Desktop/pythonworkplace/pygame_basic/character.png") 
character_size = character.get_rect().size # getting size of image
character_width = character_size[0]   # width of character
character_height = character_size[1]  # height of character
character_x_pos = (screen_width / 2) -(character_width /2)  # placed in half of width of screen
character_y_pos = screen_height  - character_height#  placed at the bottom of screen


to_x = 0
to_y = 0

#movment speed
character_speed = 0.6

#enemy
enemy = pygame.image.load("C:/Users/yaj37/Desktop/pythonworkplace/pygame_basic/enemy.png") 
enemy_size = enemy.get_rect().size # getting size of image
enemy_width = enemy_size[0]   # width of enemy
enemy_height = enemy_size[1]  # height of enemy
enemy_x_pos = (screen_width / 2) -(enemy_width /2)  # placed in half of width of screen
enemy_y_pos = (screen_height / 2)  - (enemy_height / 2)#  placed at the bottom of screen

# font definition 
game_font = pygame.font.Font(None, 40)

# whole time
total_time =10

# start time
start_ticks = pygame.time.get_ticks()



#Event loop
running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when we clsoe the window
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x *dt
    character_y_pos += to_y *dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos <0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    #collision 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect =enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

   #collision check
    if character_rect.colliderect(enemy_rect):
        print("Crushed")
        running = False
   
   # screen.fill((0, 0, 255))
    screen.blit(background, (0,0)) #drawing background
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))


    elasped_time = (pygame.time.get_ticks() - start_ticks) /1000

    timer = game_font.render(str(int(total_time - elasped_time)), True, (255, 255, 255))
    #Printed letter, True, font color

    screen.blit(timer, (10, 10))

    #if time is under 0 game is over
    if total_time - elasped_time <= 0:
        print("Time Over")
        running = False


    pygame.display.update() #drawing screen again.


pygame.time.delay(2000)

    


# pygame end
pygame.quit()
