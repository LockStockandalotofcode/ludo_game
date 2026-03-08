from random import randint

class Die:
    dice_output_max = 6

    @staticmethod
    def roll_die():
        roll = randint(1, Die.dice_output_max)
        print(f"Die roll: {roll}")
        return roll
    
# roll = Die.roll_die()
# print(roll)