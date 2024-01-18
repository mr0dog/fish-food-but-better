import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("gravel")
mousePos = (400,400)



#create a buncha empty lists
sizes1 = []
sizes2 = []
sizes3 = []
sizes4 = []
positions1 = []
positions2 = []
positions3 = []
positions4 = []
colors1 = []
colors2 = []
colors3 = []
colors4 = []


#push a buncha numbers into the lists
for i in range(1000):
    sizes1.append(random.randrange(5,10)) #push in 1 number
    positions1.append((random.randrange(0, 400),random.randrange(0, 400))) #push in a 2-slot TUPLE
    colors1.append((random.randrange(100,255),0,0)) #push in a 3-slot TUPLE
    
for i in range(1000):
    sizes2.append(random.randrange(5,10)) #push in 1 number
    positions2.append((random.randrange(400, 800),random.randrange(400, 800))) #push in a 2-slot TUPLE
    colors2.append((0,random.randrange(0, 255),0)) #push in a 3-slot TUPLE

for i in range(1000):
    sizes3.append(random.randrange(5,10)) #push in 1 number
    positions3.append((random.randrange(400, 800),random.randrange(0, 400))) #push in a 2-slot TUPLE
    colors3.append((random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255))) #push in a 3-slot TUPLE

for i in range(1000):
    sizes4.append(random.randrange(5,10)) #push in 1 number
    positions4.append((random.randrange(0, 400),random.randrange(400, 800))) #push in a 2-slot TUPLE
    colors4.append((0,random.randrange(0, 255),230,0)) #push in a 3-slot TUPLE


while 1: #game loop###########################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #render section------------------------------
    
    screen.fill((0,0,0))# Clear the screen

    #draw the lines on the screen
    pygame.draw.line(screen, (255,255,255), (400, 0), (400, 800), 2)
    pygame.draw.line(screen, (255,255,255), (0, 400), (800, 400), 2)

    #draw the gravel
    for i in range(1000):
        pygame.draw.circle(screen, colors1[i], (positions1[i][0], positions1[i][1]), sizes1[i])
        
    for i in range(1000):
        pygame.draw.circle(screen, colors2[i], (positions2[i][0], positions2[i][1]), sizes2[i])
        
    for i in range(1000):
        pygame.draw.circle(screen, colors3[i], (positions3[i][0], positions3[i][1]), sizes3[i])
    
    for i in range(1000):
        pygame.draw.circle(screen, colors4[i], (positions4[i][0], positions4[i][1]), sizes4[i])
    
    pygame.display.flip()# Update the display

#end of game loop###################################################################
pygame.quit()

