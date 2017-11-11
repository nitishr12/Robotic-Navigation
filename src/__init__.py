import pygame
#Initialize the library
pygame.init()

#Set the height and width of the window
height=522
width=480

#Initialize the screen with the dimensions
gameDisplay=pygame.display.set_mode((height,width))

#Title of the game
pygame.display.set_caption("Robot Navigation")

#Frame
clock=pygame.time.Clock()

#Load the images of the robot
robotImgTop=pygame.image.load('Robot_top.png')
robotImgDown=pygame.image.load('Robot_down.png')
robotImgLeft=pygame.image.load('Robot_left.png')
robotImgRight=pygame.image.load('Robot_right.png')

#Load the background image
backgroundImg=pygame.image.load('Layout.png')

#This flag is set when the game is exited
crashed=False

#Function to display the robot
def robot(x,y,robotImg):
    gameDisplay.blit(robotImg,(x,y))
    

#The window size that the robot can go atmost
x_startLimit=40
x_endLimit=height-30
y_startLimit=10
y_endLimit=width-65 

#Denotes the change in the position
x_change=0
y_change=0

#Initialize the starting position
x=x_startLimit
y=y_endLimit

#Initialize the starting position of the robot
robotImg=robotImgTop

#Game loop
while not crashed:
    
    #Check for different events
    for event in pygame.event.get():
        
        #If the player clicks on the close button
        if event.type == pygame.QUIT:
            crashed=True
        
        #When a key in the keyboard is pressed
        if event.type == pygame.KEYDOWN:
            
            #Left key
            if event.key == pygame.K_LEFT:
                x_change = -3
                robotImg=robotImgLeft
                
            #Right key
            if event.key == pygame.K_RIGHT:
                x_change = 3
                robotImg=robotImgRight
                
            #Up key
            if event.key == pygame.K_UP:
                y_change = -3
                robotImg=robotImgTop
                
            #Down key
            if event.key == pygame.K_DOWN:
                y_change = 3
                robotImg=robotImgDown
            #print(x,y)
                
        #When key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change=0
                y_change=0
                
    #This condition checks if the robot is within the range of the screen
    if(x+x_change>=x_startLimit and x+x_change<=x_endLimit and y+y_change>=y_startLimit and y+y_change<=y_endLimit):
        x+=x_change
        y+=y_change
        
    #Set the background image
    gameDisplay.blit(backgroundImg,(0,0))
    
    #Set the robot at the appropriate position
    robot(x,y,robotImg)
    
    #Updates the screen
    pygame.display.update()
    
    #Frame update
    clock.tick(60)
    
pygame.quit()
quit()