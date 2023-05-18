# Author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# Import pandas to compile knights and attributes into a table 
import pandas as pd

# Function to view all knights and attributes.
# Function also totals and averages attributes of entire army.
def view_knights(knights, knight_chars):
    if(len(knights) == 0):
        print("You have no knights! \
Please create some knights and try again...")
        return
    
    # Initialize variables
    array_list = []
    name_list = ["Name"]

    # Create main table with values
    for c in knight_chars:
        name_list.append(c)
    for k in knights:
        lst = []
        lst.append(k.knight_name)
        for a in k.knight_attr:
            lst.append(k.knight_attr[a])
        array_list.append(lst)
    df = pd.DataFrame(array_list)
    df.columns = name_list

    # Create sum and average rows
    tot = (df.sum(numeric_only=True))
    avg = (df.mean(numeric_only=True))
    total_list = ["Total"]
    average_list = ["Average"]
    for i in tot:
        total_list.append(i)
    for a in avg:
        average_list.append(round(a, 1))
    print("")

    # List of columns
    df_headers = ["Name"] + list(knight_chars)

    # Total and average rows
    df2 = pd.DataFrame([total_list], columns=df_headers)
    df3 = pd.DataFrame([average_list], columns=df_headers)

    # Merge main table, total and average rows, and display table
    dff = pd.concat([df, df2, df3], axis=0, ignore_index=True)
    print(dff)
    
# Run main module from any submodule
if __name__ == "__main__":
    import knight_master