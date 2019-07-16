
#%%
n = int(input("Enter No.:   "))
if n in range(100):
    if (n % 2) == 0:
        if  n >=2 and n <=5:
            print ("Not Weird")
        elif n <=20 and n >=6:
            print("Weird")
        elif n > 20 :
            print ("Not Weird")
    else:
        print("Weired")
else:
    print("Enter no between 1 - 100")


#%%



#%%



