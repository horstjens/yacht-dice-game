import random
from dataclasses import dataclass
# yacht dice-throing game see wikipedia: https://en.wikipedia.org/wiki/Yacht_(dice_game)
# for github, see: https://github.com/horstjens/yacht-w-rfelspiel/blob/main/main.py
# for repl, see: https://replit.com/@horstjens/yacht-wurfelspiel#main.py

# ---- useful functions ---
temp = []
score = 0

def howmuch(x):
    """returns how often the value x is inside temp"""
    #print("calling howmuch with", x, "of array", temp)
    return temp.count(x)

def is_yacht():
    """returns True if temp has 5 equal numbers"""
    if temp[0] == temp[1] == temp[2] == temp[3] == temp[4]:
        return True
    return False   # else: is not necessary because previous line was a return statement

def is_straight(start_value:int=1):
    """returns True if array is a straight
    param start_value: 1 or 2. 1 for small straight, 2 for big straight
    """
    if start_value == 1:
        return True if temp == [1,2,3,4,5] else False
    elif start_value == 2:
        return True if temp == [2,3,4,5,6] else False
    raise ValueError("start_value must be 1 or 2")

def small_straight():
    return is_straight(start_value=1 )

def big_straight():
    return is_straight(start_value=2 )

def four_of_a_kind():
    """returns dice value times 4 if the dice value exist 4 (or 5)  times in temp,
       otherwise return 0"""
    for x in (1,2,3,4,5,6):
        if temp.count(x) >= 4:
            return x * 4
    return 0

def choice():
    return sum(temp)

def full_house():
    """returns all dice values if temp is a full house (3 equals and 2 equals)"""
    for x in (1,2,3,4,5,6):
        for y in (1,2,3,4,5,6):
            if y==x:
                continue
            if howmuch(x) == 3 and howmuch(y) == 2:
                return sum(temp)
    return 0


categories2 = [] # empty list
@dataclass
class Cat:
    name: str
    function: any  # function object
    number: int
    played: bool = False # default value = False

    def __post_init__(self):
        categories2.append(self) # append this instance into categories2 list

Cat(name="Ones", function=howmuch, number=1, played=False  )
Cat("Twos", howmuch, 2)
Cat("Threes", howmuch, 3)
Cat("Fours", howmuch, 4),
Cat("Fives", howmuch, 5),
Cat("Sixes", howmuch, 6)
Cat("Full House", full_house, 1)
Cat("Four-Of-A-Kind", four_of_a_kind, 1),
Cat("Little Straight", small_straight, 30)
Cat("Big Straight", big_straight, 30)
Cat("Choice", choice, 1)
Cat("Yacht", is_yacht, 50)


def ask():
    """ask player what category he wants to play. returns mycat"""
    for number, cat in enumerate(categories2, 1):  # iterating over the values of dictionary
        if not cat.played: # same as: if categories2[cat].played == False
            print("{:>2}: {}".format(number,cat.name)) #{:>2} forces a leading space on numbers smaller than 10
    while True:
        command = input("wich category do you want to play? >>>")
        # ---- guardians: validate the input -----
        try:
            index = int(command)
        except:
            print("This was not a number, please try again")
            continue  # back to the start of the while loop
        # the player entered a number, but was it a valid number?
        if not (1 <= index <= 12):
            print("Number must be between 1 and 12, please try again")
            continue
        my_cat = categories2[index-1] # because index start always with 0 in python
        if my_cat.played:
            print("Please choose a category that was not already played")
            continue
        # ---- input has passed all guardians ------
        return my_cat
    # -------- end of while loop -------

def roll():
    """roll dice three times, returns temp array with dice values"""
    print("=========================================================")
    print("----- this is turn: {} --------- your score is: {} ------".format(turn, score))
    print("=========================================================")
    rolls = []
    command = "abcde"  # roll all dice
    for throw in (1, 2, 3):
        if "a" in command:
            die1 = random.randint(1, 6)
        if "b" in command:
            die2 = random.randint(1, 6)
        if "c" in command:
            die3 = random.randint(1, 6)
        if "d" in command:
            die4 = random.randint(1, 6)
        if "e" in command:
            die5 = random.randint(1, 6)
        rolls.append([die1, die2, die3, die4, die5])
        #if roll == 1:
        print("       +---+---+---+---+---+")
        print("throw# | a | b | c | d | e |")
        for t, line in enumerate(rolls, start=0):
            print("       +---+---+---+---+---+")
            print("  {}:   | {} | {} | {} | {} | {} |".format(
                    t+1,
                    rolls[t][0],
                    rolls[t][1],
                    rolls[t][2],
                    rolls[t][3],
                    rolls[t][4],
                    ))
        print("       +---+---+---+---+---+")
        if throw < 3:
            print("please enter the letter(s) for dice that should roll again (like acd):")
            command = input(">>>")
        else:
            print("  ==========================")
            return [die1,die2, die3, die4, die5]


for turn in range(1, 13):  # range(1,13) produces the numbers from 1 to 12
    temp = roll()
    my_cat = ask()
    print("You play: ", my_cat.name)
    #temp = [die1, die2, die3, die4, die5]
    temp.sort()
    function = my_cat.function
    number = my_cat.number
    # ------ calculate score --------------
    if my_cat.name in ("Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"):
        points = function(number) * number
    else:
        points = function() * number
    print("you get", points, "points")
    score += points

    # ------------------------  remove selected category ----------
    my_cat.played = True

# -------------------
print("maximum possible score is: 297")
print("your final score is:", score)
print("you reached {:.2f}% of the maximum score".format(score / 297 * 100))
