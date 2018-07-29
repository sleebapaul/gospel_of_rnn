import random 
import string
from string import punctuation

# Get all the alphabets 
alphabetsList = list(string.ascii_letters) 

# Get all the punctuations
punctuationList = list(punctuation)

# Create a dictionary with all these characters and space
dictionary = alphabetsList + punctuationList + [" "]


def randomCharPicker(aList):
    """
    Returns a randomly selected a character from aList
    Probability of selection is 1 / length of dictionary
    """
    return random.choice(aList)


if __name__ == "__main__":
    tempSentence = ""
    # Creating a sentence of 100 characters
    for _ in range(100):
        # Pick a random charater from dictionary
        randomChar = randomCharPicker(dictionary)
        # Append it to the output sentence
        tempSentence += randomChar
        # Display the sentence
        print("Current sentence: {}".format(tempSentence))