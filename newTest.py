import pygame
import time
import random
pygame.init()
display_width = 1000
display_height = 700
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('game 1')

clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
car_width=73

#pygame.draw.circle(screen, color, (x,y), radius, thickness)
def boost(boostx,boosty,radius):
    pygame.draw.circle(gameDisplay, red, (boostx,boosty), 30, 1)
    
def  things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count), True,black)
    gameDisplay.blit(text,(0,0))
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 

def car(x,y):
    gameDisplay.blit(carImg,(x,y))
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update() 
    time.sleep(2)   
    game_loop()
def crash():
    message_display('you crashed')

def game_loop():

    x= (display_width * 0.45)
    y = (display_height * 0.8)

    gameDisplay.fill(white)
    car(x,y)

    x_change = 0
    gameExit = False
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed_y = random.randrange(7,10)
    thing_speed_x = (random.randrange(-1,2))*random.randrange(7,10)
    if thing_speed_x > 0:
        f1=0
    else:
        f1=1

    thing_width = 100
    thing_height = 100  
    dodged = 0  
    while not gameExit:
        
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = +5
            
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change = 0
        
            
        x = x + x_change

        if x > display_width or x<0:
            crash()         
        if thing_starty>display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)       
            dodged +=1
            thing_speed_y = random.randrange(7,10)
            thing_speed_x = random.randrange(-1,2)*random.randrange(7,10)
            if thing_speed_x > 0:
                f1=0
            else:
                f1=1
            
            #thing_speed_y+=1

        if y < thing_starty + thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x+ car_width<thing_startx+thing_width:
                print('x crossover')
                crash()
        if thing_startx + thing_width >=  display_width and f1 == 0 :
            thing_speed_x *= (-1)
            f1=1
        if thing_startx <= 0 and f1==1:
            thing_speed_x *= (-1)
            f1=0
        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty+=thing_speed_y
        thing_startx+=thing_speed_x
        
        car(x,y)
        things_dodged(dodged)
        
        
        pygame.display.update()

        clock.tick(60)

game_loop()
pygame.quit()

quit()  
