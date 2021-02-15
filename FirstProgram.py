# To find the Fibonacci Sequence till hundred

def Fibonacci():
    rev = 0
    present = 0
    next = 1
    seq = 0
    while (next < 500):
        if seq == 0:
            print(present)
            print(next)
        seq = next + present
        print(seq)
        present = next
        next = seq