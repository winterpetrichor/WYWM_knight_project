#from numpy import array
import pandas as pd

def view_knights(knights, knight_chars):
    arraylist = []
    nlst = ["Name"]
    for c in knight_chars:
        nlst.append(c)
    #arraylist.append(nlst)
    #print(nlst)
    for k in knights:
        lst = []
        lst.append(k.k_name)
        for a in k.k_attr:
            lst.append(k.k_attr[a])
        arraylist.append(lst)
        #print(lst)
        # consider using and displaying an array

    #view = array(arraylist)
    #print(view)

    df = pd.DataFrame(arraylist)
    df.columns = nlst
    tot = (df.sum(numeric_only=True))
    avg = (df.mean(numeric_only=True))
    olst = ["Total"]
    alst = ["Average"]
    for i in tot:
        olst.append(i)
    for a in avg:
        alst.append(round(a,1))
    print("")
    kc2 = ["Name"] + list(knight_chars)
    df2 = pd.DataFrame([olst], columns=kc2)
    df3 = pd.DataFrame([alst], columns=kc2)
    dff = pd.concat([df,df2,df3], axis=0, ignore_index=True)
    print(dff)
    