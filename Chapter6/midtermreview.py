X = True
while X == True:
    y = input("Give a number between 10 and 20")
    y = int(y)
    if y >= 10 and y <= 20:
        print(y**2)
        x = False
    if y < 10:
        print("Too Low")
    elif y > 20:
        print("Too high")