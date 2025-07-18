# This is a simple rock paper scissor game #

# module's os.path will help me check if score file exist or not and random for random
import os.path
import sys
import random

# this function will give me score

def getscore(pls, cms):
    print("\nYour score is", pls)
    print("Computer score is", cms)

#This function will get score from stored file
# first score(cms) is of computer and second(pls) player

def Getfilescore():
    global cms
    global pls
    scf = open("Score(R.P.S).txt", "r")
    sc = scf.readlines()
    cms = int(sc[0])
    pls = int(sc[1])
    scf.close()


# this function saves score, ss = save score

def ss(cms, pls):
    scf = open("Score(R.P.S).txt", "w")
    scf.write(str(cms) + "\n" + str(pls))
    scf.close()


#Generated this code with Chat GPT
#//////////
# Get the directory of the currently running script
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Change the current working directory to that directory
os.chdir(script_dir)
#//////////


#this sets both scoce to zero initially
cms=0
pls=0


# This is game start

print("Welcome to R.P.S")

# This will check if score file exist it will do nothing if file does not exit then it will create a score file

if os.path.isfile('./Score(R.P.S).txt'):
    pass
else:
    scf = open("Score(R.P.S).txt", "x")
    scf.close()
    print("Your score got deleted.")

# This will take score from file, first score in file is of computer and second player
# first score(cms) is of computer and second(pls) player

try:
    Getfilescore()
except IndexError:
    ss(0,0)

# This will show previous score if both score is zero/got deleted it will show nothing
# it will also ask to reset score if any
# rr = reset respond


if cms == 0 and pls == 0:
    print("Both score are 0.")
else:
    print("\nYour score is", pls)
    print("Computer score is", cms)
    rr = str(input("Do you want to reset score, Press/Enter Y for Yes and anything else for No\n")).upper()
    if rr == "Y":
        cms = 0
        pls = 0
        ss(cms, pls)
    else:
        pass


# this function is game


def round(cms=cms, pls=pls):
    pc = ("R", "P", "S")  # pc possible choice
    nround = 0  # which round i am number of round
    while nround < 5:
        # this the part that will take mt and computer input and and see who won and add scor and which round i am in
        playerm = str(input("Chose your move.(R/P/S)\n")).upper()
        cmm = random.choice(pc)
        if playerm == "R" and cmm == "R":
            print(playerm, cmm)
            print("Tie")
            nround += 1
        elif playerm == "R" and cmm == "P":
            print(playerm, cmm)
            print("Computer won")
            cms += 1
            nround += 1
        elif playerm == "R" and cmm == "S":
            print(playerm, cmm)
            print("You won")
            pls += 1
            nround += 1
        elif playerm == "P" and cmm == "R":
            print(playerm, cmm)
            print("You won")
            pls += 1
            nround += 1
        elif playerm == "P" and cmm == "P":
            print(playerm, cmm)
            print("Tie")
            nround += 1
        elif playerm == "P" and cmm == "S":
            print(playerm, cmm)
            print("Computer won")
            cms += 1
            nround += 1
        elif playerm == "S" and cmm == "R":
            print(playerm, cmm)
            print("Computer won")
            cms += 1
            nround += 1
        elif playerm == "S" and cmm == "P":
            print(playerm, cmm)
            print("You won")
            pls += 1
            nround += 1
        elif playerm == "S" and cmm == "S":
            print(playerm, cmm)
            print("Tie")
            nround += 1
        else:
            continue
    getscore(pls, cms)

    #this is if i want to play more than one round
    #pa = play another round

    pa = str(input("Do you want to play another round. Press/Enter Y for yes and anything else for exit and save.\n")).upper()
    if pa == "Y":
        round(cms, pls)
    else:
        ss(cms, pls)


# game start, gs = game start


gs = str(input("Press/Enter Y to start game and anything else to exit.\n")).upper()
if gs == "Y":
    print("R = rock, p = paper, s = siccor.")
    round()
else:
    pass
