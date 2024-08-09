from art import logo, vs
from game_data import data as dt
import random
def generate_Random_Data():
    """"Generates a random integer that will be used as an index to the list of game_data"""
    randomNum = random.randint(0, len(dt)-1)
    randomData = dt[randomNum]

    return randomData

def compareFollowCount(personA, personB, answer):
    """Compares the value of the First Choice and Second Choice
    and gets the answer provided by the user
    then returns that value as a list if the answer is correct
    else it returns as False which will end the game"""
    if answer == 'a':
        answerFC = personA["follower_count"]
        otherFC = personB["follower_count"]
        if answerFC > otherFC:
            return personA
        else:
            return False
    elif answer == 'b':
        answerFC = personB["follower_count"]
        otherFC = personA["follower_count"]
        if answerFC > otherFC:
            return personB
        else:
            return False

score = 0
personA = generate_Random_Data()

def game(score,personA):
    """Initiates the game. Will run as long as the answer is correct. Once wrong, the game will end show the final score."""
    playGame = True
    print(logo)
    while playGame:
        print(f"Compare A: {personA["name"]}, {personA["description"]} from {personA["country"]}")

        print(vs)

        personB = generate_Random_Data()
        #Checks if the random data is the same with Person A, if so, Person B will be assigned a new random data
        if personA == personB:
            personB = generate_Random_Data()

        print(f"Compare B: {personB["name"]}, {personB["description"]} from {personB["country"]}")

        # Will get an answer from the user
        answer = input("Who has more followers? Type 'A' or 'B':\n").lower()

        if (answer == "a" or answer == "b"): #Check if the provided answer is a valid character
            winner = compareFollowCount(personA, personB, answer)
            if winner != False:
                personA = winner
                score += 1
                print("\n" * 100) #a workaround for clear screen since that doesn't seem to work on PyCharm
                print(f"That answer is correct! Current Score:{score}")
            else:
                playGame = False
                print("\n"*100) #a workaround for clear screen since that doesn't seem to work on PyCharm
                print(f"Sorry, that's wrong. Final Score:{score}")

        else:
            print("You have entered an invalid choice!")

game(score, personA)
