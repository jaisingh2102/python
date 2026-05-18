# This code demonstrates a recursive countdown function that counts down from a given number to zero, printing each number with a delay of 0.75 seconds.
import time
def countdown(n):
    if n<= 0:
        print("done")
    else:
        print(n)
        time.sleep(0.75)
        countdown(n-1)

countdown(5)