print("OS_Eater Open\nDebugging Mode: ON")
#Modules
import pygame
import random
print("Modules Imported...")

#Initialize
pygame.init()
print("Pygame Initialized...")

#Defining colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
pink = (255,0,255)
gray = (128,128,128)
bg = white
txt_colour = blue
print("Colors Set...")

#Variables
display_width = 1080
display_height = 720
block_size = 20
FPS = 30
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()
pingu_icon = pygame.image.load("OS_Eater Icon.jpg")
print("Variables Created...")

#Display
game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("OS_Eater")
pygame.display.set_icon(pingu_icon)
print("Display On...")

#Images and Sounds
#Credit for music:
#My friend Carlos Murillo 
pygame.mixer.music.load("Musix.wav")
pygame.mixer.music.play(loops = -1, start = 0.0)
door = pygame.image.load("Door.png")
door_rect = door.get_rect()
orange = pygame.image.load("Orange.png")
orange_rect = orange.get_rect()
pingu = pygame.image.load("Pingu.png")
pingu_rect = pingu.get_rect()
print("Images and Music Loaded...")

#Functions
print("Loading Functions...")

#Snake Function
def snake(lead_x,lead_y,block_size):
    pygame.draw.rect(game_display, bg, [lead_x,lead_y,block_size,block_size])
    game_display.blit(pingu, pingu_rect)
    pingu_rect.x = lead_x
    pingu_rect.y = lead_y

#Message Function
def message_rect(a, b, c, d):
    msg = font.render(a, True, b)
    rect = msg.get_rect()
    rect.center = (c, d)
    game_display.blit(msg, rect)

def message(a, b, c, d):
    msg=font.render(a, True, b)
    game_display.blit(msg, [c, d])

#Game Loop
def game_loop():
    game_exit = False
    game_over = False
    score = 0
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    apple_image = "orange"
    apple_x = round(random.randrange(0,display_width-block_size)/20.0)*20.0
    apple_y = round(random.randrange(0,display_height-block_size)/20.0)*20.0
    print("Function Variables Set...")
    
    while game_exit == False:
        #Game Over Loop
        while game_over == True:
            game_display.fill(bg)
            message_rect("Game over. Get Good. Press \"Q\" to Quit. Press \"SPACE\" to Play Again.", txt_colour, display_width / 2, display_height / 2)
            message_rect("Score: %d" %(score), txt_colour, display_width / 2, display_height /2 + 100)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_SPACE:
                        game_loop()
        #Event Handling Loop
        for event in pygame.event.get():
            #Exit
            if event.type == pygame.QUIT:
                game_exit = True
            #Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_d:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_w:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_s:
                    lead_y_change = block_size
                    lead_x_change = 0
        #Boundaries
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True
        #Continuous Movement
        lead_x += lead_x_change
        lead_y += lead_y_change
        #Background
        game_display.fill(bg)
        #Score Display
        message("Score: %d" % (score), txt_colour, 10, 10)
        #Apple
        pygame.draw.rect(game_display, bg, [apple_x, apple_y, block_size, block_size])
        if apple_image == "orange":
            game_display.blit(orange, orange_rect)
            orange_rect.x = apple_x
            orange_rect.y = apple_y
        elif apple_image == "door":
            game_display.blit(door, door_rect)
            door_rect.x = apple_x
            door_rect.y = apple_y
        #Snake Function
        snake(lead_x,lead_y,block_size)
        #Screen Update
        pygame.display.update()
        #Collision Detection & Score Update
        if lead_x == apple_x and lead_y == apple_y:
            score+=1
            apple_x = round(random.randrange(0,display_width-block_size)/20.0)*20.0
            apple_y = round(random.randrange(0,display_height-block_size)/20.0)*20.0
            if apple_image == "orange":
                apple_image = "door"
            elif apple_image == "door":
                apple_image = "orange"
        #FPS
        clock.tick(FPS)
    #Quitting the display and shell
    pygame.quit()
    quit

print("Game_Loop & Functions Ready...")
game_loop()
