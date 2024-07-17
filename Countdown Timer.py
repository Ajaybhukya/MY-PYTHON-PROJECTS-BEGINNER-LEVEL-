"""
try to run this code in the jupyter notebook which gives you the best output
"""
import time
def count(seconds):
    while seconds:
        mins,secs=divmod(seconds,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end='\r')
        time.sleep(1)
        seconds-=1
    print("Time out")
try:
    secons=int(input("Enter the seconds:"))
    count(secons)
except ValueError as e:
    print("Invalid input")
    print("Program exited")
