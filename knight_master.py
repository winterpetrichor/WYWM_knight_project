# Author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# Main module

# Import submodules
from knight_menu import *
from knight_create import create_knight
from knight_view import view_knights
from attr_edit import edit_attr
from knight_name import name_knight

# Variable for determining whether to exit
exit_var = ["running"]

# Exit function
def knights_exit(exit_var):
    exit_var.pop()
    return(exit_var)

# Basic function returns for menu if's
def yes():
    return("yes")
    
def no():
    return("no")

def name():
    return("name")

def attr():
    return("attr")

def cancel():
    return("cancel")

# Functions for passing to other modules without creating a circular import
func_tup = (
    create_knight, view_knights, name_knight, 
    edit_attr, knights_exit, yes, no, 
    name, attr, cancel)
funcs = {}
for fun in func_tup:
    funcs[fun.__name__] = fun

# Exit
while len(exit_var)>0:
    start_menus(funcs, exit_var)