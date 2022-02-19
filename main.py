import random
# yacht dice-throing game see wikipedia: https://en.wikipedia.org/wiki/Yacht_(dice_game)

categories = [
    "Ones",
    "Twos",
    "Threes",
    "Fours",
    "Fives",
    "Sixes",
    "Full House",
    "Four-Of-A-Kind",
    "Little Straight",
    "Big Straight",
    "Choice",
    "Yacht",
]

score = 0 

for turn in range(1,13): # range(1,13) produces the numbers from 1 to 12
    print("=========================================================")
    print("----- this is turn: {} --------- your score is: {} ------".format(turn, score ))
    print("=========================================================")

    command = "abcde" # roll all dice
    for roll in (1,2,3):
        if "a" in command:
            die1 = random.randint(1,6)
        if "b" in command:
            die2 = random.randint(1,6)
        if "c" in command:
            die3 = random.randint(1,6)
        if "d" in command:
            die4 = random.randint(1,6)
        if "e" in command:
            die5 = random.randint(1,6)

        if roll == 1:
            print("      +---+---+---+---+---+")
            print("roll# | a | b | c | d | e |")
        print("      +---+---+---+---+---+")
        print("  {}   | {} | {} | {} | {} | {} |".format(
            roll,
            die1,
            die2,
            die3,
            die4,
            die5 ))
        print("      +---+---+---+---+---+")
        if roll < 3:
            print("please enter the letter(s) for dice that should roll again (like acd):")
            command = input(">>>")
    # ask player for category
    for number, cat in enumerate(categories,1):
        print(number, ":", cat)
    while True:
        command = input("wich category do you want to play? >>>")
        try:
            index = int(command)
        except:
            print("This was not a number, please try again")
            continue # back to the start of the while loop
        # the player entered a number, but was it a valid number? 
        if not (1 <= index <= 12):
            print("Number must be between 1 and 12, please try again")
            continue
        my_cat = categories[index-1]
        if "already played" in my_cat:
            print("Please choose a category that was not already played")
            continue
        # ---- 
        break # valid choice, exit the while loop
        

    print("You play: ", my_cat)
    temp = [die1, die2, die3, die4, die5]
    temp.sort()

    # --- yacht: 5 equal numbers --> 50 points, otherwise 0 points
    if my_cat == "Yacht" :
        if die1 == die2 == die3 == die4 == die5:
            print("super, you rolled a yacht!  50 points!")
            score += 50
        else:
            print("sorry, no yacht you get0 points")

    # ----- choice: sum of all dice
    if my_cat == "Choice":
        sum_of_dice = sum(temp)    # this is the same as: sum_all = die1+die2+die3+die4+die5
        print("you get", sum_of_dice, "points")
        score += sum_of_dice

    # ------ big straight: 2,3,4,5,6  -> 30 points
    if my_cat == "Big Straight":
        if temp == [2,3,4,5,6]:
            print("You get 30 points")
            score += 30
        else:
            print("sorry, only 0 points")
        
    # ------ littke straight: 1,2,3,4,5  -> 30 points    
    if my_cat == "Little Straight":
        if temp == [1,2,3,4,5]:
            print("You get 30 points")
            score += 30
        else:
            print("sorry, only 0 points")

    # ----- four of a kind: > 4 times the points
    if my_cat == "Four-Of-A-Kind":
        # not elegant:
        # if (die1==die2==die3==die4) or (die2==die3==die4==die5) or ...
        # more elegant:
        for x in (1,2,3,4,5,6):
            howmuch = temp.count(x)
            if howmuch >= 4:
                points= x*4
                print("you get", points, "points")
                score += points
                break # escape the for loop
        else:  # the for loop run through without break
            print("sorry, only 0 points")

    #---- full house: 3 equals and 2 equals - > sum of all dice
    if my_cat == "Full House":
        fullhouse = False
        for x in (1,2,3,4,5,6):
            howmuch1 = temp.count(x)
            for y in (1,2,3,4,5,6):
                if x==y:
                    continue    # jump to start of the for loop, proceed with next y
                howmuch2 = temp.count(y)
                if (howmuch1 == 3) and (howmuch2 == 2):
                    fullhouse = True
                    sum_of_dice = sum(temp) 
                    print("you get", sum_of_dice, "points")
                    score += sum_of_dice
                    break
            if fullhouse:
                break
        else:  # x-loop without break
            print("sorry, only 0 points")
        # TODO: specail case yacht rolled but full house chosen

    # ---- ones : sum of ones
    if my_cat == "Ones":
        howmuch = temp.count(1)
        print("you get", howmuch, "points")
        score += howmuch

    if my_cat == "Twos":
        howmuch = temp.count(2)
        print("you get", howmuch * 2, "points")
        score += howmuch * 2

    if my_cat == "Threes":
        howmuch = temp.count(3)
        print("you get", howmuch * 3, "points")
        score += howmuch * 3

    if my_cat == "Fours":
        howmuch = temp.count(4)
        print("you get", howmuch * 4, "points")
        score += howmuch * 4

    if my_cat == "Fives":
        howmuch = temp.count(5)
        print("you get", howmuch * 5, "points")
        score += howmuch * 5

    if my_cat == "Sixes":
        howmuch = temp.count(6)
        print("you get", howmuch * 6, "points")
        score += howmuch * 6

    # ------------------------  remove selected category ----------
    # (dont really remove, just rename it)
    #my_cat = categories[index-1]
    categories[index-1] += " (already played)"

#-------------------
print("your final score is:", score)