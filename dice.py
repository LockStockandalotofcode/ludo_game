from random import randint

class Die:
    def __init__(self):
        self.dice_output_max = 6

    def roll_die(self):
        roll = randint(1, self.dice_output_max)
        print(f"Die roll: {roll}")
        return roll
    
# roll = Die.roll_die()
# print(roll)