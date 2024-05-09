###Olivia Rogers###

###Appples and Ogres###

###
###
#game plan: you have to build a bridge to cross the river
#you must find three planks to build the bridge
#you must also collect fruit that is randomly placed around the map
#there is an area blocked by the river where the ogre is
#you are stuck until you answer the question correctly
#to win the game you must build a bridge and collect enough fruit to feed to the ogre on the other side
###
###

import random

## Define a map and let the player move around it
#Define our map: 1 = wall, 0 = path
#0,0 is the top left of the map, therefore...
#moving up decreases the y location and
#moving left decreases the x location and vice versa

##CONSTANTS##
DO_NOTHING=-1
PRINT_STATEMENT=0
ASK_FOR_INPUT=1

##VARIABLES##
powerUpTurn=5  #how many turns they have if they find the power up
gamePlay=False #start the game loop as false because we ask if they want to play
power=False    #start the power up as false because they do not start with the power up

##LISTS##

#list of players inventory
inventory=[
            ["apples",0],
            ["planks",0]
            ]


#our game map
Map = [
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 0, 1, 4, 4, 1, 1, 0, 7, 8, 1],
	    [ 1, 0, 0, 1, 2, 1, 4, 4, 1, 0, 0, 7, 8, 1],
	    [ 1, 0, 6, 1, 3, 4, 4, 4, 1, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 1, 0, 1, 0, 4, 4, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 1, 0, 1, 0, 4, 4, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 0, 1, 0, 4, 4, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 0, 1, 0, 4, 4, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 0, 3, 0, 4, 4, 0, 0, 0, 7, 8, 1],
            [ 1, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 7, 8, 1],
            [ 1, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 7, 8, 1],
            [ 1, 0, 0, 1, 0, 4, 4, 4, 4, 0, 0, 7, 8, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            
	]

#list of all the possible events that can happen on each spot
eventList= [[DO_NOTHING, 0, "You are on the path","   "],
	    [DO_NOTHING, 1, "Wall","1  "],
	    [ASK_FOR_INPUT, 2, "You found a plank, do you want to pick it up? y/n","   "],
	    [PRINT_STATEMENT, 3, "You've come to a door.","   "],
	    [PRINT_STATEMENT, 4, "Theres a river in your way",")( "],
	    [PRINT_STATEMENT, 5, "You found fruit.","@  "],
            [PRINT_STATEMENT, 6, "You found a power up that shows you where all the planks are hiding, but it only lasts for 5 moves,","   "], #if they land on this square, which has a 50% chance of spawning, they are able to see all the planks for 3 moves 
            [ASK_FOR_INPUT, 7, "There is an ogre blocking your path, you must feed him 5 apples to pass,", "): " ,"Do you want to give the ogre your apples to pass? y/n"],
            [PRINT_STATEMENT, 8, "YOU WIN!!!","   "], #if they make it to the spots that are equal to 8, you win            
	   ]


##FUNCTIONS##

#define a function to print the starting statements at the beginning of the game
def starting_statements():
    print("Welcome to Apples and Ogres!")
    print("You are trapped in a forest, to escape you must cross the bridge and feed the ogre across the river.")
    print("Find planks hidden around the map to build a bridge to cross the river safely")
    print("If you are lucky, you may find a power up that shows you where the planks are hidden.")
    print("Collect 5 apples (@) to satisfy the ogre ): so he will let you pass.")
    gameStart=input("Are you ready to play? y/n")
    return(gameStart)


#Define a function to print our Map and current Player location
def drawMap(currX, currY):
    #print ("map size is : ", len(Map), " rows by ", len(Map[0]), " columns")
    print()
    for y in range (0, len(Map)):
        for x in range (0,len(Map[y])):
            if (currX == x) and (currY == y):   #print * if they are in this square
                print("*  ", end="")
                continue
            
            if Map[y][x]==2 and power==True: #print - for the plank if they have the powerup
                print("-  ", end="")
                continue
            
            print (eventList[Map[y][x]][3], end ="") #print everything else
        print()
    print()
    

#Define our function that will move the player
#The function will first check if the player can move or hits a wall
#If the player can move, then the current location will be updated
#If the player cannot move due to a wall, the location will not be updated    
def movePlayer(x,y,moveDir):

    #assume invalid move is attempted
    badMove = True

    #Now check if the move is valid - brute force method - better ways exist
    if moveDir == "u" and Map[y-1][x] != 1:
            #print ("valid up move")
            power_up(x,y)
            return (x, y-1)

    if moveDir == "d"and Map[y+1][x] != 1:
            power_up(x,y)
            #print ("valid down move")
            return (x, y+1)

    if moveDir == "l"and Map[y][x-1] != 1:
            power_up(x,y)
            #print ("valid left move")
            return (x-1, y)

    if moveDir == "r"and Map[y][x+1] != 1:
            power_up(x,y)
            #print ("valid right move")
            return (x+1, y)
         
    #they attempted a bad move
    if badMove:
        print ("**Invalid move** Try again.")
        return (x,y)   #return the same location they are in since no move


#check to see if the space the player is on is a special event besides wall or path
def check_Event (x, y):
    global currX, gamePlay
    if Map[y][x]!=-1 and Map[y][x]!=0:
        
        if Map[y][x]==4:
            print ("You cant go through the river unless you find a plank")
            
            if inventory[1][1]>=1:
                usePlank=input("you have a plank, would you like to use it to cross the river? y/n")

                if usePlank=="y":
                    inventory[1][1]=inventory[1][1]-1
                    Map[y][x]= 0
                    return
        
            currX=currX-1
            return (currX)
            
        if eventList[Map[y][x]][0]==1: #if first object in list is ASK_FOR_INPUT
            if Map[y][x]==7: #check first if it is an ogre
                if inventory[0][1]>=5: # then check if they have enough apples to feed it
                    giveApple=input(eventList[Map[y][x]][4]) #ask if they want to feed the ogre their apples
                    if giveApple=="y":
                        inventory[0][1]=inventory[0][1]-5
                        Map[y][x]=0
                        return
                    
                    currX=currX-1                 
                    return
                
                else: #if they dont have enough apples then they cannot pass
                    print(eventList[Map[y][x]][2])
                    currX=currX-1
                    return
                
            answer=input(eventList[Map[y][x]][2])
            
            if answer== "y":
                inventory[Map[y][x]-1][1]=inventory[Map[y][x]-1][1]+1 
                Map[y][x]=0
                
            return
            
        if eventList[Map[y][x]][0]==0: #if first object in list is PRINT_STATEMENT
            print(eventList[Map[y][x]][2])
            if Map[y][x]==8: #if they make it to an 8 they win
                gamePlay=False
                return(gamePlay)                 
    return

			
#a function that adds fruit into random places around the left half of  map		
def add_fruit():
    #to place the appples randomly
    random_y_apple= random.randint(2,len(Map)-2)
    random_x_apple= random.randint(1,5)
    Map[random_y_apple][random_x_apple]=5


#a function that adds planks into random places around the left half of map    
def add_planks():
    # to place the planks randomly
    random_y_plank= random.randint(2,len(Map)-2)
    random_x_plank= random.randint(1,5)
    Map[random_y_plank][random_x_plank]=2
    
    
#to check if the player collected apples
def check_collisions(x,y):
    global inventory
    if Map[y][x]==5:
        Map[y][x]=0
        inventory[0][1]=inventory[0][1]+1
        add_fruit()
        

#print the players inventory before each turn
def print_inventory():
    for x in range(0,len(inventory)):
        print("you have", inventory[x][1],inventory[x][0])


#place power up in specific spot with 50% chance of spawning
def place_power_up():
    powerUp=random.randint(0,10)
    if powerUp<5:
        Map[4][2]=0
    return

#functions that checks first if you have the power up, then executes its purpose for 5 moves
def power_up(x,y):
    global powerUpTurn,power

    if Map[y][x]==6:
        print(eventList[Map[y][x]][2])
        Map[y][x]=0
        power=True
        
    if power==True:
        print("you have",powerUpTurn,"moves left for your power up.")
        powerUpTurn=powerUpTurn-1
        if powerUpTurn<0:
            power=False
            
        return
    return


##MAIN PROGRAM##
        
#Set our starting location
currX = 1
currY = 4

#start the game if they want to play
game=starting_statements()
if game=="y":
    gamePlay=True

#change three of the spots on the map to a fruit and one to a power up if chance is greater that 50%
place_power_up()
for fruit in range(0,4):
    add_fruit()
    
for planks in range(0,4):
    add_planks()
    
#draw the map the first time before asking for a move
drawMap(currX, currY)

#Let the player move around the map on the path until they reach the end of the game
while gamePlay==True:
    check_Event(currX,currY)
    check_collisions(currX,currY)
    print_inventory()
    moveDir = input("Enter direction (u,d,l,r): ")
    currX, currY = movePlayer(currX, currY, moveDir)
    drawMap(currX, currY)
    
