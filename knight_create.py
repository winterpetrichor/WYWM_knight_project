# import random for shuffle to randomize distribution of attribute points
import random

# import local modules
from attr_edit import edit_attr
from knight_menu import show_menu

# knight class to hold number, name and attibutes
class Knight:
    def __init__(self, k_num, k_name, k_attr): #, knights_data):
        self.k_num = k_num
        self.k_name = k_name
        self.k_attr = k_attr
        ####### DOES KNIGHTS_DATA NEED TO EXIST?
        # self.knights_data = knights_data

    def create_knight(chars, knights, knight_chars, total_points, kc):
        # knights_data = []
        k_attr={}
        kc=[0]*chars
        # knights_data.append(len(knights)+1)
        k_num = len(knights)+1
        print("")
        k_name = str(input("What is your Knight's name: "))
        # knights_data.append(k_name)
        points = total_points
        while points > 0:
            kc[0] += 1
            random.shuffle(kc)
            points -=1
                
        for i in range(chars):
            k_attr[knight_chars[i]]=kc[i]

        # knights_data.append(k_attr)
        # knights.append(knights_data)
        
        print("")
        print("Welcome to the Royal army, Sir " + k_name)
        print("-- Attributes --")
        for attr in k_attr:
            print(str(attr) + " = " + str(k_attr[attr]))

        return(k_num, k_name,k_attr)#,knights_data)

    def print_knight(self):
        print("")
        print(str(self.k_num) + ": " + str(self.k_name))
        for i in self.k_attr:
            print("    " + str(i) + ": " + str(self.k_attr[i]))
        # print(self.knights_data)


# call for this when you want to create a new knight
def create_knight(knights, knight_chars, chars, total_points, kc):

    knights.append(Knight(*(Knight.create_knight(chars, 
                                                 knights, 
                                                 knight_chars, 
                                                 total_points, 
                                                 kc))))

    print("")
    print("- Would you like to re-train Sir " + knights[-1].k_name + "?")

    if show_menu("yn") == "yes":
        edit_attr(knight_chars, chars, total_points, kc, knights[-1], knights)

    else:
        pass

if __name__ == "__main__":
    import knight_master