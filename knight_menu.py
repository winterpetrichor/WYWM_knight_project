# Author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# Function to programatically generate menus and capture exceptions

# Import traceback to implement try and except 
# to display error without halting program.
import traceback

# Initialize required variables

# List of class objects that are knights
knights = [] 

# Individual knight
knight = [] 

# Characteristics/ attributes
knight_chars = ("Fortitude", "Intellect", "Bravado", "Ambition") 

# Used regularly, just for shortening code
chars = len(knight_chars)

# Calculate total points available for distribution
total_points = 5*(chars+1)

# Start with 0 for each attribute
knight_chars_point_list = [0]*chars

# Empty dictionary to hold menus
menu_dict = {}

# Function to programatically generate menus.
# I think a structure like this 
# might make editing menus easier at a later date.
def menu_generation(funcs, exit_var):

    # tuple of menu names
    menus = (
        "main",
        "char",
        "yn",
        "exit"
    )

    # Menu options, functions and arguments
    menu_tup_main = [
        ["--- Main Menu ---", "What would you like to do?"],
        ["Create a new Knight", funcs["create_knight"], (
        knights, knight_chars, chars, total_points, 
        knight_chars_point_list)],
        
        # Always update knight_create/create_knight/if show_menu
        # When updating the edit_attr args below
        ["Select and update a Knight", funcs["edit_attr"], (
        total_points, knight, knights)],
        ["Army Statistics", funcs["view_knights"], (
        knights, knight_chars)],
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
        ["--- Knight Attributes Menu ---", "What would you like to update?"],
    ]
    menu_tup_yn = [
        [""],
        ["Yes", funcs["yes"], ()],
        ["No", funcs["no"], ()]
    ]

    # Fill char menu with charateristics/attributes
    for char in knight_chars:
        menu_tup_attr.append([char])
        
    # Number all items for reference
    menu_list = [menu_tup_main, menu_tup_char, menu_tup_yn]
    for menu in menu_list:
        for j in range(len(menu)):
            menu[j].insert(0, j)

    # Fill menu dictionary
    for i in range(len(menu_list)):
        menu_dict[menus[i]] = menu_list[i]

def show_menu(menu_name):

    # Print menu title and all options
    for opt in menu_dict[menu_name]:

        # Skip title for yes/no menu
        if opt[0] == 0:
            if menu_name == "yn":
                pass
            else:
                print(opt[1])
                print(opt[2])
        
        # Print title
        else:
            print(str(opt[0])+": "+str(opt[1]))
    return(menu_selection(menu_name))

def menu_selection(menu_name):

    # Get and validate user selection
    try:

        # Get user input from menu dialog
        selection = int(input("Select your option: "))
        return(menu_dict[menu_name][selection][2]
               (*menu_dict[menu_name][selection][3]))
    
    # Tidy and print exception for error reporting, but continue running.
    # This was implemented to help catch and diagnose errors in submodules.
    # I kept it because I think in general, having the specific error
    # information available for users is important.
    except Exception as e:
        print("")
        print("ERROR MESSAGE:")
        print(e)
        print(traceback.format_exc())
        print("--- Please select a valid option, try again... ---")
        return(menu_selection(menu_name))

# Execute (called from main module)
def start_menus(funcs, exit_var):
    menu_generation(funcs, exit_var)
    show_menu("main")
    print("")
    
# Run main module from any submodule
if __name__ == "__main__":
    import knight_master