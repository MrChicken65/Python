replayPrompt = 'y'

def guessANumber():
    start = 1
    end = 100

    print(f"Pick a number between {start} and {end}.")
    print("I will guess it in as few guesses as possible!")

    guess = (end + start) // 2
    response = input(f"is {str(guess)} too high, too low, or correct?")
    response = response.lower()

    while response != 'correct':
        if response == 'too high':
            end = guess - 1
        else: #Response == 'too low'
            start = guess + 1

        guess = (end + start) // 2
        response = input(f"Is {guess} too high, low, or correct?")
        response = response.lower()

    print(f"Your number is {guess}.")
    replayChoice = input("Play again? (y/n)")
    return replayChoice


def nim():
    pile = 15
    print(f"The pile has {pile} stones")

    winner = ""
    while pile != 0:
        c1Move = randomMove(pile)
        pile = pile - c1Move
        print(f"Random Randy takes {c1Move} stone(s). Pile is now {pile}")
        if pile == 0:
            winner = "Random Randy"
        else:
            c2Move = nimbleMove(pile)
            pile = pile - c2Move
            print(f"Nimble Nacy takes {c2Move} stone(s). Pile is now {pile}")
            if pile == 0:
                winner = "Nimble Nancy"
    print(f"The winner is {winner}!")
    replayChoice = input("Play again? (y/n)")
    return replayChoice

def randomMove(pile):
    import random
    move = random.randint(1, 3)
    if move > pile:
        move = pile

    return move

def nimbleMove(pile):
    if pile % 4 != 0:
        move = pile % 4
    else:
        move = 1

    return move

gameChoice = input("Would you like to play guess a number (a) or nim (b)? (type a/b)")


if gameChoice == "a":
    while replayPrompt != "n":
        replayPrompt = guessANumber()
elif gameChoice == "b":
    while replayPrompt != "n":
        replayPrompt = nim()
else:
    print("Error: lease make a valid selection.")

