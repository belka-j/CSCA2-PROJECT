#the logic behind the define functions(line 1 to line 63) was used from lab 8
#we modified them to fit into our code

#importing the file so we can read and write into it
import csv

with open("Score.List.csv") as reader_file:
    # Read the file
    reader = csv.reader(reader_file)
    # Make it a list type, so it's easier to manage the data
    data = list(reader)



def read_csv():

    # Open the file given so we can read what's inside
    with open("Score.List.csv") as reader_file:
        # Read the file
        reader = csv.reader(reader_file)
        # Make it a list type, so it's easier for to manage the data
        data = list(reader)
    # The first row of the data has the header
    # The rest of the data are records and will be stored in the database
    return (data[0], data[1:])



def write_to_csv(data):

    # To make our database more organized, we will sort our csv file
    data.sort(key=lambda k: k[0])
    header = read_csv()[0]
    # Open the file given so we can write on it
    with open("Score.List.csv", 'w', newline="") as writer_file:
        writer = csv.writer(writer_file)
        # When we write the updated scorelist back on the file.
        writer.writerows([header] + data)



def add_score(name, score):

    # Create a new record
    scorelist = read_csv()[1]
    player_score = [name, score]
    # Add the player score at the end of the scorelist
    scorelist += [player_score]
    # Write the new scorelist to the file
    write_to_csv(scorelist)


#the code below changes the score of an already existing player in the scorelist
def change_score(name, new_score):

    scorelist = read_csv()[1]
    # we check which item in the scorelist matches the current player's name 
    for player_score in scorelist:
        if player_score[0] == name:
            #when the match is found the code below adds the new score
            #to the already existing one
            player_score[1] = int(player_score[1]) + new_score
         
    write_to_csv(scorelist)



def get_player_score(name):
    # Loop through every item in the scorelist list (every row)
    scorelist = read_csv()[1]
    for player_score in scorelist:
        if player_score[0] == name:
            return int(player_score[1])



#this define function prints the right picture of the hangman depending on
# how many aguesses are left
def draw_hangman(guesses_left):
    if guesses_left == 6:
        print ("________      ")
        print ("|      |      ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
    elif guesses_left == 5:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
    elif guesses_left == 4:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /       ")
        print ("|             ")
        print ("|             ")
    elif guesses_left == 3:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|      ")
        print ("|             ")
        print ("|             ")
    elif guesses_left == 2:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|             ")
        print ("|             ")
    elif guesses_left == 1:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|     /       ")
        print ("|             ")
    else:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|     / \     ")
        print ("|             ")



def replace_dashes(word, dashes, guess):
    result = ""
    #looping through every character in the word
    for character in range(len(word)):
        #if the guessed letter matches the index character
        if word[character] == guess:
            # Adds the guess to the  string if the guess is correct
            result = result + guess
        else:
    # Add the dash at index character to the result if it doesn't match the guess
            result = result + dashes[character]
    return result


#Hangman game 

answer = input("Enter a username to start playing Hangman: ")
player_ = answer 
print("Welcome to Hangman, " + player_ + " !")


# we got the lines 156-159 from the internet - stackoverflow.com;
#it turns the columns into a list
from csv import DictReader

with open("Score.List.csv") as f:
    names = [row["Name"] for row in DictReader(f)]
    #set names to start from the 2nd row(first is empty)
    names = names[1:]

#setting this variable to yes so that the game can be played a smany times
#as the player wants, whenever play again is not yes the loop will stop
play_again = "yes"

while play_again == "yes": 
  attempts = 6
  import random
#random word is chosen from the csv file and saved
  words = open('CommonWords.csv').read().splitlines()
  my_word = random.choice(words)

#the game starts, the word is printed as a multiple of _ for every letter in the word

  print("The game has begun! Your word has " + str(len(my_word)) + " letters. You have 6 attempts. Good luck!")
  guess_word = "_" * len(my_word)
  print("Word: " + guess_word)
  draw_hangman(attempts)


  Game_mode = "none"
  #check that only one letter is entered and that it is a letter in the alphabet and only lower case
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  #going to add the guessed letter to this list, so that player's don't
  #pick the same letter twice
  list_letter = []
  


  #the loop is going to work while the player has attempts left or until the word is guessed
  while not(Game_mode == "won" or Game_mode == "lost"):
    answer = input("Guess a letter: ")
    guessed_letter = answer 
    #checking for the valid input(lower case, only one letter)
    if not guessed_letter in alphabet or not len(guessed_letter) == 1:
        print("Only one letter and a lower case can be used")
    #checking if the letter has already been guessed
    elif guessed_letter in list_letter:
        print("You have already guessed this letter! Try again!")
    #checking if the letter guessed is in the randomized word
    elif guessed_letter in my_word:
        #adding the guessed letter to a list to keep track of the used letter
        list_letter.append(guessed_letter)
        print("You guessed correctly!")
        #replacing the dash with the guessed letter
        guess_word = replace_dashes(my_word, guess_word, guessed_letter)
        print(guess_word) 
        # if no more dashes, that means the word has been guessed, and the player one
        if not "_" in guess_word:
            print("CONGRATULATIONS! You Won!")
            #setting the game modet o won so that the loop stops
            Game_mode = "won"

          # checking if the player is in the scorelist
            #if they are
            if player_ in names:
                #changing the score by the number of attempts left
                change_score(player_, int(attempts))
            else:
                #adding the player and their score to the scorelist 
                add_score(player_, attempts)
    else:
        #adding the guessed letter to a list to keep track of the used letter
        list_letter.append(guessed_letter)
        # subtracting one from attempts because they guessed wrong
        attempts -= 1
        print(guess_word)
        # if attempts is less than 1 it means the player lost
        if attempts < 1:
            print ("GAME OVER! Better Luck Next Time! The word was: " + (my_word))
            #setting the game_mode to lost so that the loop stops
            Game_mode = "lost"
            draw_hangman(attempts)

            # checking if the player is in the scorelist
              #if they are
            if player_ in names:
                #subtracting one from their existing score
                change_score(player_, -1)

            else:
                #if the player is playing for the first time
                #add their name and a score of 0 to the scorelist
                add_score(player_, 0)

        #if they have 1 attempts left, notify them that they have only 1 try left
        elif attempts == 1:
            print("Wrong guess! This is your last chance!")
            draw_hangman(attempts)
            print(guess_word)
        # else just say the guess was wrong and how many attempts they have left
        else:
            print("Wrong guess! You have " + str(attempts) + " attempts left!")
            draw_hangman(attempts)
            print(guess_word)

  #print their total score
  print("Your total score is " + str(get_player_score(player_)))
  answer = input("Do you want to play again? Enter yes to play again, or enter smth else to STOP. ")
  #set play again to answer tp either stop or repeat the loop
  play_again = answer



from csv import DictReader
# we got the lines 266-270 from stackoverflow.com
#it turns the columns into a list
with open("Score.List.csv") as f:
    scores = [row["Score"] for row in DictReader(f)]
    #set scores to start from the 2nd row(first is empty)
    scores = scores[1:]
    #loop through every score and turn it into an integer
    for i in range(len(scores)):
        scores[i] = int(scores[i])

#check for the player"s name that corresponds with the highest score from the score list
#set index to 0 to start checking from the first score
index = 0
#loop through every score
for item in scores:
    #if the score matches the maximum score
    if scores[index] == max(scores):
        #set the player with the highest score to the corresponding name 
        highest_score_player = names[index]
    #chnage index by 1 to check the next score/name
    index += 1

print("The player with the highest score is " + (highest_score_player) + " with " + str(max(scores)) + " points.")