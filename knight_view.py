# author winterpetrichor [https://github.com/winterpetrichor]
# WYWM Software Development python project

# import pandas to compile knights and attributes into a table 
import pandas as pd

# function to view all knights and attributes
# function also totals and averages attributes of entire army
def view_knights(knights, knight_chars):
    if(len(knights)==0):
        print("You have no knights! \
Please create some knights and try again...")
        return
    
    # initialize variables
    arraylist = []
    nlst = ["Name"]

    # create main table with values
    for c in knight_chars:
        nlst.append(c)
    for k in knights:
        lst = []
        lst.append(k.k_name)
        for a in k.k_attr:
            lst.append(k.k_attr[a])
        arraylist.append(lst)
    df = pd.DataFrame(arraylist)
    df.columns = nlst

    # create sum and average rows
    tot = (df.sum(numeric_only=True))
    avg = (df.mean(numeric_only=True))
    olst = ["Total"]
    alst = ["Average"]
    for i in tot:
        olst.append(i)
    for a in avg:
        alst.append(round(a,1))
    print("")

    # list of columns
    kc2 = ["Name"] + list(knight_chars)

    # total and average rows
    df2 = pd.DataFrame([olst], columns=kc2)
    df3 = pd.DataFrame([alst], columns=kc2)

    # merge main table, total and average rows, and display table
    dff = pd.concat([df,df2,df3], axis=0, ignore_index=True)
    print(dff)
    
# run main module from any submodule
if __name__ == "__main__":
    import knight_master