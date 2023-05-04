# author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# function to programatically generate menus and capture exceptions

# import traceback to implement try and except 
# to display error without halting program
import traceback

# initialize required variables

# list of class objects that are knights
knights = [] 

# individual knight
knight = [] 

# characteristics/ attributes
knight_chars = ("Fortitude", "Intellect", "Bravado", "Ambition") 

# used regularly, just for shortening code
chars = len(knight_chars)

# calculate total points available for distribution
total_points = 5*(chars+1)

# start with 0 for each attribute
kc=[0]*chars

# empty dictionary to hold menus
menudict={}

# function to programatically generate menus
# I think a structure like this 
# might make editing menus easier at a later date
def menu_generation(funcs, exit_var):

    # tuple of menu names
    menus = (
        "main",
        "char",
        "yn",
        "exit"
    )

    # menu options, functions and arguments
    menu_tup_main = [
        ["--- Main Menu ---","What would you like to do?"],
        ["Create a new Knight", funcs["create_knight"], (knights, 
                                                         knight_chars, 
                                                         chars, 
                                                         total_points, 
                                                         kc)],
        
        # always update knight_create/create_knight/if show_menu
        # when updating the edit_attr args below
        ["Select and update a Knight", funcs["edit_attr"], (total_points,
                                                            knight, 
                                                            knights)],
        ["Army Statistics", funcs["view_knights"], (knights, 
                                                    knight_chars)],
        ["Exit", funcs["knights_exit"], [exit_var]]
    ]
    menu_tup_char = [
        ["--- Knight Characteristics Menu ---",
         "What would you like to update?"],
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

    # fill char menu with charateristics/attributes
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

        # skip title for yes/no menu
        if opt[0] == 0:
            if menuname == "yn":
                pass
            else:
                print(opt[1])
                print(opt[2])
        
        # print title
        else:
            print(str(opt[0])+": "+str(opt[1]))
    return(menu_selection(menuname))

def menu_selection(menuname):

    # get and validate user selection
    try:

        # get user input from menu dialog
        selection = int(input("Select your option: "))
        return(menudict[menuname][selection][2]
               (*menudict[menuname][selection][3]))
    
    # tidy and print exception for error reporting, but continue running
    # this was implemented to help catch and diagnose errors in submodules
    # I kept it because I think in general, having the specific error
    # information available for users is important
    except Exception as e:
        print("")
        print("ERROR MESSAGE:")
        print(e)
        print(traceback.format_exc())
        print("--- Please select a valid option, try again... ---")
        return(menu_selection(menuname))

# execute (called from main module)
def start_menus(funcs, exit_var):
    menu_generation(funcs, exit_var)
    show_menu("main")
    print("")
    
# run main module from any submodule
if __name__ == "__main__":
    import knight_master