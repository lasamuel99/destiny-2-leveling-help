from enum import Enum
import math

class Armor(Enum):
    PRIMARY = 1
    SECONDARY = 2
    HEAVY = 3
    HELMET = 4
    ARMS = 5
    CHEST = 6
    LEGS = 7
    CLASS = 8

def create_dictionary(gear):
    return {
        Armor.PRIMARY: gear[0],
        Armor.SECONDARY: gear[1],
        Armor.HEAVY: gear[2],
        Armor.HELMET: gear[3],
        Armor.ARMS: gear[4],
        Armor.CHEST: gear[5],
        Armor.LEGS: gear[6],
        Armor.CLASS: gear[7]
    }

def current_light(gear_dict):
    return sum(gear_dict.values())/8

def even_out(gear_dict):
    current = math.floor(current_light(gear_dict))

    potential_gear = gear_dict.copy()

    for k, v in potential_gear.items():
        if v < current:
            potential_gear[k] = current
    
    return current_light(potential_gear)