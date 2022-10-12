import random

limb_lst = ["Right hand", "Left hand", "Right foot", "Left foot"]

color_lst = ["Green", "Red", "Yellow", "Blue"]

limb_num = random.randint(0, (len(limb_lst) - 1))

color_num = random.randint(0, (len(color_lst) - 1))

print(f"You should put your {limb_lst[limb_num]} on {color_lst[color_num]}.")