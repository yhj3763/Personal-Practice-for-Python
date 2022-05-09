import pygame

#initialize 
pygame.init()

# setting up for screen size
screen_width = 400
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My Game")


#loading background
background = pygame.image.load("C:/Users/yaj37/Desktop/pythonworkplace/pygame_basic/background.png")

#loading sprite
character = pygame.image.load("C:/Users/yaj37/Desktop/pythonworkplace/pygame_basic/character.png") 
character_size = character.get_rect().size # getting size of image
character_width = character_size[0]   # width of character
character_height = character_size[1]  # height of character
character_x_pos = (screen_width / 2) -(character_width /2)  # placed in half of width of screen
character_y_pos = screen_height  - character_height#  placed at the bottom of screen


#Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when we clsoe the window
            running = False  

   
   # screen.fill((0, 0, 255))
    screen.blit(background, (0,0)) #drawing background

    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update() #drawing screen again.


# pygame end
pygame.quit()
