import pygame
import os
###############################################################
# Basic initialzation(Must) 

#initialize 
pygame.init()

# setting up for screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My Game")

#FPS
clock = pygame.time.Clock()
#################################################################

# 1. User game initialzation(Background, Game Image, Cordinate, Speed, Fontt)
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

#background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]


#character
character =pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height


character_to_x= 0

character_speed = 5

# weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# can use multiple times
weapons =[]

weapon_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. Event dealing(Keyboard, Mouse, etc..)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when we clsoe the window
            running = False  
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width /2) - (weapon_width /2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

      

    # 3. Game Character position Definition
    character_x_pos += character_to_x

    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # weapon position
    weapons = [ [w[0], w[1]- weapon_speed]  for w in weapons]

    weapons = [ [w[0], w[1]]  for w in weapons if w[1] > 0]
    # 4. Collision

    # 5. Drawing on the screen

    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))
   
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos,character_y_pos))
    


    pygame.display.update() #drawing screen again.

    


# pygame end
pygame.quit()
