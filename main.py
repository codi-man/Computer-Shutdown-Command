#This is a python command that allows you to shut down a computer

import os

shut_down = int(input("Do you want to shut down the system? Press 1 for yes or any other integer key for no: "))

#Create an if statement
if shut_down == 1:
    print("Enter Number of Seconds to Shutdown System: ")
    sec = int(input())
    strOne = "shutdown /s /t "
    strTwo = str(sec)
    str = strOne+strTwo
    os.system(str)
#else statement, when the "if" condition is false 
else:
    print("Ok, The system will not be shutdown")
