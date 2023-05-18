# Author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# Function to rename knight
def name_knight(knight):
    knight.knight_name = str(input("What is "+ knight.knight_name + "'s new name: "))
    return(knight)

# Run main module from any submodule
if __name__ == "__main__":
    import knight_master