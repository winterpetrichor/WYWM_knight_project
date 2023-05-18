# Author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# Import show_menu for y/n menu
from knight_menu import show_menu

# Import name_knight to edit knight name, this could have 
# been included here, but done as a separate module for 
# separation of functionality.
from knight_name import name_knight

# Function to edit each attribute by entering an integer
def each_point(knight, points):
    for i in knight.knight_attr:
        try: 
            knight.knight_attr[i] = int(input(str(i) + " = "))
            points = points - knight.knight_attr[i]
            print("- You have " + str(points) + " points remaining ... -")
        except: # Exceptions displayed by knight_menu function
            print("- Please enter an integer to try again. Starting over... -")
            each_point(knight, points)
            break
    return(points)

# Wrapper function for attribute editing
def edit_each(knight, total_points):
    print("")
    print("How would you like to re-educate sir "+ knight.knight_name+"?")
    print("- You have a maximum of " + str(total_points) 
          + " to assign. Spend them wisely. -")
    points = total_points
    points = each_point(knight, points)

    # Prevent point overspending
    if points < 0:
        print("Out of points! Starting over...")
        edit_each(knight, total_points)
    else:
        print("")
        print("After going through some re-training, Sir " 
                + knight.knight_name + " now has the following attributes:")
        for i in knight.knight_attr:
            print(str(i) + ": " + str(knight.knight_attr[i]))

# Function to select the knight to edit
def sel_knight_func(knights):
    try: 
        sel_knight_num = int(input("Which knight would you like to update: "))
        if sel_knight_num > len(knights):
            raise IndexError
        else:
            return(knights[sel_knight_num-1])
    except:
        print("- Please enter the number of a knight \
shown above to try again. Starting over... -")
        return(sel_knight_func(knights))

# Function to oversee knight editing
def edit_attr(total_points, knight, knights):
    if len(knights) == 0:
        print("You have no knights! \
Please create some knights and try again...")
        return
    elif knight == []:
        print("")
        print("-- Please select a knight --")

        # Print all knights to allow selection
        for k in knights:
            print(str(k.knight_num) + ": " + str(k.knight_name))
            for j in k.knight_attr:
                print("    " + str(j) + ": " + str(k.knight_attr[j]))

        # Call sel_knight to allow knight selection input
        sel_knight = sel_knight_func(knights)

        # Confirm selection and show "char" menu
        print("You have selected Sir " + str(str(sel_knight.knight_name)))
        print("")
        edit_choice = show_menu("char")
        if edit_choice == "name":
            sel_knight = name_knight(sel_knight)
        elif edit_choice == "attr":
            edit_each(sel_knight, total_points)
        elif edit_choice == "cancel":
            print("Returning to the Main Menu... ")
        return
    else:
        edit_each(knight, total_points)

# Run main module from any submodule
if __name__ == "__main__":
    import knight_master