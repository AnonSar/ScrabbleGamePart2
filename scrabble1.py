import sys
import random


TILES_USED = 0 # records how many tiles have been returned to user
SHUFFLE = False # records whether to shuffle the tiles or not

# inserts tiles into myTiles
def getTiles(myTiles):
    myTiles.clear()
    myTiles += ['B','A','N','A','E','G','T']


# prints tiles and their scores
def printTiles(myTiles):
    tiles = ""
    scores = ""
    for letter in myTiles:
        tiles += letter + "  "
        thisScore = getScore(letter)
        if thisScore > 9:
            scores += str(thisScore) + " "
        else:
            scores += str(thisScore) + "  "

    print("\nTiles : " + tiles)
    print("Scores: " + scores)

# gets the score of a letter
def getScore(letter):
    for item in Scores:
        if item[0] == letter:
            return item[1]



scoresFile = open('scores.txt')
tilesFile = open('tiles.txt')

# read scores from scores.txt and insert in the list Scores
Scores = []
for line in scoresFile:
    line = line.split()
    letter = line[0]
    score = int(line[1])
    Scores.append([letter,score])
scoresFile.close()

# read tiles from tiles.txt and insert in the list Tiles
Tiles = []
for line in tilesFile:
    line= line.strip()
    Tiles.append(line)
tilesFile.close()

# decide whether to return random tiles
rand = input("Do you want to use random tiles (enter Y or N): ").upper()
if rand == "Y":
    SHUFFLE = True
else:
    if rand != "N":
        print("You did not enter Y or N. Therefore, I am taking it as a Yes :P.")
        SHUFFLE = True
        
if SHUFFLE:
    random.shuffle(Tiles)


myTiles = []
getTiles(myTiles)
printTiles(myTiles)

print(" ")
word = input("Enter a word: ").upper()

#checks whether the user input "user_input_1" includes only alphabetic characters or not
def WordCheck(user_input_1):
    if user_input_1.isalpha() == False:
        if user_input_1 == '***': 
            print("Better luck next time.")
            return False
        else:             
            print("Only Use English letters !!!")
            return False
    else:                  
        return True

#checks whether the user input "user_input_2" exists in the dictionary or not
def DictCheck(user_input_2):
    file =""
    file = open("dictionary.txt","r")
    for word_2 in file: 
        word_2 = word_2.replace("\n","")
        if user_input_2 == word_2:
            return True 
    else: 
        return False
    file.close()
    
#checks whether the user input "user_input_3" can be made with the given tiles or not
def TilesCheck(user_input_3):
    list_1 = []
    list_2 = []
    counter = 0
    for char_1 in user_input_3:
        list_1.append(char_1)
    for char_2 in myTiles:
        list_2.append(char_2)
        
    for char_3 in list_1:        
            for char_4 in list_2:
                if char_3 == char_4:#checks whther a charcater of user input = character of mytiles or not
                    list_2.remove(char_4) 
                    counter += 1#If a character of myTiles = user input "user_input_3" then add 1 to counter
                    break
    if counter != len(list_1):   #if the word cannot be made using tiles, return False 
        return False
    elif counter == len(list_1): #if the word can be made using tiles, return true
        return True

#calculates the score of the user input "user_input_4" 
def score_of_the_word(user_input_4):
    counter_1 = 0
    for letter in Scores:
        for letter_1 in user_input_4:
            if letter[0] == letter_1:#checks if the user input character = the letter stored in the "Scores"
                counter_1 += letter[1]#add the score of the alphabet to "counter_1" occuring in user input
                                                   
    return counter_1   #returning the score of the word


#calculates the word with the highest score
def HighestScore(text):
    text_2 = ""
    WordScore = 0
    list_3 = [0]
    file_1 = ""
    file_1 = open("dictionary.txt","r")
    for text_1 in file_1:#for checking each word in the dictionary
        text_1 = text_1.replace("\n","")
        if TilesCheck(text_1) == True:#checks what all words of the dictionary with the given tiles
             WordScore = score_of_the_word(text_1)#stores the score of the valid word in "WordScore"
             list_3.append(WordScore)             #that can be made with given tiles
             if list_3[0] < WordScore:
                 list_3[0] = WordScore#stores the highest scores in "list_3[0]"
                 text_2 = text_1#stores the word with highest score in "text_2"

    if list_3[0] == 0:
        print("No word can be made using these tiles.")
    else:
        print("The word " +text_2 + " is the word with highest score. It's score is " + str(list_3[0]))

    file_1.close()#closing the dictionary    
    

while word != "***":
    
    if WordCheck(word) == True: 
        if DictCheck(word) == True:
            if TilesCheck(word) == True:
                print("Cool, this is a valid word.")
                WordScore_1 = score_of_the_word(word)
                print("Score of the word "+word+" is: " + str(WordScore_1))
                print(" ")
                HighestScore(word)
                break
            
            else:
                print("This word cannot be made using your tiles.")
                print(" ")
                word = input("Enter a word: ").upper()
                
        else:
            print("I have never heard of this word.")
            print(" ")
            word = input("Enter a word: ").upper()

    else:
        print(" ")
        word = input("Enter a word: ").upper()
    
    
else: #if the user enters "***" then prints the message and prints the word with with highest score 
   WordCheck(word)
   print(" ")
   HighestScore(word)
