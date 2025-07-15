#Today we are going to creat a Dictionart that take input from user and return the meaning of the word from the dictionary
dic = {"Ironic":"Meaning the opposite of what you say", "Encompass":"Surround and have or hold within", "Pensive":"thinking deeply and quietly about something serious", "Unfaithful":"having a sexual relationship with somebody who is noy your husband, wife or partner"}
want = input("Walcome to salman dictionary plese type the word you want meaning of.")
print(want,"=", dic[want.capitalize()], end=".")
