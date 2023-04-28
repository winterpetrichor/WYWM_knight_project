#import random
#from knight_create import create_knight
#from attr_edit import edit_attr as edit_attr
import traceback

knights = []
knights_data = []
knight_chars = ("Fortitude", "Intellect", "Bravado", "Ambition")
chars = len(knight_chars)
total_points = 5*(chars+1)
kc=[0]*chars
menudict={}
null = ""

def menu_generation(funcs, exit_var):
    # list of menus
    menus = (
        "main",
        "char",
        "yn",
        "exit"
    )
    # tuples of menu options
    menu_tup_main = [
        ["--- Main Menu ---","What would you like to do?"],
        ["Create a new Knight", funcs["create_knight"], (knights, knight_chars, chars, total_points, kc)],
        ["Select and update a Knight", funcs["edit_attr"], (knight_chars, chars, total_points, kc, knights_data, knights)],
        ["Army Statistics", funcs["view_knights"], (knights, knight_chars)],
        ["Exit", funcs["knights_exit"], [exit_var]]
    ]
    menu_tup_char = [
        ["--- Knight Characteristics Menu ---","What would you like to update?"],
        #["Name", funcs["name"], ()],
        #["Attributes", funcs["attr"], ()],
        ["Name", funcs["name"], ()],
        ["Attributes", funcs["attr"], ()],
        ["Cancel", funcs["cancel"], ()]
    ]
    menu_tup_attr = [
        ["--- Knight Attributes Menu ---","What would you like to update?"],
    ]
    menu_tup_yn = [
        [""],
        ["Yes", funcs["yes"], ()],
        ["No", funcs["no"], ()]
    ]
    # fill char menu with chars
    for char in knight_chars:
        menu_tup_attr.append([char])
        
    # number all items for reference
    menulist = [menu_tup_main, menu_tup_char, menu_tup_yn]
    for menu in menulist:
        for j in range(len(menu)):
            menu[j].insert(0,j)
    # fill menu dictionary
    for i in range(len(menulist)):
        menudict[menus[i]] = menulist[i]

def show_menu(menuname):
    # print menu title and all options
    for opt in menudict[menuname]:
        if opt[0] == 0:
            if menuname == "yn":
                pass
            else:
                print(opt[1])
                print(opt[2])
            
        else:
            print(str(opt[0])+": "+str(opt[1]))

    return(menu_selection(menuname))

def menu_selection(menuname):

    # get and validate user selection
    try:
        selection = int(input("Select your option: "))
        return(menudict[menuname][selection][2]
               (*menudict[menuname][selection][3]))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        print("--- Please select a valid option, try again... ---")
        return(menu_selection(menuname))

def start_menus(funcs, exit_var):
    menu_generation(funcs, exit_var)
    show_menu("main")
    print("")
    # print(menudict)
    # print("")
    


if __name__ == "__main__":
    import knight_master