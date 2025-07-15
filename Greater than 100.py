# progam will contineu if you put number below 100 if you put more that 100 it will break
while (True):
    num = int(input("Plese enter number.\n"))
    if num > 100:
        print("Congratulation you have put a number greater that 100.\n")
        break
    else:
        print("Try again!\n")
        continue
