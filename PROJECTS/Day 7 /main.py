import random 

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
print(chosen_word)
display = []

for _ in range(len(chosen_word)):
  display += "_"
print(display)

again = False
lives = 6 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

while again == False:
    guess = input("Guess a letter: ").lower()
     
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter 

    if guess not in chosen_word:
        lives -= 1 
        if lives == 0:
          again = True
          print("You lose")
    
    print(f"{' '.join(display)}")

    print(display)
    if "_" not in  display:
      again = True
      print("You win.")

    print(stages[lives])