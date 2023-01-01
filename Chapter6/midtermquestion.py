x = True
while x == True:
    y = input("Enter a number equal to or greater than ten and equal to or lesser than twenty.")
    y = int(y)
    if y >= 10 or y <= 20:
        print(y**2)
        x = False
    else 