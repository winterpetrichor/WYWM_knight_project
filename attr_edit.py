# author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# import show_menu for y/n menu
from knight_menu import show_menu

# import name_knight to edit knight name, this could have 
# been included here, but done as a separate module for 
# separation of functionality
from knight_name import name_knight

# function to edit each attribute by entering an integer
def each_point(knight, points):
    for i in knight.k_attr:
        try: 
            knight.k_attr[i] = int(input(str(i) + " = "))
            points = points - knight.k_attr[i]
        except: # exceptions displayed by knight_menu function
            print("- Please enter an integer to try again. Starting over... -")
            each_point(knight, points)
            break
    return(points)

# wrapper function for attribute editing
def edit_each(knight, total_points):
    print("")
    print("How would you like to re-educate sir "+ knight.k_name+"?")
    print("- You have a maximum of " + str(total_points) 
          + " to assign. Spend them wisely. -")
    points = total_points
    points = each_point(knight, points)

    # prevent point overspending
    if points < 0:
        print("Out of points! Starting over...")
        edit_each(knight, total_points)
    else:
        print("")
        print("After going through some re-training, Sir " 
                + knight.k_name + " now has the following attributes:")
        for i in knight.k_attr:
            print(str(i) + ": " + str(knight.k_attr[i]))

# function to select the knight to edit
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

# function to oversee knight editing
def edit_attr(total_points, knight, knights):
    if len(knights) == 0:
        print("You have no knights! \
Please create some knights and try again...")
        return
    elif knight == []:
        print("")
        print("-- Please select a knight --")

        # print all knights to allow selection
        for k in knights:
            print(str(k.k_num) + ": " + str(k.k_name))
            for j in k.k_attr:
                print("    " + str(j) + ": " + str(k.k_attr[j]))

        # call sel_knight to allow knight selection input
        sel_knight = sel_knight_func(knights)

        # confirm selection and show "char" menu
        print("You have selected Sir " + str(str(sel_knight.k_name)))
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

# run main module from any submodule
if __name__ == "__main__":
    import knight_master