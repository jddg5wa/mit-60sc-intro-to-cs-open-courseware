import random

def dice_roll(diceSides):
    return random.randint( 1, diceSides)

def all_same(items):
    return all(x == items[0] for x in items)

def yahtzee( numTrails, rollsPerTrial, diceSides, firstNum):

    diceRolls = []

    for x in range(numTrails):
        roll = []
        # roll.append(firstNum)

        for x in range(rollsPerTrial):
            roll.append(dice_roll(diceSides))
            # print roll

        # print all_same(roll)
        if all_same(roll):
            diceRolls.append(roll)

    probYahtzeeRoll = float(len(diceRolls))/numTrails
    # print diceRolls
    return probYahtzeeRoll*100

# print diceRoll(6)
print yahtzee( 1000000, 5, 6, dice_roll(6))