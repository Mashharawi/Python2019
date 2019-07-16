
#%%
import random 
ls = [] 
for j in range(10000): 
        ls.append(random.randint(1, 200)) 
print(ls[:10])  
while True:
    num=input("Enter integer number please:   ")
    num = int(num)
    if (num % 2) != 0:
        print("Please enter even no.")
        continue
    else:
        found = False
        for i in ls:
            if i == num:
                print("Yes its exist")
                found = True
                break 
        if not found:
            print("Your no. not  exist")
        else:
            break
            
    #num=int(input ("Enter num only"))


#%%



