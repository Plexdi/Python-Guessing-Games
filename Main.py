import json as js #to get access to json files
import random #to be able to randomise items
import numpy as np #numpy is a module used for arrays 
import os #os will let you use your operating system 
import platform #indentify what OS the code is running on 

#variables
commandLine = 'cls' if platform.system() == 'Windows' else 'clear'
Player_File_Path = r'C:\Users\Thanh\Documents\School Work\Unit 4 - Programming\Guessing games\Player.txt'


#The guessing games 
def game():
    NUM_GUESS = 6
    USER_GUESS = 0
    os.system(commandLine) # clearing the terminal
    with open('items.json', 'r') as x:
        data = js.load(x) #opening up the json file to be read

    #picking a random description by collecting the index. Then printing out the description so that the user can guess
    index = random.choice(range(24))
    item = data[index] #finding the index of the item that is inside the variable name data
    print(f"description: {item['description']}") 
    name = item['name']

    while (USER_GUESS <= 6): #as long as the "USER_GUESS" is smaller or = 6 it wll continue running
        user_guess = input("Enter a guess: ").lower()
        if user_guess == name:
            os.system(commandLine)
            print("You guessed it!")
            USER_GUESS += 1
            print(f"You took: {USER_GUESS}")
            break
        
        else:
            os.system(commandLine)
            NUM_GUESS -= 1
            USER_GUESS += 1 
            print("Incorrect. Try again")
            print(f"You got: {NUM_GUESS} attempt left")
            continue
    
    retry = input("Would you like to try again? [y][n]: ").lower()
    if retry == 'y':
        main()
    
    else:
        quit("Have a nice day")
        

#checking if the participant name exist or not
def check_file_name(name):
    try:
        with open("Player.txt", 'r') as file:
            content = file.read()
            return name in content
    except FileNotFoundError: 
        return False

#showing the the list of previous players
def PlayerTable():
    os.system(commandLine)
    with open('Player.txt', 'r') as f:
        content = f.read()
        print(content)


#for new players who has not yet been registered
def new_player(name):
    name = input("Enter your name: ")
    if check_file_name(name):
        print('The name is already in the file')
        while True:
            register = input('Would you like to login? [y/n]: ').lower()
            if register == 'y':
                Exisitng_Player(Login=True)
            elif register == 'n':
                confirmation = input("You selected no, are you sure? if yes you will quit the program, if not you will be registering. [y/n]: ").lower()
                while True:
                    if confirmation == 'y':
                        new_player()
                    elif confirmation == 'n':
                        quit("Thank you for trying out my program")
                    else:
                        print("Invalid option. Please type in either [y/n]: ")
                        continue
            else:
                print("Invalid option. Try again")
                continue
    else:
        with open(Player_File_Path, 'a') as f:
            f.write(f"{name}\n") 
            game()
        return name


#this is to login retry
def Exisitng_Player(Login):
    while True:
        Login = input("Enter in your name: ")
        with open(Player_File_Path) as f:
            if check_file_name(Login):
                confirmation = input(f"To confirm your name is: {Login}? [y][n]: ").lower()
                if confirmation == 'y':
                    print('Then we shall get started on the guessing game!')
                    os.system(commandLine)
                    game()
                else:
                    os.system(commandLine)
                    continue
                
            else:
                print(f'"{Login}" does not exist. ')
                while True:
                    retry = int(input("Would you like to try again or register [1][2]: "))
                    if retry == 1:
                        os.system(commandLine)
                        Exisitng_Player(Login=True)
                    elif retry == 2:
                        new_player(name=True)

                    else:
                        print("Invalid option try again")
                        continue


def json_file():
    os.system(commandLine)
    # Load JSON data from file
    with open('items.json', "r") as f:
        data = js.load(f)

    # Now 'data' is a list of dictionaries, each representing an item in your JSON file
    # You can access the data as needed
    for item in data:
        print(f"Name: {item['name']}")
        print(f"Description: {item['description']}\n")

#main program
def main():
    menu = np.array(['League Table','New Player', 'Login', 'items'])
    os.system(commandLine)

    index = 1
    print("Menu:")
    for x in menu:
        print(f'{index}: {x}')
        index += 1 

    while True:
        menu = input("Enter in the menu number: ")
        try:
            menu_num = int(menu)
            if menu_num == 1:
                PlayerTable()

            elif menu_num == 2:
                print("Hello", new_player(name=True))

            elif menu_num == 3:
                Exisitng_Player(Login=True)

            elif menu_num == 4:
                json_file()
        
            else:
                print("Invalid option, try again")
                continue
        
        except ValueError:
            print(f'{menu} is not a number. Try again')
            continue


main()