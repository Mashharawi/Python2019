
#%%
def is_leap(year):
    leap = False
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


#%%
year = int(input("Enter"))
is_leap(year)


#%%
/* the code with traditional  sol.
# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
*/



