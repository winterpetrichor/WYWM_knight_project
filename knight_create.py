# Author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# Import random for shuffle to randomize distribution of attribute points
import random

# Import local modules
from attr_edit import edit_attr
from knight_menu import show_menu

# Knight class to hold number, name and attibutes
class Knight:
    def __init__(self, knight_num, knight_name, knight_attr):
        self.knight_num = knight_num
        self.knight_name = knight_name
        self.knight_attr = knight_attr

    # Function to create knight, assign number and generate attributes
    def create_knight(chars, knights, knight_chars, total_points, knight_chars_point_list):
        
        # Attribute dictionary
        knight_attr = {}

        # Start with 0's for each attribute
        knight_chars_point_list = [0]*chars

        # Start from 1 instead of 0
        knight_num = len(knights)+1 

        print("")
        knight_name = str(input("What is your Knight's name: "))
        points = total_points
        
        # Loop to randomly increment attribute points
        while points > 0:
            knight_chars_point_list[0] += 1
            random.shuffle(knight_chars_point_list)
            points -=1
                
        # Populate attributes with values
        for i in range(chars):
            knight_attr[knight_chars[i]] = knight_chars_point_list[i]
        
        # Creation confirmation, show name and attributes
        print("")
        print("Welcome to the Royal army, Sir " + knight_name)
        print("-- Attributes --")
        for attr in knight_attr:
            print(str(attr) + " = " + str(knight_attr[attr]))
        return(knight_num, knight_name, knight_attr)

    # Function to print knight, not used in the modules.
    # Just preserved to print class attributes if required in future.
    def print_knight(self):
        print("")
        print(str(self.knight_num) + ": " + str(self.knight_name))
        for i in self.knight_attr:
            print("    " + str(i) + ": " + str(self.knight_attr[i]))

# Call for this when you want to create a new knight
def create_knight(knights, knight_chars, chars, total_points, kc):

    # Create knight using Knight class function and append to "knights" list
    knights.append(Knight(*(Knight.create_knight(
        chars, knights, knight_chars, 
        total_points, kc))))

    # Prompt to "re-train" (assign custom attributes)
    print("")
    print("- Would you like to re-train Sir " + knights[-1].knight_name + "?")

    # Always update knight_menu/menu_tup_main/funcs["edit_attr"] line
    # when updating the edit_attr args below.
    if show_menu("yn") == "yes":
        edit_attr(total_points, knights[-1], knights)

    else:
        pass

# Run main module from any submodule
if __name__ == "__main__":
    import knight_master