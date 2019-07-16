#%% [markdown]
# # loops in Python 

#%%
list(range(2,10))


#%%
list(range(2,10,3))

#%% [markdown]
# ## range(start,stop,step)

#%%
[i+3 for i in range(10)]

#%% [markdown]
# # While

#%%
while True:
    name = input("Enter Name")
    if name.startswith('#'):
        continue  #go to line one
        print("Hello"+name)
    ans = input("Do ir again")
    if ans == 'n':
        print("Goodbye")
        break  # go to line 
    print("done")
    


#%%
import random 
ls = [] 
for j in range(1000): 
        ls.append(random.randint(1, 10000)) 
print(ls)  

num=int(input("Enter integer number please"))
if (num % 2) == 0:
    if num in ls:
        print("Yes its exist")
    print("Unfotunatly your num not Exist")
num=int(input ("Enter even only"))


#%%
import random 
ls = [] 
for j in range(1000): 
        ls.append(random.randint(1, 10000)) 
# print(ls)  

num=int(input("Enter integer number please"))
if (num % 2) == 0:
            if num in ls:
                print("Yes its exist")
            print("Unfotunatly your num not Exist")
num=int(input ("Enter even only"))


#%%



