"""This is a wordle helper utility
    Micah Johnson helped me with how to treat the parameter none when it was passed in. He gave me the idea for bool in my show possible
    words funciton
    https://www.w3schools.com/python/ref_func_all.asp
    https://www.w3schools.com/python/ref_func_all.asp
"""
import sys

def userGuess(green: str | None, yellow: str | None, grey: str | None)->str|dict[str,int]|set[str]:
    """This function takes in the user inputs and assigns them for organization
    
    Args: green(str): green is the characters already in the right place
          yellow(str): yellow is the characters that are in the word but not in the right place
          grey(str): grey is the characters that are not included in the word
    """
    greyList = []
    yellowDict = {}
    
    #Yellow Letters
    yellowDict = spiltString(yellow)
    
    #Grey Letters list
    for char in grey: 
        if char not in greyList:
            greyList.append(char)
        else: pass
    greySet = set(greyList)

    return green, yellowDict, greySet

def spiltString(yellow: str)->dict[str, int]:
    yCannotBe = {}
    i = 0
    while i<len(yellow):
        key = yellow[i]
        i+=1
        values = []
        while i<len(yellow) and yellow[i].isdigit():
            values.append(int(yellow[i])-1)
            i+=1
        if values: yCannotBe[key] = values
    return yCannotBe

def readToList(fileWords: str)->list[str]:
    listWords = []
    with open(fileWords, 'r') as file:
        for line in file: listWords.append(line.strip())
    
    return listWords
        
def deleteGrey(words: list[str], greyLetters: set[str])-> list[str]:
    possibleWords = []
    for word in words:
        if any(char in greyLetters for char in word): continue
        else: possibleWords.append(word)
    return possibleWords

def deleteYellow(words: list[str], yellowLetters: dict[str,int])->list[str]:
    wordsCopy = []
    for word in words:
        validWord = True
        for key, positions in yellowLetters.items():
            if key not in word: 
                validWord = False
                break
            for pos in positions:
                if word[pos] == key:
                    validWord = False
                    break
            if not validWord: break
        if validWord: wordsCopy.append(word)

    return wordsCopy
    
def returnGreen(words: list[str], greenLetters: dict[str, int])->list[str]:
    possibleWords = []
    for word in words:
        if all(word[value] == key for key, value in greenLetters.items()): possibleWords.append(word)
        else: continue    
    return possibleWords

def showPossibleWords(words: list[str], letters: str, also: dict[str, int] | None, gone: set | None)->None:
    """
    This function takes in a list of words, green letters, yellow letters, and grey letters for the game wordle. It will then iterate through
    the list of words and print the possible words that the wordle can be.

    args: words(list[str]): list of all possible wordle answers
    letters(str): green letters
    also(dict{str, int}): dictionary of yellow letters and their position
    gone(set[str]): list of all not avaible grey characters
    """
    greenDict = {}

    #Green Letters dict: use a dict because it gives location and character
    for i in range(len(letters)):
        if letters[i] != ".":
            greenDict[letters[i]] = i

    if bool(gone): updatedWords = deleteGrey(words, gone)
    else: updatedWords = words    
    if bool(also):
        updatedWords2 = deleteYellow(updatedWords, also)
    else: updatedWords2 = updatedWords
    finalWords = returnGreen(updatedWords2, greenDict)

    for word in finalWords:
        print(word)

def main() -> None:
    green, yellow, grey = userGuess(sys.argv[1], sys.argv[2], sys.argv[3])
    listWords = readToList("wordle_answers.txt")
    showPossibleWords(listWords, green, yellow, grey)

if __name__ == "__main__":
    main()


