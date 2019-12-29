#this is a password generator that includes at least 1 cap, 1 lower, 1 digit and 1 symbol in random order

import random
import string

caps_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lows_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
digs_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ",", "<", ">", ".", "/", "?", ";", ":", "[", "{", "]", "}", "|"]

replacedChars_list = []

allCharacters_list = caps_list + lows_list + digs_list + symbols_list

def list_to_string(l):
    i = 0
    string = ""
    while i != len(l):
        string = string + l[i]
        i = i + 1
    return string

flag = 0
while flag == 0:
    user_input = input("How long do you want your password to be?: ")
    try:
        int(user_input)
    except ValueError:
        print("Please enter a integer!")
        flag = 0
        continue
    if int(user_input) <= 3:
        print("Your password needs to be at least 4 characters!")
        flag = 0
    elif int(user_input) > 3:
        i = 0
        password = []
        while i != int(user_input):
            if len(password) < 4 and i < 4:
                password.append(random.choice(caps_list))
                password.append(random.choice(lows_list))
                password.append(random.choice(digs_list))
                password.append(random.choice(symbols_list))
                i = i + 4
            elif i >= 4:
                password.append(random.choice(allCharacters_list))
                i = i + 1
        random.shuffle(password)
        print(list_to_string(password))
        anotherOne = input("Would you like to generate another password? (Y/N): ")
        if anotherOne == "Y" or anotherOne == "y":
            password = []
            flag = 0
        elif anotherOne == "N" or anotherOne == "n":
            flag = 1
            break
        else:
            flag = 1
            break
print("Exiting program...")            
    
