# author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# function to rename knight
def name_knight(knight):
    knight.k_name = str(input("What is "+ knight.k_name + "'s new name: "))
    return(knight)

# run main module from any submodule
if __name__ == "__main__":
    import knight_master