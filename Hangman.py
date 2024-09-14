#Hangman because why not?
import os

word = "What is the word"

print("Welcome to hangman!!!")
word = word.strip().lower()
guessed_letters = []
fill = []
vic = 0
score = 7
word_length = len(word)

for i in word:
    if i != ' ':
        fill.append("_")
    else:
        fill.append(' ')


def print_fill():
    for x in range(len(fill)):
        print(fill[x], end=' ')

print_fill()
def add_fill(letter):
    pos = 0
    global vic
    for pos in range(word_length):
        if letter in word[pos]:
            fill[pos] = letter
            pos = pos + 1
            vic = vic + 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def guess():
    while True:
        global score
        global vic
        if score == 0:
            print("\n\n")
            print(f"You have lost... the word is '{word}'")
            print("\n\n")
            return 0
        if vic == word_length:
            print("\n\n")
            print(f"Congrats! You guessed '{word}' correctly! You win!")
            print("\n\n")
            return 0
        letter = input(f"\n\n~You have {score} wrong guesses left~\nEnter a letter: ")
        if len(letter) != 1:
            clear_screen()
            print("Only one letter please!")
            continue 

        if letter in guessed_letters:
            clear_screen()
            print(f"You alrady guessed {letter.upper()}, try again\n")
            print_fill()
            continue
        elif letter in word:
            clear_screen()
            print(f"{letter.upper()} is in the word! Keep going!\n")
            add_fill(letter)
            guessed_letters.append(letter)
            print_fill()
            
            
        else:
            clear_screen()
            print(f"{letter.upper()} is not in the word! Try again!\n")
            score = score - 1
            print_fill()
            
            
            


guess()