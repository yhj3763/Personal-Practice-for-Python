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

#Event loop
running = True
while running:
    dt = clock.tick(30)
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
   
   # screen.fill((0, 0, 255))
    screen.blit(background, (0,0)) #drawing background

    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update() #drawing screen again.


# pygame end
pygame.quit()
