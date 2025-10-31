#Hangman 

#Importing necessary modules: 
import random
import time 

#List of words as per difficulty levels: 
e = [
    'apple', 'mango', 'kiwi', 'litchi', 'papaya', 'carrot', 'potato', 'tomato', 'onion', 
    'beetroot', 'radish', 'cabbage', 'nut', 'pecan', 'audi', 'bmw', 'dodge', 'ford', 
    'honda', 'jeep', 'kia', 'mazda', 'nissan', 'subaru', 'volvo', 'tesla', 'tata', 
    'suzuki', 'ant', 'bear', 'cat', 'dog', 'newt', 'owl', 'quail', 'snake', 'tiger', 
    'vulture', 'whale', 'xerus', 'yak', 'zebra', 'frog', 'cake', 'bulb', 'song', 'trip', 
    'skiing', 'jazz', 'buzz', 'hajj', 'faff', 'fizz', 'fuzz'
]

m = [
    'avocado', 'banana', 'orange', 'grapes', 'watermelon', 'strawberry', 'pineapple', 
    'muskmelon', 'cucumber', 'spinach', 'broccoli', 'capsicum', 'almond', 'cashew', 
    'pistachio', 'walnut', 'peanut', 'hazelnut', 'macadamia', 'chestnut', 'chevrolet', 
    'hyundai', 'jaguar', 'lexus', 'mercedes', 'porsche', 'toyota', 'elephant', 'anteater', 
    'giraffe', 'leopard', 'kangaroo', 'monkey', 'penguin', 'rabbit', 'unicorn', 
    'platypus', 'treasure'
]

h = [
    'spanish tomato', 'cauliflower', 'pumpkin seed', 'sunflower seed', 'land rover', 
    'volkswagen','pneumonoultramicroscopicsilicovolcanoconiosis', 'antidisestablishmentarianism', 
    'floccinaucinihilipilification', 'supercalifragilisticexpialidocious'
]

levels = [e, m , h] 

#Scaffold: 
def print_scaffold(wrongguess):
    if wrongguess==6:
        print("__________")
        print("|        |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_________")     
    elif wrongguess==5:
        print("__________")
        print("|        |")
        print("|        O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif wrongguess==4:
        print("__________")
        print("|        |")
        print("|         O")
        print("|         |")
        print("|         | ")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif wrongguess==3:
        print("__________")
        print("|        |")
        print("|         O")
        print("|        /|")
        print("|       / | ")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif wrongguess==2:
        print("__________")
        print("|        |")
        print("|         O")
        print("|        /|\\")
        print("|       / | \\")
        print("|")
        print("|")
        print("|")
        print("|_________") 
    elif wrongguess==1:
        print("__________")
        print("|        |")
        print("|        O")
        print("|       /|\\")
        print("|      / | \\")
        print("|       /   ")
        print("|      /     ")      
        print("|")
        print("|_________")
    elif wrongguess==0: 
        print("\nHANGMAN!\n")
        print("__________")
        print("|        |")
        print("|        O")
        print("|       /|\\")
        print("|      / | \\")
        print("|       / \\ ")
        print("|      /   \\ ")
        print("|")
        print("|_________") 
        print("\nGAME OVER!\n")

#List of art, interaction with the user: 
art = [ "Angry Chinese Man flipping the table:︵ヽ(`Д´)ﾉ︵ ┻━┻","A cat: ฅ^•ﻌ•^ฅ","A dog: ᶘ ᵒᴥᵒᶅ","A bear: ʕ•ᴥ•ʔ","3 monkeys: 🙈🙉🙊",
    "A penguin that looks like a bear: ʕ•ᴥ•ʔ","A fish: ><(((('>","An evil looking shark: (•̀ᴗ•́)و ̑̑",
    "A snail: @(^_^)@","A butterfly: Ƹ̵̡Ӝ̵̨̄Ʒ","A flower: ✿","A tree: 🌳","A cloud: ☁️","A sun: ☀️","A moon: 🌙","A star: ⭐️","A rainbow: 🌈",
    "A snowflake: ❄️","A snowman that looks like a ladybug: ☃️","A volcano: 🌋", "A mountain: ⛰","A river: 🏞","A lake: 🏞","A beach: 🏖",
    "A desert: 🏜","A tent: ⛺️","A house: 🏠","A castle: 🏰","A palace: 🏛","A church: ⛪️","A mosque: 🕌","A temple: ⛩","A bridge: 🌉",
    "A tunnel: 🚇","A train: 🚂","A car: 🚗","A bus: 🚌","A taxi: 🚕","A truck: 🚚","A bicycle: 🚲","Some fish: 𓆝 𓆟 𓆞 𓆝 𓆟"
] 

interactions = [ "The twelve most commonly occurring letters in the English language are e-t-a-o-i-n-s-h-r-d-l-u (from most to least)", "A common strategy is to guess vowels first, as English only has five vowels (a, e, i, o, and u, while y may sometimes, but rarely, be used as a vowel) and almost every word has at least one.", "The letter 'e' is the most commonly used letter in the English language.","The letter 'q' is the least commonly used letter in the English language.","The word 'uncopyrightable' is the longest English word that can be written without repeating a letter.", "According to a 2010 study conducted by Jon McLoone for Wolfram Research, the most difficult words to guess include jazz, buzz, hajj, faff, fizz, fuzz and variations of these.", "The American game show Wheel of Fortune was inspired by hangman. Merv Griffin conceived of the show after recalling long car trips as a child, on which he and his sister played the game.", "The longest game of hangman lasted 16 hours and 37 minutes, and was achieved by the students of the University of Lethbridge in Alberta, Canada, on 21 November 2019.","The longest word in the English language is pneumonoultramicroscopicsilicovolcanoconiosis, a type of lung disease caused by inhaling very fine silicate or quartz dust.","In July 2017, the BBC introduced a game show of its own called Letterbox, which is also based on hangman.", "The answer is 42. Google says so!", 
]

#Functions to carry out interactions with the user: 
def interaction():
    print(random.choice(interactions))

#Function to print the introductory message: 
def print_intro():

    print("Let the games begin!")

    print("Choose your difficulty level: ") 

#Function to select the difficulty level: 
def diff_lvl():
    print("Select the difficulty level:\n ")
    time.sleep(1)
    level=input("1 - Easy , 2 - Not so hard , 3 - Pretty hard, but possible, 4 - I can't make up my mind! \n")
    try:
        if level=="1":
            print("You have chosen the Easy level. ok, look's like someone's not up for a tough challenge.\n ")
            someword=random.choice(e)
        elif level=="2":
            print("You have chosen the Not so hard level. Sitting on the fence again, aren't we?.\n")
            someword=random.choice(m)
        elif level=="3":
            print("You have chosen the Pretty hard, but possible level. Someone's feeling a little adventurous today.\n")
            someword=random.choice(h)
        elif level=="4":
            print("You have chosen the I can't make up my mind level. Yeah, that can happens sometimes, especially with ice-cream flavors.\n")
            somelevel=random.choice(levels) 
            someword=random.choice(somelevel)
        elif level=="42":
            print(random.choice(art))
            diff_lvl()
        return someword
    except:
        print("Trying to be funny are we?\n")
        print("Please enter a valid input\n")
        diff_lvl()
    return someword

#Main body: 
def hangman():
    print("\nWelcome to Hangman!\n")
    time.sleep(1)
    print("Today, we shall play Hangman!\nA game that is more pleasant than it sounds.\n") 
    time.sleep(2)
    print("Though the origins of this game are not exactly known,\nthe earliest mentions of this game date back to the late 19th century,\nin a book for children's games by Alice Bertha Gomme.\n")
    time.sleep(2)
    print("\nThat version, pretty much similar to the one we are about to play,\nlacked the image of a hangman, and instead, just kept the score.\n")
    time.sleep(2)
    print("\nNow I don't know who came up with the idea of the hangman itself, or why, \nbut it all seems pretty disturbing to me. \nThis was supposed to be a kid's game, right? \n\nAnyway, who am I to judge? \nOn this note, Let's play!\n") 
    time.sleep(2)
    choice=input("Are you ready to play? (yes/no):\n").strip().lower()
    time.sleep(2)
    if choice=="yes":
        print("\nLet's get started!\n")
        word=diff_lvl() 
        time.sleep(1)
        wordlen=len(word)
        toguess=wordlen-1
        chances=wordlen+3
        gameover=False
        guessed=[wordlen-1]
        wrongguess=6
        print("The word has",wordlen,"letters. You have",chances,"chances to guess the word.\nYou can only make", wrongguess, "wrong guesses.")
        time.sleep(1)
        print("Good luck!")
        print_scaffold(wrongguess)
        time.sleep(1)
        guessed = ["_"]*wordlen
        print(guessed)
        while not gameover==True:
            if toguess==0:
                gameover=True
                print("Congratulations! You have guessed the word correctly!")
                time.sleep(1)
                print("Would you like to play again?")
                playagain=input("yes/no: ").strip().lower()
                if playagain=="yes":
                    hangman()
                else:
                    print("Thank you for playing!")
                    quit()
            else:
                letter=input("Enter a letter: ").strip().lower()
                if len(letter)>1 or letter=="":
                    print("Please enter a valid input")
                elif letter in guessed: 
                    print("You have already guessed this letter. Here is what you have guessed so far:\n", guessed)
                else:
                    if letter in word: 
                        toguess-=1
                        chances-=1
                        print("Your guess was correct!")
                        for i in range(wordlen):
                            if letter == word[i]:
                                guessed[i] = letter
                            else:
                                continue
                        print("Chances left: ",chances, "Wrong guesses left: ",wrongguess)
                        print(guessed)
                        time.sleep(1)
                        interaction()
                        time.sleep(1)
                        print_scaffold(wrongguess)
                    else:
                        wrongguess-=1
                        chances-=1
                        print("Your guess was incorrect this time!")
                        if wrongguess==0 or chances==0:                        
                            print_scaffold(wrongguess)
                            print("The correct answer was:" ,word)
                            print("Would you like to play again?")
                            playagain=input("yes/no: ").strip().lower()
                            if playagain=="yes":
                                hangman()
                            else:
                                print("Thank you for playing!")
                                quit()
                            gameover=True
                        else: 
                            print("Chances left: ",chances, "Wrong guesses left: ",wrongguess)
                            print(guessed)
                            interaction()
                            time.sleep(1)
                            print_scaffold(wrongguess)
    else:
        print("Bye! Thank you for visiting!")
        quit()

hangman() 




