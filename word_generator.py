#random nickname generator using morse-code


import random
#name list
name = ['alpha','beta','charlie','delta','echo','foxtrot','golf','hotel','india','juliet','kilo','lina','mike','november','papa','quebec','romeo','sierra','tango','uniform','victor','whiskey','x-ray','yankee','zulu']


def generator():
    #two random numbers 
    num1 = random.randint(0,24)
    num2 = random.randint(0,24)

    #two random names
    done = name[num1]
    done2 = name[num2]


    #we will get our name if both names aren't equal
    if num1 != num2:
        print(f'The generated name is {done} {done2}')
    #else there would be an error
    else:
        print('error')    

    

generator()