import pygame

#initialize 
pygame.init()

# setting up for screen size
screen_width = 400
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My Game")


#loding background
background = pygame.image.load("C:/Users/yaj37/Desktop/pythonworkplace/pygame_basic/background.png")

#Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when we clsoe the window
            running = False  

   
   # screen.fill((0, 0, 255))
    screen.blit(background, (0,0)) #drawing background

    pygame.display.update() #drawing screen again.


# pygame end
pygame.quit()
