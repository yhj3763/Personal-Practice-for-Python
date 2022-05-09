import pygame

#initialize 
pygame.init()

# setting up for screen size
screen_width = 400
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My Game")

#Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when we clsoe the window
            running = False  


# pygame end
pygame.quit()
