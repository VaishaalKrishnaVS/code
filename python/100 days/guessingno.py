from random import randint

EASY_LEVEL = 10   #global variables
HARD_LEVEL = 5  #global variables

def check_answer(guess, answer,turns):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        
def set_dificulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print("Choose a difficulty. Type 'easy' or 'hard':  ")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turns = set_dificulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer is {answer}")
            return
        elif guess!= answer:
            print("Guess Again")

game()