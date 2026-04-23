import time
def countdown(n):
    if n<= 0:
        print("done")
    else:
        print(n)
        time.sleep(0.75)
        countdown(n-1)

countdown(5)