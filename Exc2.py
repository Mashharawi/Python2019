#%% [markdown]
# #print in list ls only the element which greater than left nighbour and less than left nighbour

#%%
import random 
ls = [] 
for j in range(100): 
        ls.append(random.randint(1, 200)) 
print(ls[:8]) 


#%%
for i in range(1,len(ls)-1):
    if ls[i-1] < ls[i] < ls[i+1]:
        print("i-1",ls[i-1],"i",ls[i],"i+1",ls[i+1],)


#%%



#%%



#%%



#%%



