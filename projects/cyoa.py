"""Project 00: Guess a number 1-3!!!"""
__author__ = "730228276"

from random import randint

points: int = 0
number: int = 0
player: str = "name"
random: int = 0
NAMED_CONSTANT: str = '\U00000000'


def main() -> None:
    """This is the main function.""" 
    greet()
    global points
    points = 0
    print("Hello, " + player)
    global random
    random = randint(1, 3)
    print(random)
    global number
    number = int(input("Please choose a number: 1, 2, 3, or enter 0 to exit the game. "))
    
    if number == 0:
        print("Game exited. You earned 0 adventure points. Goodbye ")

    while number > 0:
        if number == random:
            correct()
            congrats(points)
        else:
            if number > random:
                guess()
            else:
                if number < random:
                    guess2()
        number = 0

        
def greet() -> None:
    """Welcoming my player!"""
    print("Let's play a game! I am thinking of a number 1-3. You have to guess which number it is!")
    global player
    player = input("What is your name? ")


def correct() -> None:
    """You guessed correctly!"""
    global points
    points = points + 1


def guess() -> None:
    """Guess Lower!"""
    global number
    global random
    while number != random:
        print(player + ", Guess lower! ")
        number = int(input("New guess: "))
    global points
    points = points + 1
    congrats(points)
        

def guess2() -> None:
    """Guess Higher!"""
    global number
    global random
    while number != random:
        print(player + ", Guess higher!")
        number = int(input("New guess: "))
    global points
    points = points + 1
    congrats(points)
  

def congrats(x: int) -> int:
    """Congrats, you won!"""
    print(player + ", You guessed correctly! You earned 1 adventure point. Goodbye! ")
    return points


if __name__ == "__main__":
    main()