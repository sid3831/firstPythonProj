# To find the Fibonacci Sequence till hundred

def Fibonacci():
    rev = 0
    present = 0
    next = 1
    seq = 0
    while (next < 300):
        if present == 0:
            print(present)
            print(next)
        hold= next
        next= next + present
        print(next)
        present = hold
