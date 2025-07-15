# this progarm gona tell if you can drive or not
age = int(input("Plese type you are so we can tel you can drive or not.\n"))

if age>100 or age<7:
    print("That an invalid age.")
elif age>18:
    print("you can drive.")
elif age==18:
    print("We cannot tell if you can drive or not plese come for phycal cheak-up for canformation.")
else:
    print("You cannot drive.")
