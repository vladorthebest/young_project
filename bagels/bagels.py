import random


class Bugels():
    """ Game bugels!!!
    The player must guess a number from 100 - 999.

    The game has hints:
    1. Fermi - The right number in the right place
    2. Pico - The right number in the wrong place
    3. Bugels - The wrong number

    class have 1 function:
        turn(number_player)
    """


    def __init__(self):
        """ Ganerate number 100-999 """

        create = lambda x: random.randint(x, 9)
        self.number = list(map(create, [1,0,0]))
        
        self.status = None


    def turn(self, number_p):
        """ Return True - if all number right
        Return False - if not all number right

        self.status - hint

        """

        number_p = list(map(lambda x: int(x),list(number_p)))
        self.status = None
        fermi = False
        pico = False

        for index, cislo_p in enumerate(number_p):
            if cislo_p in self.number:
                if cislo_p == self.number[index]:
                    fermi = True
                else:
                    pico = True

        if fermi == True:
            self.status = 'Fermi'
        elif pico == True:
            self.status = 'Pico'  
        else:
            self.status = 'Bagels'     
                
        
        if number_p  == self.number:
            return True
        else:
            return False


def number_check(number):
    """ checks the player's number """
    if len(number) == 3:
        
        try:
            number = int(number)
            return True
        except:
            return False
    else:
        return False



bugels = Bugels() # Create number
turn = 0 # turn counter
while True:   
    turn += 1
    
    number_player = input(f'\nTurn {turn}. Your number: ') # player input number 

    if number_check(number_player): #check number
        end = bugels.turn(number_player)  #turn game (check number player and number game)
        print(bugels.status)

        if end:
            print('You WIN!!!')
            break

        elif turn == 10:
            print('You LOSE!!!')
            break
    else: 
        print('You must enter a number from 100-999!!!')
