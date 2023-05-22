# adding player's health as a global variable
player_health = 100
# ====================================================================================
# importing things:
# ====================================================================================
import random
import time
import sys
from time import sleep
# ====================================================================================
# ====================================================================================
# ====================================================================================



# ====================================================================================
# ====================================================================================
# ====================================================================================
# 
# Adding functions to the game:
# ====================================================================================
# typewriter function:
def typewrite_fast(text):
        lines = [text]
        greentext = '\033[32m'
        ENDC = '\033[m'
        
        # for each line of text (or each message) 
        for line in lines:   
        # for each character in each line 
            for c in line:                 
            # print a single character, and keep the cursor there.
                print(greentext + c, end='')    
                # flush the buffer
                sys.stdout.flush()
                # wait a little to make the effect look good.
                sleep(0.001)          
            print(ENDC + '')
def typewrite(text):
    lines = [text]
    from time import sleep
    import sys
    # for each line of text (or each message) 
    for line in lines:   
     # for each character in each line 
        for c in line:                 
         # print a single character, and keep the cursor there.
            print(c, end='')    
            # flush the buffer
            sys.stdout.flush()
            # wait a little to make the effect look good.
            sleep(0.01)          

        print('')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# health deduction function:
def baby_dont_hurt_me(current_health):
    current_health = current_health - 50
    global player_health
    player_health = current_health
    # return current_health
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# rock paper scissors lizard spock game function:
def rock_paper_scissors_spock():
    # defining function to find out who won and return a specific value which indicates win, loss or draw for the actual game
    def who_won(user_choice, computer_choice):
        # Making sure that draw is possible and that the game restarts
        if user_choice == computer_choice:
            return "It's a draw!", 2
        # comparing rock against the computer's scissors or lizard. Anything else beats it
        if user_choice == 'rock':
            if computer_choice == 'scissors' or computer_choice == 'lizard':
                return "Fine, you won this time. I'll still get you in the end.", 1
            else:
                return "I win!", 0
        # applying same logic as above, only need to care about parts that I win
        if user_choice == 'paper':
            if computer_choice == 'rock' or computer_choice == 'spock':
                return "You win, but you can't keept this up.", 1
            else:
                return "I win!", 0
        # applying same logic as above, only need to care about parts that I win
        if user_choice == 'scissors':
            if computer_choice == 'paper' or computer_choice == 'lizard':
                return "Fine, you won this time. I'll still get you in the end..", 1
            else:
                return "I win!", 0
        # applying same logic as above, only need to care about parts that I win
        if user_choice == 'spock':
            if computer_choice == 'rock' or computer_choice == 'scissors':
                return "Fine, you won this time. I'll still get you in the end.", 1
            else:
                return "I win!", 0
        # applying same logic as above, only need to care about parts that I win
        if user_choice == 'lizard':
            if computer_choice == 'paper' or computer_choice == 'spock':
                return "Fine, you won this time. I'll still get you in the end.", 1
            else:
                return "I win!", 0

    # defining the game itsef - need to get input from the user, what needs to be printed, list of options...
    def play_rock_paper():
        typewrite_fast(r""" 






▄▄▄         ▄▄· ▄ •▄          ▄▄▄· ▄▄▄·  ▄▄▄·▄▄▄ .▄▄▄          
▀▄ █·▪     ▐█ ▌▪█▌▄▌▪        ▐█ ▄█▐█ ▀█ ▐█ ▄█▀▄.▀·▀▄ █·        
▐▀▀▄  ▄█▀▄ ██ ▄▄▐▀▀▄·         ██▀·▄█▀▀█  ██▀·▐▀▀▪▄▐▀▀▄         
▐█•█▌▐█▌.▐▌▐███▌▐█.█▌        ▐█▪·•▐█ ▪▐▌▐█▪·•▐█▄▄▌▐█•█▌        
.▀  ▀ ▀█▄▀▪·▀▀▀ ·▀  ▀        .▀    ▀  ▀ .▀    ▀▀▀ .▀  ▀        
        .▄▄ ·  ▄▄· ▪  .▄▄ · .▄▄ ·       ▄▄▄  .▄▄ ·             
        ▐█ ▀. ▐█ ▌▪██ ▐█ ▀. ▐█ ▀. ▪     ▀▄ █·▐█ ▀.             
        ▄▀▀▀█▄██ ▄▄▐█·▄▀▀▀█▄▄▀▀▀█▄ ▄█▀▄ ▐▀▀▄ ▄▀▀▀█▄            
        ▐█▄▪▐█▐███▌▐█▌▐█▄▪▐█▐█▄▪▐█▐█▌.▐▌▐█•█▌▐█▄▪▐█            
         ▀▀▀▀ ·▀▀▀ ▀▀▀ ▀▀▀▀  ▀▀▀▀  ▀█▄▀▪.▀  ▀ ▀▀▀▀             

                                      


.........................................................


""")
        # list of options:
        choices = ['rock', 'paper', 'scissors', 'spock', 'lizard']
        # setting variable to true to run the program again
        restart_game = True
        # condition to make sure the game gets restarted if draw happens
        while restart_game:
            # getting user input
            typewrite("Thought you could escape? Let's see if luck is on your side!")
            user_choice = input("Choose your destiny! rock, paper, scissors, spock, or lizard: ").lower()
            # clearing the screen
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            # condition to make sure user input is usable. 
            if user_choice not in choices:
                typewrite("Why don't you try that again, but this time choose one of the actual options.")
                for specific_time in range (0,5):  
                    loading_waiting = "Loading" + "." * specific_time
                    print (loading_waiting, end="\r")
                    time.sleep(1)
                continue
            # Devil's choice using random.choice
            computer_choice = random.choice(choices)
            print("I've chosen mighty", computer_choice,"!")
            # defining two variables to same value. One is used for print and one for check for the outcome
            result, status = who_won(user_choice, computer_choice)
            print(result)
            # checking the outcome and assigning the global variable the value we need (will be used to deduct health calling another function)
            if status == 1:
                # when the player wins, assigning global variable value 1 and letting the player know
                typewrite("You got lucky, but you're merely delaying the inevitable!")
                restart_game = False
            elif status == 0:
                # when the devil wins, assigning global var. 0 and letting player know they lost
                baby_dont_hurt_me(player_health)
                typewrite("The demon cackles and rakes a jagged claw across your chest.\n'Don't think you'll get off that easy.'")
                restart_game = False
            else:
                # restarting the game if any other outcome occurs
                typewrite("Hmmm. Not fair, we will play again.")
    # need to call only play_rock_paper as the function is only usable for this function itself, it doesn't need calling separately
    play_rock_paper()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  toss a coin game function:
def toss_a_coin():
    def who_won(user_choice, landed_coin):
        if user_choice == landed_coin:
            return "Good guess.", 1
        else:
            return "Yes!", 0
    
    # defining the game itsef - need to get input from the user, what needs to be printed, list of options...
    def play_toss_a_coin():
        typewrite_fast(r""" 

╦ ╦╔═╗╔═╗╔╦╗╔═╗  
╠═╣║╣ ╠═╣ ║║╚═╗  
╩ ╩╚═╝╩ ╩═╩╝╚═╝  
  ╔═╗╦═╗         
  ║ ║╠╦╝         
  ╚═╝╩╚═         
╔╦╗╔═╗╦╦  ╔═╗    
 ║ ╠═╣║║  ╚═╗    
 ╩ ╩ ╩╩╩═╝╚═╝    
                 
                 
                 
           

.........................................................


""")
        # list of options:
        choices = ['heads', 'tails']
        # setting variable to true to run the program again
        restart_game = True
        # checking the theory, need to comment that out
        # print(toss_a_coin_results, "line 32 toss_a_coin_results after calling it global")
        global toss_a_coin_results
        toss_a_coin_results = 0
        # condition to make sure the game gets restarted if draw happens
        while restart_game:
            # getting user input
            typewrite("I am going to flip a coin.")
            user_choice = input("Let's seal your destiny! Heads or tails? ").lower()
            # clearing the screen
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            # condition to make sure user input is usable. 
            if user_choice not in choices:
                typewrite("You have to choose, no point trying to stall.")
                for specific_time in range (0,5):  
                    loading_waiting = "Checking the contract and rules again" + "." * specific_time
                    print(loading_waiting, end="\r")
                    time.sleep(1)
                continue
            # Devil's choice using random.choice
            landed_coin = random.choice(choices)
        
            print("And it's", landed_coin,"!")
            # defining two variables to same value. One is used for print and one for check for the outcome
            result, status = who_won(user_choice, landed_coin)
            print(result)
            # checking the outcome and assigning the global variable the value we need (will be used to deduct health calling another function)
            if status == 1:
                # when the player wins, assigning global variable value 1 and letting the player know
                input("Go on, run until I get you again!")
                toss_a_coin_results = 1
                restart_game = False
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
            elif status == 0:
                # when the devil wins, assigning global var. 0 and letting player know they lost
                toss_a_coin_results = 0
                input("Too bad! I always win, I don't even understand why you are trying...")
                restart_game = False
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
            else:
                # restarting the game if any other outcome occurs
                input("That's not in my contract or rules. We are playing again.")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
    # need to call only play_toss_a_coin, as it uses the who_won function
    typewrite("Now that I have caught up with you, I am going to have some fun.")
    typewrite("The devil pull out an ancient looking ornate gold coin")
    play_toss_a_coin()
    # counting the results. The first time, the toss_a_coin_results are the overall results.
    result_of_all_rounds = toss_a_coin_results
    # Preparing for the second round
    typewrite("Ok, best of three.  Let's see how luck you really are.")
    input("Waiting until you get yourself together...")
    # clearing the screen
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    # running the game 2nd time:
    play_toss_a_coin()
    # overall results + last game results from toss_a_coin_results will give me the current score
    result_of_all_rounds += toss_a_coin_results
    input("It's getting nice and hot here. Let's do it again.")
    # clearing the screen
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    play_toss_a_coin()
    result_of_all_rounds += toss_a_coin_results
    # just testing the theory here, will comment out
    # print(result_of_all_rounds)
    # print(toss_a_coin_results)
    # need an if loop - unless the result_of_all_rounds value is 2 or more, the player lost
    if result_of_all_rounds >= 2:
        typewrite("")
    else:
        typewrite("The demon grabs you by the arm and pushes the coin into your chest\nyour skin sizzles at the contact and begins to blister and pop as white hot metal burns deep into you.\nYou wrench yourself free and start to stumble away.")
        baby_dont_hurt_me(player_health)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# anagram game function:
def anagram_game():
# defining function for the random choice of one of the words in the list. List words can be updated as needed
    def choose_word():
        # List of the words - if you wish to update them, do that here
        devils_words = ['darkness', 'fire', 'shadows', 'hot', 'deep', 'evil', 'soul','desire']
        # the function will return randomly selected - random.chocie string from the list above
        return random.choice(devils_words)

    # defining devil language haha
    # function is meant to take an input (word) from the list that will then get corrupted
    def devil_language(word):
        # taking the input word and assigning it to variable corrupted word. So I can corrupt it without loosing
        # value coming from function choose_word:
        corrupted_word = list(word)
        # randomly shuffling the index of the variable corrupted_word
        random.shuffle(corrupted_word)
        # I had to convert the string because it kept giving me errors when it was used in the actual game code
        # I am not sure why though
        return ''.join(corrupted_word)

    # defining function to play the game so it can also repeat and give an output using the functions above:
    def game_code():
        # variable choosen word will gain value of function choose_word that will randomly select one and return it
        chosen_word = choose_word()
        # assigning value of the devil_language function, which will be corrupted word to variable corrupted
        corrupted = devil_language(chosen_word)
        # Setting a counter by assigning int number to a variable, how many times the player can attempt to guess the word:
        # By changing this number, the amount of attempts will change for the game. Can be decreased down to 0.
        # if this is set to 0, the condition ''while attempts > 0'' won't ever apply and the player will immediately loose
        attempts = 4
        # pulling global variable into the function, so the function can change its value based on the outcome of the game
        global player_health
        # informing the player that a new game is starting...
        typewrite_fast(r""" 


    ╔═╗╔╗╔╔═╗╔═╗╦═╗╔═╗╔╦╗
    ╠═╣║║║╠═╣║ ╦╠╦╝╠═╣║║║
    ╩ ╩╝╚╝╩ ╩╚═╝╩╚═╩ ╩╩ ╩

    """)

        print()
        typewrite("Let's see if you can understand my language!")
        typewrite("It's harder than you think!")
        # a loop to make sure the user has 4 attempts to guess the correct word:
        while attempts > 0:
            # the devil gives the player a corrupted word from corrupted variable
            typewrite("I say: "+corrupted)
            # taking input of a guess what the word might be from the user:
            guess = input("What do I mean? Type here: ")
            # it's easier to set just one condition - if the word from the list and guessed word match it's a win
            # checking anything else isn't required, because this is the only way to win the game
            if guess == chosen_word:
                # letting the player know they guessed correctly and changing the value of global variable
                typewrite("Maybe you are better than I thought. But that won't save you forever!")
                # the game should end here if the player guessed well, so I can skip the rest
                return
            # once the if loop ends, I need to make sure the attempt is reduced. 
            attempts -= 1
            # telling the user they are wrong and that how many times they can try this. I had to increase it by 1
            # for it to make sense for the user:
            print(typewrite("You are WRONG! You can try again! I give you: "),attempts+1," chance!")
        # when the if condition fails, and attemps = 0 the game will inform the player they lost and the correct word
        typewrite("Wrong, wrong, wrong wrong WRONG! You have no chance against me!")
        typewrite("The correct translation is: "+chosen_word+" but that's no use for you now!")
        baby_dont_hurt_me(player_health)
        # global variable gets updated so it can be used later on in the overall program


    # need to run the game
    game_code()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# roll dice game function:
def dicegame():
    global player_health
    typewrite_fast(r""" 





 ______      _____     ____    _____  
(_  __ \    (_   _)   / ___)  / ___/  
  ) ) \ \     | |    / /     ( (__    
 ( (   ) )    | |   ( (       ) __)   
  ) )  ) )    | |   ( (      ( (      
 / /__/ /    _| |__  \ \___   \ \___  
(______/    /_____(   \____)   \____\ 
                                      


.........................................................


""")
    typewrite("Let's see if you can even win when playing against yourself.")
    typewrite("Here - take these dice and roll them!")
    def dice_number():
        _ = input("Press enter to roll the dice")
        die1 = random.randrange (1, 7)
        die2 = random.randrange (1, 7)
        return (die1, die2)
    def dice_sum(dice):
        die1, die2 = dice
        print("You have rolled {} and {} for a total of {}".format(die1,die2,sum(dice)))
    value = dice_number()
    dice_sum(value)
    sum_of_dices = sum(value)
    # Result 1 win, result 2 lose, result 3 set new point and try to match

    if sum_of_dices in (7, 11):
        result = 1
    

    elif sum_of_dices in (2, 3, 12):
        result = 2

    else: 
        result = 3
        target = sum_of_dices
        print("To win you need to roll", target)

    while result == 3:
        value = dice_number()
        dice_sum(value)
        sum_of_dices = sum(value)
        
        if sum_of_dices == target:
            result = 1
            
        elif sum_of_dices == 7:
            result = 2
    

    if result == 1:
        typewrite("Either you have a protector, or you are just lucky this time.")
        typewrite("None will last forever, I promise you!")
        
    else:
        typewrite("You lose....er, Hahahaha!")
        baby_dont_hurt_me(player_health)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# hangman game function:
def hangman():
# Word library
    words = 'pies hypnotic grass door unbecoming whine birthday flight deranged experience'.split()
    typewrite_fast(r""" 




 _      __    _      __    _       __    _     
| |_|  / /\  | |\ | / /`_ | |\/|  / /\  | |\ | 
|_| | /_/--\ |_| \| \_\_/ |_|  | /_/--\ |_| \| 

.........................................................


""")
    typewrite("Have you ever heard about people being hanged?")
    typewrite("I don't actually care. We are playing hangman now!")
    input("I wish you bad luck!")
    def randomword(wordList):
        wordlib = random.randint(0, len(wordList) - 1)
        return wordList[wordlib]
    word = randomword(words)

    guesses = ''
    turns = 10

    while turns > 0:
        lose = 0
        for char in word:
            if char in guesses:
                print (char,end=" "),
            else:
                print ("_",end=" "),
                lose +=1


        if lose == 0:
            # Continue onto the next room without losing health
            typewrite ("Well. I will give you another chance. Run until I catch you again!")
            input("")
            break

        guess = input (" Guess a letter: ")
        guess = guess.lower()
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong!", + turns, 'guesses left...' )
            if turns == 0:
                typewrite ("Your soul... is MINE! Hahaha")
                input()
                death_screen()           
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Blackjack game function:
def blackjack():
    playerin = True
    dealerin = True
    deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        "J","Q","K","A","J","Q","K","A","J","Q","K","A","J","Q","K","A",]
    playerhand = []
    dealerhand = []
    typewrite_fast(r""" 
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ 
""")

    typewrite("I am shuffling....................................................")
    typewrite("Thank you, dealing the cards now..................................")
    input("Hit enter when ready to view the cards.")
    def dealcard(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)
    
    def total(turn):
        total = 0
        face = ['J','Q','K']
        for card in turn:
            if card in range(1,11):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total 

    def revealdealerhand():
        if len(dealerhand) == 2:
            return dealerhand[0]
        elif len(dealerhand) > 2:
            return dealerhand[0], dealerhand[1]
    
    for _ in range(2):
        dealcard(dealerhand)
        dealcard(playerhand)
    
    while playerin or dealerin:
        typewrite(f"The dealer has {revealdealerhand()} and X")
        typewrite(f"You have {playerhand} for a total of {total(playerhand)}")
        if playerin:
            stayorhit = input("1: Stay\n2: Hit\n")
        if total(dealerhand) > 16:
            dealerin = False
        else:
            dealcard(dealerhand)
        if stayorhit == '1':
            playerin = False
        else:
            dealcard(playerhand)
        if total(playerhand) >= 21:
            break
        elif total(dealerhand) >= 21:
            break
    
    if total(playerhand) == 21:
        typewrite(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for the total of {total(dealerhand)}")
        typewrite("Blackjack! You win")
    
    elif total(dealerhand) == 21:
        typewrite(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for the total of {total(dealerhand)}")
        typewrite("Blackjack! Dealer wins!")
    
    elif total(playerhand) > 21:
        typewrite(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for the total of {total(dealerhand)}")
        typewrite("You bust! Dealer wins!")
    
    elif total(dealerhand) > 21:
        typewrite(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for the total of {total(dealerhand)}")
        typewrite("Dealer has bust! You win!")
    
    elif 21 - total(dealerhand) < 21 - total(playerhand):
        typewrite(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for the total of {total(dealerhand)}")
        typewrite("Dealer wins")
    
    elif 21 - total(dealerhand) > 21 - total(playerhand):
        typewrite(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for the total of {total(dealerhand)}")
        typewrite("You win!")
    
    elif total(playerhand) == total(dealerhand):
        typewrite(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for the total of {total(dealerhand)}")
        typewrite(f"\nYou and the dealer have the same total \nIt's a draw!")
    typewrite("Thank you for playng.")
    input("Please hit enter to continue.")    
# ====================================================================================
# ====================================================================================
# ====================================================================================
# 
# Adding screens to the game:
# ====================================================================================
# Starting screen:
players_name = "None"
def start_screen():
    import time
    from datetime import datetime, timedelta
    from time import sleep
    import sys
    global players_name
    def typewrite_fast(text):
        lines = [text]
        redtext = '\033[31m'
        ENDC = '\033[m'
        
            # for each line of text (or each message) 
        for line in lines:   
            # for each character in each line 
            for c in line:                 
                # print a single character, and keep the cursor there.
                print(redtext + c, end='')    
                    # flush the buffer
                sys.stdout.flush()
                    # wait a little to make the effect look good.
                sleep(0.0025)
            print(ENDC + '')        

    typewrite_fast(r"""
    (                        (                                          
    )\ )                 )   )\ )              (                        
    (()/(      )  (    ( /(  (()/(     (     )  )\ (          (  (       
    /(_))  ( /(  )(   )\())  /(_))   ))\ ( /( ((_))\   (     )\))(  (   
    (_))_   )(_))(()\ ((_)\  (_))_   /((_))(_)) _ ((_)  )\ ) ((_))\  )\  
    |   \ ((_)_  ((_)| |(_)  |   \ (_)) ((_)_ | | (_) _(_/(  (()(_)((_) 
    | |) |/ _` || '_|| / /   | |) |/ -_)/ _` || | | || ' \))/ _` | (_-< 
    |___/ \__,_||_|  |_\_\   |___/ \___|\__,_||_| |_||_||_| \__, | /__/ 
                                                            |___/       
    """)

    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()

    
    print_slow("Welcome to Dark Dealings!")
    print_slow("Prepare yourself for a terrifying experience.")
    print_slow("You find yourself on an adventure in Vegas \ntempting your fate to see if it's on your side.")
    # print_slow("Your objective is to escape with a profit and uncover the  dark secrets the casino's are hiding.")
    print_slow("Before we begin, security want to see your ID")
    playername = input("What is the name on your ID ")
    players_name = playername   
    # def calculate_age(birth_date):
    #     current_date = datetime.now()
    #     age = current_date.year - birth_date.year
            
    #     if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    #         age -= 1
    #     return age
    # birth_date_str = input("Enter the birth date on your ID (YYYY-MM-DD): ")
    # birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    # age = calculate_age(birth_date)
    # if age >= 21:
    #     print()
    #     print_slow(f"Welcome {playername} ")
    #     input(f"Press enter to dive into the game...")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     full_game()
    # else:
    #     typewrite("Not old enough, unable to continue")
    #     input("If an adult allows you to play this game, please hit enter")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     print("")
    #     full_game()
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    full_game()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Bet soul dialog:
def bet_soul():
    def restart_the_game_prompt():
        # printing space
        print()
        # printing options
        typewrite("1. Yeah, not doing that...")
        typewrite("2. I don't care about my soul, I will beat you!")
        print()
        # assigning value to variable from user input
        choice = input("Enter your choice (1/2): ")
        # making sure input is correct and if not, then to ask for it again
        while choice not in ['1', '2']:
            choice = input("Invalid choice. Please enter 1 or 2: ")
        return choice
    # main dialog for the end game function:
    def main_dialog():
        typewrite_fast(r"""
                                                            
_-_ _,,           ,                                 
   -/  )         ||                                 
  ~||_<    _-_  =||=       '\\/\\  /'\\ \\ \\ ,._-_ 
   || \\  || \\  ||         || ;' || || || ||  ||   
   ,/--|| ||/    ||         ||/   || || || ||  ||   
  _--_-'  \\,/   \\,        |/    \\,/  \\/\\  \\,  
 (                         (                        
                            -_-                     
            __      _ _    _ ,                      
  -_-/    ,-||-,   - - /  - -  _-_-                 
 (_ /    ('|||  )    ('||  ||   /,                  
(_ --_  (( |||--))  (( ||--||   ||                  
  --_ ) (( |||--))  (( ||--||  ~||                  
 _/  ))  ( / |  )   (( /   ||   ||                  
(_-_-     -____-      -___-\\, (  -__,              
                                                    
                                                    
        """)
        sleep(3)
        typewrite("Nice game. Let's make it more interesting!")
        typewrite("Would you bet your soul?")
        # variable assigned based on the user input using function restart_the_game_prompt
        choice = restart_the_game_prompt()
        if choice == '1':
            typewrite("Brilliant!!!")
            input("Your soul is mine!")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            death_screen()
        elif choice == '2':
            print("Perfect, let's do it!")
            sleep(3)
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
    # at this stage not sure how we will make the game to start over. Will have to think about it further.
    main_dialog()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Death screen:
def death_screen():

    def typewrite_fast(text):
        lines = [text]
        redtext = '\033[31m'
        ENDC = '\033[m'
    
        # for each line of text (or each message) 
        for line in lines:   
        # for each character in each line 
            for c in line:                 
            # print a single character, and keep the cursor there.
                print(redtext + c, end='')    
                # flush the buffer
                sys.stdout.flush()
                # wait a little to make the effect look good.
                sleep(0.001)          
            print(ENDC + '')


    typewrite_fast(r""" 
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄  ▐██▌ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌ ▐██▌ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌ ▐██▌ 
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌ ▓██▒ 
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓  ▒▄▄  
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒  ░▀▀▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒  ░  ░ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░     ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░     ░    
 ░ ░                           ░                  ░            """)
    
     # defining function to restart the game prompt
    def restart_the_game_prompt():
        # printing space
        print()
        # printing options
    
        lines1 = ["As you feel the room spin and your vision begins to fade, you hear a voice ask:\nDo you wish to play again? Y/N. "]
        for line in lines1:          
            for c in line:          
                print(c, end='')  
                sys.stdout.flush()  
                sleep(0.05)      
                
        # assigning value to variable from user input
        choice = input()
        choice == choice.lower
        # making sure input is correct and if not, then to ask for it again
        while choice not in ["y", "n"]:
            choice = input("Invalid choice. Please enter Y or N: ")
            
        return choice
    # main dialog for the end game function:
    def main_dialog():       
        choice = restart_the_game_prompt()
        if choice == 'n':
            typewrite("Game ended.")
            sleep(3)
            end_game()
        elif choice == 'y':
            typewrite("Game restarted.")
            sleep(2)
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            global player_health
            player_health = 100
            start_screen()
    # at this stage not sure how we will make the game to start over. Will have to think about it further.
    main_dialog()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Win screen:
def win_screen():

    def typewrite_fast(text):
        lines = [text]
        from time import sleep
        import sys
        # for each line of text (or each message) 
        for line in lines:   
        # for each character in each line 
            for c in line:                 
            # print a single character, and keep the cursor there.
                print(c, end='')    
                # flush the buffer
                sys.stdout.flush()
                # wait a little to make the effect look good.
                sleep(0.001)          
            print('')


    # defining the function for ASCII printing

        # r is for raw text 
        # https://stackoverflow.com/questions/23623288/print-full-ascii-art
    typewrite_fast(r"""
     /$$     /$$                        /$$                                          
    |  $$   /$$/                       | $$                                          
     \  $$ /$$//$$$$$$  /$$   /$$      | $$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$       
      \  $$$$//$$__  $$| $$  | $$      | $$__  $$ |____  $$|  $$  /$$//$$__  $$      
       \  $$/| $$  \ $$| $$  | $$      | $$  \ $$  /$$$$$$$ \  $$/$$/| $$$$$$$$      
        | $$ | $$  | $$| $$  | $$      | $$  | $$ /$$__  $$  \  $$$/ | $$_____/      
        | $$ |  $$$$$$/|  $$$$$$/      | $$  | $$|  $$$$$$$   \  $/  |  $$$$$$$      
        |__/  \______/  \______/       |__/  |__/ \_______/    \_/    \_______/      



                                                                       /$$ /$$       
                                                                      | $$| $$       
      /$$$$$$   /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$| $$       
     /$$__  $$ /$$_____/ /$$_____/ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$       
    | $$$$$$$$|  $$$$$$ | $$        /$$$$$$$| $$  \ $$| $$$$$$$$| $$  | $$|__/       
    | $$_____/ \____  $$| $$       /$$__  $$| $$  | $$| $$_____/| $$  | $$           
    |  $$$$$$$ /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$$|  $$$$$$$ /$$       
     \_______/|_______/  \_______/ \_______/| $$____/  \_______/ \_______/|__/       
                                            | $$                                     
                                            | $$                                     
                                            |__/                                     
                                            """)
    # defining function to restart the game prompt
    def restart_the_game_prompt():
        # printing space
        print()
        # printing options
        typewrite("1. I don't dare to say your name! (End the game)")
        typewrite("2. I am not scared to say your name! (Play again)")
        print()
        # assigning value to variable from user input
        choice = input("Enter your choice (1/2): ")
        # making sure input is correct and if not, then to ask for it again
        while choice not in ['1', '2']:
            choice = input("Invalid choice. Please enter 1 or 2: ")
        return choice
    # main dialog for the end game function:
    def main_dialog():
        typewrite("You have escaped. I dare you to say my name out loud!")
        typewrite("Ready?")
        # variable assigned based on the user input using function restart_the_game_prompt
        choice = restart_the_game_prompt()
        if choice == '1':
            typewrite("Game ended.")
            sleep(3)
            end_game()
        elif choice == '2':
            typewrite("Game restarted.")
            sleep(2)
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            global player_health
            player_health = 100
            start_screen()
    # at this stage not sure how we will make the game to start over. Will have to think about it further.
    main_dialog()
# ====================================================================================
# ====================================================================================
# ====================================================================================
# 
# Following the diagram and adding it to the game:
# ====================================================================================

def full_game():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    # loading screen
    for specific_time in range (0,5):  
        loading_waiting = "Loading" + "." * specific_time
        print (loading_waiting, end="\r")
        time.sleep(1)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    typewrite("Welcome to the BlackJack table, I can see you have placed your bet already.")
    typewrite("Let's play.")
    input()
    blackjack()
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    # once player wins or looses, the devil wants another game for their soul. Player has to accept to continue
    # otherwise the game ends here and we call the death screen - devil takes the soul without asking
    # ===============================================================
    bet_soul()
    blackjack()

    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    # Here - options to go left or right



    # def fourchoices():
    #     roomchoices = [1, 2, 3, 4]
    #     typewrite("filler rext, left or right")
    #     userinput = ""
    #     while userinput not in roomchoices:
    #         typewrite("left or right")
    #         userinput = input.int()
    #         if userinput == "1":
    #             typewrite("")
    #             anagram_game() 
    #             # church
    #         if userinput == "2":
    #             typewrite("")
    #             dicegame()
    #             # street
    #         if userinput == "3":
    #             typewrite("")
    #             rock_paper_scissors_spock()
    #             # casino
    #         if userinput == "4":
    #             typewrite("")
    #             toss_a_coin()
    #             # shop
                
    #         else:
    #             typewrite("You have to choose a direction!")
    # function for the selections:
    def start_another_game_prompt():
        # printing space
        typewrite("1. Attempt to escape to the church")
        typewrite("2. Attempt to escape to another casino")
        typewrite("3. Attempt to escape following the street road")
        typewrite("4. Attempt to escape to a gun shop")
        # assigning value to variable from user input
        choice = input("Enter your choice (1/2/3/4): ")
        # making sure input is correct and if not, then to ask for it again
        while choice not in ['1', '2','3','4']:
            choice = input("You have to choose an escape route!")
        return choice
    # main dialog for the user first time on the street - this runs after the hell_exterior - choice left
    def first_dialog():
        typewrite("You turned left and you can see a few escape routes.")
        typewrite("Your options are:")
            # variable assigned based on the user input using function restart_the_game_prompt
        choice = start_another_game_prompt()
        if choice == '1':
            typewrite("The church stands like a beacon of hope in this hellish landscape, you're sure if you can make it there it will provide sanctuary\nYou gather your strength and begin to sprint towards the entrance.\nAs you get closer you realise that the doors and windows are boarded shut and a heavy chain is locking the front gate.\nYou try to adjust course and find somewhere else to run to, but it's too late, your attacker is upon you.")
            input("Press enter to dodge their attack!")
            typewrite("Going somewhere?")
            typewrite("Don't worry I won't leave you alone...")
            for specific_time in range (0,3):  
                loading_waiting = "Loading" + "." * specific_time
                print (loading_waiting, end="\r")
                time.sleep(1)
            dicegame()
        elif choice == '2':
            typewrite("You run towards the casino, hopefully if the other one brought you here, then somehow this one has the key to escaping.\n As you run closer it dawns on you how much this looks like the casino you just left, almost exactly alike.\nFrom the style and layout, right down to the huge fire burning inside it.\nYou spin on your heel and try to run somewhere else, but it's too late. The demon has caught up with you. ")
            input("Press enter to dodge their attack!")
            typewrite("Going somewhere?")
            typewrite("Don't worry I won't leave you alone...")
            for specific_time in range (0,3):  
                loading_waiting = "Loading" + "." * specific_time
                print (loading_waiting, end="\r")
                time.sleep(1)
            toss_a_coin()
        elif choice == '3':
            typewrite("'Yeah', you think to yourself 'Hiding isn't the best plan but maybe I can outrun this guy'\nYou launch yourself at full speed down the deserted street, you feet beating against the uneven path\nSuddenly you feel the ground begin to shake like it did in the casino, just for a moment, you lose your balance and slowly stumble, you try to adjust and resume your escape but it's too late\nThat momentary stop is all it took.  In a flash the demon darts in front of you, blocking your path.")
            input("Press enter to dodge their attack!")
            typewrite("Going somewhere?")
            typewrite("Don't worry I won't leave you alone...")
            for specific_time in range (0,3):  
                loading_waiting = "Loading" + "." * specific_time
                print (loading_waiting, end="\r")
                time.sleep(1)
            anagram_game()
        elif choice == '4':
            typewrite("The gun store seems like the obvious choice, if you can get something to defend yourself then maybe you'll be able to survive here.\nYou run as fast of you can towards the store, it's neon sign growing brighter with every step.\nYou fix your gaze on the sign and push forward, blinkering yourself against any distraction, just focused on making it there and soon.\nIn fact, you're so fixated on the sign that you fail to notice that the windows of the store have heavy shutters pulled down tight over them, you don't notice the chuncky chain and padlock wrapped around the door, and you definitely don't notice the footsteps growing louder behind you\nYou slam heavily into the front door and bounce right off, as you spin and right yourself you see the demon standing directly in front of you.")
            input("Press enter to dodge their attack!")
            typewrite("Going somewhere?")
            typewrite("Don't worry I won't leave you alone...")
            for specific_time in range (0,3):  
                loading_waiting = "Loading" + "." * specific_time
                print (loading_waiting, end="\r")
                time.sleep(1)
            rock_paper_scissors_spock()
    # left_right option function:
    def left_right():
        # printing space
        typewrite("1. Turn right and try to open the red door")
        typewrite("2. Turn left and see if there is a better escape route")
        # assigning value to variable from user input
        choice = input("Enter your choice (1/2): ")
        # making sure input is correct and if not, then to ask for it again
        while choice not in ['1', '2']:
            choice = input("You have to choose a direction!")
        return choice
    # progressing story - describing the change of environment and allowing the player select their escape route (left/right)
    def hell_exterior():
        # directions = ["left", "right"]
        typewrite("The room begins to shake violently, sending plaster flying from the ceiling.") 
        sleep(3)
        print("")
        typewrite("Smoke belches from craters where sections of the floor should be, as they crumble into nothingness.")
        sleep(3)
        print("")
        typewrite("Flames lick up the walls, stripping the paint and pushing flakes of it into the air.")
        sleep(3)
        print("")
        typewrite("The intense heat makes the air shimmer like a mirage, but you know that this is really happening.")
        sleep(3)
        print("")
        typewrite("You need to get out. Fast...")
        sleep(3)
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        typewrite("You burst through the door and into the street outside. \nThe chaos unfolding inside the casino seems to have spread to the rest of the city; \nthe sky is blood red and fires have broken out as far as the eye can see.")
        sleep(3)
        print("")
        print("")
        typewrite("Directly in front of you a huge fire is beginning to grow; \nyou can feel the heat from here, there's no way you can go in that direction.  \nTo your left you see a row of buildings; maybe shops or bars? \nYou'll have to get closer to see. To your right you can see a vast wall with a mysterious red door")
        sleep(3)
        print("")
        print("")
        typewrite("Suddenly from behind you, a voice cries out 'THERE IS NO HOPE, YOUR SOUL IS MINE!'")
        print("")
        print("--------------------------------------------------------------------------------------------")
        typewrite("You need to run, which direction do you go?")
        sleep(3)

            # variable assigned based on the user input using function restart_the_game_prompt
        choice = left_right()
        if choice == '1':
            typewrite("You run towards the door, the sound of heavy footsteps of your pursuer filling your ears. \nAfter what seems like an eternity the door handle is within reach, \nyou stretch out your hand and grasp it, turning violently, but it refuses to budge.")
            typewrite("Your pursuer is already behind you.")
            typewrite("Gotcha.....")
            sleep(5)
            hangman()       
        elif choice == '2':
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            first_dialog()

        # userinput = input("Type left or right to choose the escape path!")
        # while userinput not in directions:
        #     typewrite("left or right")
        #     userinput = input.lower()
        #     if userinput == "left":
        #         # street
        #         typewrite("")
        #         first_dialog()
        #     if userinput == "right":
        #         # door
        #         typewrite("You run towards the door, the sound of heavy footsteps of your pursuer filling your ears. After what seems like an eternity the door handle is within reach, you stretch out your hand and grasp it, turning violently, but it refuses to budge.")
        #         typewrite("")
        #         hangman()
        #     else:
        #         typewrite("You have to choose a direction!")
    hell_exterior()  
    for specific_time in range (0,5):  
        loading_waiting = "Loading" + "." * specific_time
        print (loading_waiting, end="\r")
        time.sleep(1)
    if player_health == 0:
       death_screen()

    # after ending with the left option = turning left on the street, they can run to:
    # shop with guns - heart (need to replace these in diagram)
    # church - spades (need to replace these in diagram)
    # another casino - 3rd symbol (need to replace in diagram)
    # try to run away from the street (need to replace in diagram)

    # shop option - devil catches the player before they manage to enter and starts flip coin
    # church option - devil catches the player before they enter and starts anagram
    # casino option - the same but starts rock paper scissors
    # street run option - devil catches them and starts dice roll game
    # ============================================
    # hangman()
    # print(player_health)
    # if player_health == 0:
    #     death_screen()
    # ============================================
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    # Second round for the games
    # main dialog for the second escape on the street:
    def second_dialog():
        typewrite("You have managed to slip out and run back to the middle of the street.")
        sleep(1)
        typewrite("Your options are:")
            # variable assigned based on the user input using function restart_the_game_prompt
        choice = start_another_game_prompt()
        if choice == '1':
            typewrite("The church stands like a beacon of hope in this hellish landscape, you're sure if you can make it there it will provide sanctuary\nYou gather your strength and begin to sprint towards the entrance.\nAs you get closer you realise that the doors and windows are boarded shut and a heavy chain is locking the front gate.\nYou try to adjust course and find somewhere else to run to, but it's too late, your attacker is upon you.")
            input("Press enter to dodge their attack!")
            typewrite("Going somewhere'?")
            typewrite("Don't worry I won't leave you alone...")
            for specific_time in range (0,3):  
                loading_waiting = "Loading" + "." * specific_time
                print (loading_waiting, end="\r")
                time.sleep(1)
            dicegame()
        elif choice == '2':
            typewrite("You run towards the casino, hopefully if the other one brought you here, then somehow this one has the key to escaping.\n As you run closer it dawns on you how much this looks like the casino you just left, almost exactly alike.\nFrom the style and layout, right down to the huge fire burning inside it.\nYou spin on your heel and try to run somewhere else, but it's too late. The demon has caught up with you. ")
            input("Press enter to dodge their attack!")
            typewrite("Going somewhere?")
            typewrite("Don't worry I won't leave you alone...")
            for specific_time in range (0,3):  
                loading_waiting = "Loading" + "." * specific_time
                print (loading_waiting, end="\r")
                time.sleep(1)
            toss_a_coin()
        elif choice == '3':
            typewrite("'Yeah', you think to yourself 'Hiding isn't the best plan but maybe I can outrun this guy'\nYou launch yourself at full speed down the deserted street, you feet beating against the uneven path\nSuddenly you feel the ground begin to shake like it did in the casino, just for a moment, you lose your balance and slowly stumble, you try to adjust and resume your escape but it's too late\nThat momentary stop is all it took.  In a flash the demon darts in front of you, blocking your path.")
            input("Press enter to dodge their attack!")
            typewrite("Going somewhere?")
            typewrite("Don't worry I won't leave you alone...")
            for specific_time in range (0,3):  
                loading_waiting = "Loading" + "." * specific_time
                print (loading_waiting, end="\r")
                time.sleep(1)
            anagram_game()
        elif choice == '4':
            typewrite("The gun store seems like the obvious choice, if you can get something to defend yourself then maybe you'll be able to survive here.\nYou run as fast of you can towards the store, it's neon sign growing brighter with every step.\nYou fix your gaze on the sign and push forward, blinkering yourself against any distraction, just focused on making it there and soon.\nIn fact, you're so fixated on the sign that you fail to notice that the windows of the store have heavy shutters pulled down tight over them, you don't notice the chuncky chain and padlock wrapped around the door, and you definitely don't notice the footsteps growing louder behind you\nYou slam heavily into the front door and bounce right off, as you spin and right yourself you see the demon standing directly in front of you. ")
            input("Press enter to dodge their attack!")
            typewrite("Going somewhere?")
            typewrite("Don't worry I won't leave you alone...")
            for specific_time in range (0,3):  
                loading_waiting = "Loading" + "." * specific_time
                print (loading_waiting, end="\r")
                time.sleep(1)
            rock_paper_scissors_spock()
    second_dialog()
    for specific_time in range (0,5):  
        loading_waiting = "Loading" + "." * specific_time
        print (loading_waiting, end="\r")
        time.sleep(1)
    if player_health == 0:
       death_screen()
    else:
        win_screen()

    # shop option - devil catches the player before they manage to enter and starts flip coin
    # church option - devil catches the player before they enter and starts anagram
    # casino option - the same but starts rock paper scissors
    # street run option - devil catches them and starts dice roll game

    # the player can then run again, choosing from the remaining options i.e. 
    # if selected church, only the other 3 options will be presented in the next round
    # once selected, the relevant game will start

    # after each game check player_health
    # if player_health == 0:
    #   death_screen()


def end_game():
    print("")
start_screen()
end_game()
