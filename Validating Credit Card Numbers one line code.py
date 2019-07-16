import re

PATTERN=r"^(?!.*([0-9])(?:-?\1){3})[456][0-9]{3}(-?)[0-9]{4}\2[0-9]{4}\2[0-9]{4}$"

def is_valid_card(sequence):
    x=re.search(PATTERN, sequence)
    #print(x)
    if x != None:
        return True
    return False
#result = is_valid_card('5122-2368-7954-3214')
#print(result)


while True:
    n = input("Enter number or enter # to END!     :")
    if n != '#':
        result = is_valid_card(n)
        print(result)
    else:
        print("Bye")
        break