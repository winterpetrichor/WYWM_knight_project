# author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# import random for shuffle to randomize distribution of attribute points
import random

# import local modules
from attr_edit import edit_attr
from knight_menu import show_menu

# knight class to hold number, name and attibutes
class Knight:
    def __init__(self, k_num, k_name, k_attr):
        self.k_num = k_num
        self.k_name = k_name
        self.k_attr = k_attr

    # function to create knight, assign number and generate attributes
    def create_knight(chars, knights, knight_chars, total_points, kc):
        
        # attribute dictionary
        k_attr={}

        # start with 0's for each attribute
        kc=[0]*chars

        # start from 1 instead of 0
        k_num = len(knights)+1 

        print("")
        k_name = str(input("What is your Knight's name: "))
        points = total_points
        
        # loop to randomly increment attribute points
        while points > 0:
            kc[0] += 1
            random.shuffle(kc)
            points -=1
                
        # populate attributes with values
        for i in range(chars):
            k_attr[knight_chars[i]]=kc[i]
        
        # creation confirmation, show name and attributes
        print("")
        print("Welcome to the Royal army, Sir " + k_name)
        print("-- Attributes --")
        for attr in k_attr:
            print(str(attr) + " = " + str(k_attr[attr]))
        return(k_num, k_name,k_attr)

    # function to print knight, not used in the modules
    # just preserved to print class attributes if required in future
    def print_knight(self):
        print("")
        print(str(self.k_num) + ": " + str(self.k_name))
        for i in self.k_attr:
            print("    " + str(i) + ": " + str(self.k_attr[i]))

# call for this when you want to create a new knight
def create_knight(knights, knight_chars, chars, total_points, kc):

    # create knight using Knight class function and append to "knights" list
    knights.append(Knight(*(Knight.create_knight(chars, 
                                                 knights, 
                                                 knight_chars, 
                                                 total_points, 
                                                 kc))))

    # prompt to "re-train" (assign custom attributes)
    print("")
    print("- Would you like to re-train Sir " + knights[-1].k_name + "?")

    # always update knight_menu/menu_tup_main/edit_attr line
    # when updating the edit_attr args below
    if show_menu("yn") == "yes":
        edit_attr(total_points, knights[-1], knights)

    else:
        pass

# run main module from any submodule
if __name__ == "__main__":
    import knight_master