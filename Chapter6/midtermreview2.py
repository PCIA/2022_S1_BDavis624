L = True
def square(num):
    return num**2
while L == True:
    x = input("Please input a number or press q to quit")
    if x == "q" or x == "Q":
        L = False
    else:
        x = int(x)
        print(square(int(x)))