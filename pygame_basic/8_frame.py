import pygame
###############################################################
# Basic initialzation(Must) 

#initialize 
pygame.init()

# setting up for screen size
screen_width = 400
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My Game")

#FPS
clock = pygame.time.Clock()
#################################################################

# 1. User game initialzation(Background, Game Image, Cordinate, Speed, Fontt)


running = True
while running:
    dt = clock.tick(30)

    # 2. Event dealing(Keyboard, Mouse, etc..)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when we clsoe the window
            running = False  

      

    # 3. Game Character position Definition
  
    # 4. Collision

    # 5. Drawing on the screen
   

    pygame.display.update() #drawing screen again.

    


# pygame end
pygame.quit()
