#counter
import time
print("Enter timing in MM:SS")

#we will take input here
text = input()

# taking each digit from minutes and seconds
s1 = (text[0])
s2 = (text[1])
s3 = (text[3])
s4 = (text[4])
temp = s1 + s2 # cocananted minutes together 
temp2 = s3 + s4 # cocanated seconds together



s5 = int(temp) #minutes converted to integer
s6 = int(temp2) #seconds converted to integer


rounds = s5 + 1
#created loop by adding 1 to minutes as after 00 also 59 seconds remain

#below is logic to reverse the while loop until the our conunter becomes zero the loop will eventually break when both minutes and second will be zero
#otherwise after seconds will be zero,minutes will be deducted by 1 and seconds will be reset to 59


while rounds != 0:
    

    if s5 == 00 and s6 == 00:
        end = f"{00}:{00}"
        print(end)
        break
    elif s6 == 00:
        s5 = s5 - 1
        rounds -= 1
        s6 = 59
    

    jump = f"{s5}:{s6}"
    print(jump)
    time.sleep(1)

    s6 -= 1

    


    


