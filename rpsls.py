import random
import json

# an implementation of Rock Paper Scissors Lizard Spock
# import random because this is important for games.

# this program is not designed for efficiency or clarity at points.
# there are some "teaching" bits to this - which result in redundancy.

# we are using json for the history file




# rules
# Scissors Cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapatate Lizard
# Lizard eats Paper
# Paper disaproves Spock
# Spoke vaporises Rock
# Rock crushes Scissors

outcomes = {
    ('Scissors', 'Paper'): 'cut',
    ('Paper', 'Rock'): 'covers',
    ('Rock', 'Lizard'): 'crushes',
    ('Lizard', 'Spock'): 'poisons',
    ('Spock', 'Scissors'): 'smashes',
    ('Scissors', 'Lizard'): 'decapatate',
    ('Lizard', 'Paper'): 'eats',
    ('Paper', 'Spock'): 'disaproves',
    ('Spock', 'Rock'): 'vaporises',
    ('Rock', 'Scissors'): 'crushes',
}

rock = ["rock", "r", "rk"]
paper = ["paper", "p", "pa"]
scissors = ["scissors", "s", "sc"]
lizard = ["lizard", "l", "li"]
spock = ["spock", "sp"]

gameElts = ["rock", "paper", "scissors", "lizard", "spock"]

computerName = "Computer"
playerName = "Player"

def choiceToName(choice):
    if choice in rock:
        result = rock[0].capitalize()
    elif choice in spock:
        result = spock[0].capitalize()
    elif choice in paper:
        result = paper[0].capitalize()
    elif choice in lizard:
        result = lizard[0].capitalize()
    elif choice in scissors:
        result = scissors[0].capitalize()
    else:
        result = None
    return result


def numberToName(num):
    if num < len(gameElts):
        return gameElts[num]


def loadHistory():
    try:
        with open(historyFile) as jsonFile:
            data = json.load(jsonFile)
            historyData["wld"] = data["wld"]
            historyData["history"] = data["history"]
    except:
        print("No History File")
        historyData["wld"] = {"w": 0, "l": 0, "d": 0}
        historyData["history"] = []


def displayHistory():
    if True: #numberOfGames % 5 == 0 and numberOfGames > 0:
        vHistory = input("Do you want to view your game history? (y/n)")
        if vHistory == "y":
            print("Your game history:")
            print("*" * 20)

            print(f"W:{historyData['wld']['w']} L:{historyData['wld']['l']} D:{historyData['wld']['d']}")
            for h in historyData["history"]:
                print(h)
def writeHistory():
    with open(historyFile, 'w') as outfile:
        json.dump(historyData, outfile)

def getValidChoice():
    validChoice = False
    choice = ""
    while not validChoice:
        choicePrompt = "rock (r), paper (p), scissors (s), lizard (l), spock (sp)? "
        print("*" * len(choicePrompt))
        choice = choiceToName(input(choicePrompt)).capitalize()
        if choice is not None:
            validChoice = True
    return choice

# load history file
# display history (if 5th game)
# input player choice
# generate computer choice
# check who wins
#

# output winner
# save win / loss
# save to history var
# ask if we want to play again
# if not write history file.


historyFile = "rplsHistory.txt"
wld = {"w": 0, "l": 0, "d": 0}
historyList = []
historyData = {}

historyData["wld"] = wld
historyData["history"] = historyList

# attempt to load the history
loadHistory()

isRunning = True
numberOfGames = 0


while isRunning:
    displayHistory()
    playerChoice = getValidChoice()
    computerChoice = numberToName(random.randint(0, len(gameElts)-1)).capitalize()
    prompt = (f"{playerChoice} v {computerChoice}")
    print(prompt)
    print("*" * len(prompt))
    outcome = ""
    if playerChoice == computerChoice:
        outcome = (f"{playerChoice} v {computerChoice}: Draw")
        historyData["wld"]["d"] += 1
    elif (playerChoice, computerChoice) in outcomes:
        outcome = (f'{playerName} win! {playerChoice} {outcomes[playerChoice, computerChoice]} {computerChoice}.')
        historyData["wld"]["w"] += 1
    elif (computerChoice, playerChoice) in outcomes:
        outcome = (f'{computerName} wins! {computerChoice} {outcomes[computerChoice, playerChoice]} {playerChoice}.')
        historyData["wld"]["l"] += 1
    else:
        outcome = (f'Invalid choice {playerChoice}')
    print(outcome)
    historyData["history"].append(outcome)
    print(f"You have {historyData['wld']['w']} wins and {historyData['wld']['l']} losses and {historyData['wld']['d']} draws")
    numberOfGames += 1
    again = input("Do you want to play again? (y/n) ")
    if again == "n":
        isRunning = False
    # write history file
    writeHistory()





