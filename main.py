import random
from hangingFIG import showcase
from word_list import words
from hangman_art import art
from colorama import Fore, Back, Style
from replit import audio

  
def choose_random_word(list):
  '''Args:
      list : list of words 
    Returns:
      a random word from the list of words which the help of random fuction
    Examples:
      choose_random_word(["abruptly", "absurd","abyss","affix"]-> "absurd"
      choose_random_word(["apple", "orange", "one"]->
         "orange"
  '''

  return random.choice(list)

def vision(art):
  '''Args: 
        list of hanging figure
     Return:
        a hanging figure on level with live decrease.
  '''
  return showcase

def guessing(disperse_list):
    global guess
    guess = input("Guess a letter: ")
    guess = guess.lower()

    if not guess.isalpha():
        ans = "Enter a Letter only. Every other things are not allowed"
        ans += "\n"

    elif len(guess) != 1:
        print("Enter a single character only.\n")
    elif guess in disperse_list:
        print("Chose another letter. You have already chosen this word")
      
def main():
    play = True
    print("-------------" + Fore.RED + "WELCOME TO HANGMAN GAME" + Style.RESET_ALL+"-------------")
    print(Fore.GREEN + art+ Style.RESET_ALL + "\n" + "\n")
    print(Back.RED + "INSTRUCTIONS:"+ Style.RESET_ALL + "\n")
    print("1. Guess the character in word")
    print("2. You have 6 chances to the guess word correctly")
    print("3. On every wrong guess chance is reduced by one, which won’t be counted on a correct guess"+ "\n")
    print(Fore.LIGHTMAGENTA_EX + "LET'S START" + Style.RESET_ALL + "\n")

    source = audio.play_file('piano.mp3')

    stages = vision(art)

    life_line = 6

    chosen_word = choose_random_word(words)

    disperse_list = []
    for letter in chosen_word:
        disperse_list += "_"
    print(disperse_list)
    # if the chosen_word is "hello", then the disperse_list will have a undercase equal to the number of character in "hello". ie
    #disperse_list = ["_","_","_","_","_"]
    while play:
        guessing(disperse_list)
        
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                letter = chosen_word[i]
                if letter == guess:
                    disperse_list[i] = letter
        # if a letter in the position is same as guess, then "_" will get replaced by guess letter in that same position.
      
        else:
            print("This is not a desired letter. You have " + str(life_line) + " left.")
            life_line -= 1
            if life_line == 0:
                print(Fore.CYAN + stages[life_line]+ Style.RESET_ALL)
                print("Your life_line are over. You lose. Better luck next time" + "\n")
                print("The word is " + chosen_word)
                break
                
                play = False

        print("\n")

        if "_" not in disperse_list:
            print(disperse_list)
            print("CONGRATULATION! You guess the word correctly. You win")
            
            play = False
            break
        
        print(Fore.CYAN + stages[life_line]+ Style.RESET_ALL)
        print(disperse_list)

    
    while input("\nDo you want to play again?. Enter yes to play again and no to quit.").lower() == "yes":
      main()

    print("\n" +Fore.GREEN +"See you again"+ Style.RESET_ALL )


  
if __name__ == "__main__":
    main()