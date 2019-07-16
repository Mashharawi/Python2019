
#%%
n = int(input())
credits  = [int(input()) for _ in range(n)]
print(credits)


#%%
for i in range(len(credits)):
    print("hi",credits[i])
    print(first_n_digits(credits[i],1))
    if first_n_digits(credits[i],1) = 
    
    


#%%
import math

def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)
first_n_digits(2145,2)


#%%
import re
def CheckStr(str1):
    
    x = bool(re.match("^[0-9-]*$", str1))
    return x


#%%
CheckStr('8855r588')


#%%
def Noofdigits(str1):
    
    x = len(str1)
    return x


#%%
Noofdigits('85466')


#%%
n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)


#%%
import re

PATTERN=r"^(?!.*([0-9])(?:-?\1){3})[456][0-9]{3}(-?)[0-9]{4}\2[0-9]{4}\2[0-9]{4}$"

def is_valid_card(sequence):
    x=re.search(PATTERN, sequence)
    #print(x)
    if x != None:
        return True
    return False
    #return re.search(PATTERN, sequence)


#%%
is_valid_card('4444-4587-8912-3456')

#%% [markdown]
# ###### import re
# 
# PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
# This might seem arcane, so let us have a look at that pattern. Anything inside parentheses is considered a group. So we have four groups: ([456][0-9]{3}) and three times ([0-9]{4}). The hyphens in between have ? and are therefore optional. If they exist, they must occur once, so -- is not allowed.
# 
# The […] indicates are character class. Only characters inside that class are allowed at that point. The ^ indicates that we're describing the start of our string, not some point in the middle. So we have to start with 456. That requriement is now met. We're followed by 3 ({3}) digits. Our first group therefore consists of four digits, and so do the others. The $ makes sure that there is nothing left: our string has to stop there.
# 
# The re documentation provides more information.
# 
# We now have met most of our conditions:
# 
# we have 16 digits
# we have groups of four
# we only have digits or hyphens
# we start with a 4, 5 or 6

#%%



