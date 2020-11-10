# BiYing Pan(bp483)
# CS 171-062

import random
random.seed()

# create a setupDoors()
def setupDoors():
    G = 'goat'
    G = 'goat'
    C = 'car'

    doors = ['G', 'G', 'C']
    random.shuffle(doors)
    return doors

# create a playerDoor()
def playerDoor():
     
    return random.randint(1,3)

# create a montyDoor()
def montyDoor(doors, player):
    
    doors = setupDoors()
    player= playDoor()
    
    montyDoor = 0
    while montyDoor == doors['G'] and montyDoor != player:
        montyDoor = random.randint(1,3)
        
    return montyDoor

# create a playRound()
def playRound():
   
    doors = setupDoors()
    player = playerDoor()
    
    if doors[player-1] == 'C':  
        return True
                    
    if doors[player-1] == 'G':
        return False
    
if __name__ =='__main__':
    
    # print title
    print('Welcome to Monty Hall Analysis')
    print('Enter \'exit\' to quit.')

    # stop the program when user enter 'exit' by using the loop
    tests=0   
    while tests != 'exit':
        tests = input('How many tests should we run? ')
        try:
            switchWin = 0
            stayWin = 0
            
            tests = int(tests)
                          
            i = 0
            for i in range(tests):
                result = playRound()
                if result:
                    stayWin += 1
                else:
                    switchWin += 1
   
            stayWinPercent = stayWin/float(tests)*100
            switchWinPercent = switchWin/float(tests)*100
            
            print('Stay Won', stayWinPercent,'% of the time.')
            print('Switch Won', switchWinPercent,'% of the time.')
            
        except ValueError as e:
            if tests != 'exit':
                print('Please enter a number: ')
    print('Thank you for using this program')
