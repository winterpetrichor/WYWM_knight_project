from knight_menu import show_menu
from knight_name import name_knight

def each_point(knight, points):
    for i in knight.k_attr:
        try: 
            knight.k_attr[i] = int(input(str(i) + " = "))
            # print(str(i) + " = " + str(knights_data[2][i]))
            points = points - knight.k_attr[i]
        except:
            print("- Please enter an integer to try again. Starting over... -")
            each_point(knight, points)
            break
    return(points)
    
def edit_each(knight, total_points):
    print("")
    print("- You have a maximum of " + str(total_points) 
          + " to assign. Spend them wisely. -")
    points = total_points
    points = each_point(knight, points)
    if points < 0:
        print("Out of points! Starting over...")
        edit_each(knight, total_points)
    else:
        print("")
        print("After going through some re-training, Sir " 
                + knight.k_name + " now has the following attributes:")
        for i in knight.k_attr:
            print(str(i) + ": " + str(knight.k_attr[i]))

def sel_knight_func(knights):
    # print(knights)
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

def edit_attr(knight_chars, chars, total_points, kc, knight, knights):
    if len(knights) == 0:
        print("You have no knights! \
Please create some knights and try again...")
        return
    elif knight == []:
        print("")
        print("-- Please select a knight --")
        for k in knights:
            print(str(k.k_num) + ": " + str(k.k_name))
            for j in k.k_attr:
                print("    " + str(j) + ": " + str(k.k_attr[j]))
        sel_knight = sel_knight_func(knights)
        print("You have selected Sir " + str(str(sel_knight.k_name)))
        print("")
        edit_choice = show_menu("char")
        if edit_choice == "name":
            sel_knight = name_knight(sel_knight)
        elif edit_choice == "attr":
            edit_each(sel_knight, total_points)
        elif edit_choice == "cancel":
            print("Returning to the Main Menu... ")
        else:
            print("error")
        # 
        return
    else:
        edit_each(knight, total_points)

if __name__ == "__main__":
    import knight_master