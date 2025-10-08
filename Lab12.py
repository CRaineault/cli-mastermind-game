# Lab 12 - Customizable Mastermind Game - Cassandra Raineault - December 7th, 2021

from random import randint



def get_code_color(peg_count, repeats):

    if (peg_count <= 6) or (peg_count > 6 and repeats == "y"):
        hidden_code = []
        for n in range(peg_count):
            if repeats == "n":
                needs_reroll = True
                while needs_reroll == True:
                    color_num = randint(1,6)
                    if color_num not in hidden_code:
                        needs_reroll = False
                        hidden_code.append(color_num)
            else:
                color_num = randint(1,6)
                hidden_code.append(color_num)
                
    elif peg_count > 6 and repeats == "n":
        hidden_code = []
        for n in range(peg_count):
            needs_reroll = True
            while needs_reroll == True:
                color_num = randint(1,10)
                if color_num not in hidden_code:
                    needs_reroll = False
                    hidden_code.append(color_num)
                
    return hidden_code

def convert_code_into_colors(hidden_code):
    for n in range(len(hidden_code)):
        if hidden_code[n] == 1:
            hidden_code[n] = "Blue"
            
        elif hidden_code[n] == 2:
            hidden_code[n] = "Red"
        
        elif hidden_code[n] == 3:
            hidden_code[n] = "Green"
            
        elif hidden_code[n] == 4:
            hidden_code[n] = "Yellow"
        
        elif hidden_code[n] == 5:
            hidden_code[n] = "Pink"
            
        elif hidden_code[n] == 6:
            hidden_code[n] = "White"
            
        elif hidden_code[n] == 7:
            hidden_code[n] = "Black"
            
        elif hidden_code[n] == 8:
            hidden_code[n] = "Orange"
            
        elif hidden_code[n] == 9:
            hidden_code[n] = "Brown"
            
        elif hidden_code[n] == 10:
            hidden_code[n] = "Purple"
            
    return hidden_code
            
def get_code_num(peg_count, repeats):
    
    hidden_code = []
    for n in range(peg_count):
        if repeats == "n":
            needs_reroll = True
            while needs_reroll == True:
                num = randint(1, 10)
                if num not in hidden_code:
                    needs_reroll = False
                    hidden_code.append(num)
        else:
            num = randint(1, 10)
            hidden_code.append(num)
            
    return hidden_code


def check_guess(user_guess, hidden_code):
    if len(user_guess) != len(hidden_code):
        return "Error"
    
    hits = 0
    blows = 0
    hit_list = []
        
    for i in range(len(user_guess)):
        
        if user_guess[i] == str(hidden_code[i]):
            hits += 1
            hit_list.append(user_guess[i])
        
    checked_list = []
        
    for i in range(len(user_guess)):
        
         if user_guess[i] in str(hidden_code) and str(hidden_code[i]) != user_guess[i]:
            
            if checked_list.count(user_guess[i]) < str(hidden_code).count(user_guess[i]) and hit_list.count(user_guess[i]) < str(hidden_code).count(user_guess[i]):
                blows += 1
        
         checked_list.append(user_guess[i])
        
    result = [hits, blows]
     
    return result
    
    
            
def set_up_game():
    settings_choice = input("\nIf you have played the game before, you may choose to reload your settings from the last game you played. Load settings (y/n)?: ")
    
    if settings_choice == "y":
         f = open("mastermindsettings.txt", "r")
         f_text = f.read()
         game_version = int(f_text[0])
         peg_count = int(f_text[1])
         repeats = f_text[2]
    
    
    
    
    else:
        game_version = 0
        peg_count = 0
        repeats = ""
        while game_version < 1 or game_version > 2:
            game_version = int(input("Would you like to play (1) Original Mastermind (colored pegs) or (2) Number Mastermind?: "))
        while peg_count < 4 or peg_count > 10:
            peg_count = int(input("How long would you like the hidden code to be? (4-10 pegs): "))
        while repeats != "y" and repeats != "n":
            repeats = input("Would you like to have repeat colors/numbers? (y/n): ")
   
    if game_version == 1:
        hidden_code = get_code_color(peg_count, repeats)
        hidden_code = convert_code_into_colors(hidden_code)
    elif game_version == 2:
        hidden_code = get_code_num(peg_count, repeats)
        
    settings = [str(game_version), str(peg_count), repeats]
    f = open("mastermindsettings.txt", "w")
    for stat in settings:
        f.write(stat)
    f.close()
    
    return hidden_code
    

def play_game():
    hidden_code = set_up_game()
    
    if 4 <= len(hidden_code) <= 6:
        guess_count = 8
        
    elif len(hidden_code) <= 8:
        guess_count = 12
        
    else:
        guess_count = 16
     
    rounds_played = 0
    for r in range(guess_count):
        user_guess = []
        for n in range(len(hidden_code)):
            guess = input(str("Enter your guess for the color/number in position #" + str(n+1) +" (color names should be capitalized): "))
            user_guess.append(guess)
        
        result = check_guess(user_guess, hidden_code)
        
        print("\nYour results are:", result[0], "hit(s) and", result[1], "blow(s).")
        rounds_played +=1
        
        
        if result[0] == len(hidden_code):
            game_result = "Win"
            
            overall_result = [game_result, rounds_played]
            
            return overall_result
        
    game_result = "Lose"
    overall_result = [game_result, rounds_played]
    print("The hidden code was: ", hidden_code, "\n")
    return overall_result
            
    
def main():
    print("Welcome to Customizable Mastermind!")
    give_instructions = input("Would you like to read the game instructions? (y/n): ")
    if give_instructions == "y":
        print("\n")
        instructions = open("README.txt", "r")
        instruction_lines = instructions.readlines()
        for line in instruction_lines:
            print(line)
    
    continue_playing = True
    win_count = 0
    loss_count = 0
    while continue_playing == True:
        result = play_game()
        if result[0] == "Win":
            win_count += 1
            print("Congratulations! You guessed the correct code after", result[1], "round(s)\n.")
        else:
            loss_count += 1
            print("Sorry, but you lost this time.\n")
        print("\nResults so far:\nWins: ", win_count, "\tLosses: ", loss_count)
        play_again_choice = input("\nPlay again? Type 'yes' or 'y' to confirm: ")
        if play_again_choice == "Yes" or play_again_choice == "yes" or play_again_choice == "y":
            continue_playing = True
        else:
            continue_playing = False
    print("Thank you for playing! Exiting...")
    


if __name__ == "__main__":
    main()