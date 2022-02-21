# yazhee dice-throing game see wikipedia: https://en.wikipedia.org/wiki/Yahtzee
# for github, see: https://github.com/horstjens/yacht-dice-game
# license: GPL3, 2022 by Horst JENS, horstjens@gmail.com https://spielend-programmieren.at

import random
from dataclasses import dataclass

def howmuch(x: int) -> int:
    """Returns how often the value x is inside temp."""
    return temp.count(x)

def is_yahtzee() -> bool:
    """Returns True if temp has 5 equal numbers."""
    if temp[0] == temp[1] == temp[2] == temp[3] == temp[4]:
        return True
    return False   # else: is not necessary because previous line was a return statement

def is_small_straight() -> bool:
    """Returns True if Four sequential dice (1-2-3-4, 2-3-4-5, or 3-4-5-6) are in temp."""
    if (3 in temp) and (4 in temp):
        if (1 in temp) and (2 in temp):
            return True
        if (2 in temp) and (5 in temp):
            return True
        if (5 in temp) and (6 in temp):
            return True
    return False

def is_large_straight() -> bool:
    """Returns True if Five sequential dice are in temp (1-2-3-4-5 or 2-3-4-5-6)."""
    if (2 in temp) and (3 in temp) and (4 in temp) and (5 in temp):
        if (1 in temp) or (6 in temp):
            return True
    return False

def four_of_a_kind() -> int:
    """Returns sum of all dice if at least four dice are the same."""
    for x in (1,2,3,4,5,6):
        if temp.count(x) >= 4:
            return sum(temp)
    return 0

def three_of_a_kind() -> int:
    """Returns sum of all dice if at least three dice are the same."""
    for x in (1,2,3,4,5,6):
        if temp.count(x) >= 3:
            return sum(temp)
    return 0

def chance() -> int:
    return sum(temp)

def is_full_house() -> bool:
    """Returns True if if temp is a full house (3 equals and 2 equals)."""
    for x in (1,2,3,4,5,6):
        for y in (1,2,3,4,5,6):
            if y==x:
                continue
            if howmuch(x) == 3 and howmuch(y) == 2:
                return True
    return False

def calculate_points(cat:any, joker_rules=False) -> int:
    """Takes a dataclass category instance and  returns the points."""
    function = cat.function
    number = cat.number
    if cat.name in ("Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"):
        points = function(number) * number
    else:
        if joker_rules and (cat.name in ("Full House", "Small Straight", "Large Straight")):
            points = cat.max_points
        else:
            points = function() * number
    return points

def ask(joker_rules=False) -> any:
    """Ask player what category he wants to play. Returns a category instance."""
    for number, cat in enumerate(categories2, 1):  # iterating over the values of dictionary
        if not cat.played: # same as: if categories2[cat].played == False
            # --- calculate points for each possible category
            points = calculate_points(cat, joker_rules)
            jokertext = "(joker)" if (cat.name in ("Full House", "Small Straight", "Large Straight")) and joker_rules else "       "
            print("{:>2}: {:<16} {}--> {:>2} points of max. {:>2}".format(number,cat.name, jokertext,  points, cat.max_points)) #{:>2} forces a leading space on numbers smaller than 10
    while True:
        command = input("wich category do you want to play? >>>")
        # ---- guardians: validate the input -----
        try:
            index = int(command)
        except:
            print("This was not a number, please try again")
            continue  # back to the start of the while loop
        # the player entered a number, but was it a valid number?
        if not (1 <= index <= len(categories2)):
            print("Number must be between 1 and {}, please try again".format(len(categories2)))
            continue
        my_cat = categories2[index-1] # because index start always with 0 in python
        if my_cat.played:
            print("Please choose a category that was not already played")
            continue
        # ---- input has passed all guardians ------
        return my_cat
    # -------- end of while loop -------

def roll() -> list:
    """Roll the dice three times, returns temp array with dice values."""
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
        if "j" in command:
            die1, die2, die3, die4, die5 = 1,1,1,1,1
        rolls.append([die1, die2, die3, die4, die5])
        print("       +---+---+---+---+---+")
        print("throw# | a | b | c | d | e |")
        for t, line in enumerate(rolls, start=0):
            print("       +---+---+---+---+---+")
            print("       | {} | {} | {} | {} | {} |".format( *[unicode_lookup[x] for x in rolls[t]]))
            print("  {}:   | {} | {} | {} | {} | {} |".format(t+1, *rolls[t]))
        print("       +---+---+---+---+---+")
        if throw < 3:
            print("please enter the letter(s) for dice that should roll again (like acd):")
            command = input(">>>")
        else:
            print("  ==========================")
            return [die1,die2, die3, die4, die5]
    # ------- end of for loop ---------

@dataclass
class Cat:
    """A class to hold categories that the user can play."""
    name: str
    function: any  # function object as attribute
    number: int
    max_points: int
    played: bool = False # default value = False
    scored: int = 0      #


    def __post_init__(self) -> None:
        """Appends the newly created class instance to the list 'categories2'."""
        categories2.append(self)


# ------ main program starts here ----------
temp = []
score = 0
categories2 = [] # empty list

unicode_lookup = {
    1: "\u2680",
    2: "\u2681",
    3: "\u2682",
    4: "\u2683",
    5: "\u2684",
    6: "\u2685",
}

Cat(name="Ones", function=howmuch, number=1, max_points=5, played=False, scored=0  )
Cat("Twos", howmuch, 2, 10)
Cat("Threes", howmuch, 3, 15)
Cat("Fours", howmuch, 4, 20),
Cat("Fives", howmuch, 5, 25),
Cat("Sixes", howmuch, 6, 30)
Cat("Full House", is_full_house, 25, 28) # 3 x 6  + 2 x 5 = 28
Cat("Three-Of-A-Kind", three_of_a_kind, 1, 30) # 5 x 6
Cat("Four-Of-A-Kind", four_of_a_kind, 1,  30) # 5 x 6
Cat("Small Straight", is_small_straight, 30, 30)
Cat("Large Straight", is_large_straight, 40, 40)
Cat("Choice", chance, 1, 30) # 5 x 6
Cat("Yahtzee", is_yahtzee, 50,50)

bonus = 0
for turn in range(1, len(categories2)+1):
    joker = False
    temp = roll()
    temp.sort() # yatzee special rules
    yahtzee = categories2[-1] # the last one
    if is_yahtzee():
        # ------ rule 0: if a yatzee is first rolled and not played already it must be taken as yatzee
        if not yahtzee.played:
            print("==================----------------------------==================")
            print("*-*-*-*-*-*-*-*-*------- first Yatzee !!! -----*-*-*-*-*-*-*-*-*")
            print("==================----------------------------==================")
            print(".......................      {} points !  ......................".format(yahtzee.number))
            score += yahtzee.number
            yahtzee.played = True
            yahtzee.scored = yahtzee.number
            continue #
        elif yahtzee.played and (yahtzee.scored != 0):
            print("==================----------------------------==================")
            print("........................ INCREDIBLE!!!..........................")
            print("*-*-*-*-*-*-*-*------- another Yatzee !!! -----*-*-*-*-*-*-*-*-*")
            print("==================----------you get ----------==================")
            print(".......................  100 bonus points !  ...................")

            score += 100
            # free joker rule: if upper section is already used,
            # yatzee can act as a joker for full houes, small straight and large straight
            # is upper section used?
            eyes = temp[0]
            if categories2[eyes - 1].played:
                print("....... AND you can choose a category with JOKER rules..........")
                joker = True
            else:
                print("....... AND you can choose a category (but without JOKER rules).")
                joker = False
            print("==================----------------------------==================")




        # yathzee joker rule #1: If the corresponding Upper Section box is unused then that category must be used.

    my_cat = ask(joker)
    print("You play: ", my_cat.name)
    #temp = [die1, die2, die3, die4, die5]
    temp.sort()
    function = my_cat.function
    number = my_cat.number
    points = calculate_points(my_cat, joker)
    print("you get", points, "points")
    score += points
    # ------------------------  update scored and played ----------
    my_cat.played = True
    my_cat.scored = points

# -------------------
print("*-*-*-=== summary of this game ===-*-*-*")
print("category           points: scored / max.")
for cat in categories2:
    print("{:<20}: reached {:>2} of {:>2}".format(cat.name, cat.scored, cat.max_points))
print("your final score is:", score)
print("maximum possible score is: 297")
print("you reached {:.2f} % of the maximum score".format(score / 297 * 100))
