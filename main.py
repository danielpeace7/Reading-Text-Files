# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# from cgitb import text
# from itertools import count


def readfile(filename):
    # [assignment] Add your code here 
    openFile = open("C:\\Users\\hi\\Downloads\\Reading-Text-Files\\story.txt", "r")
    readFile = openFile.read()
    # print(readFile)
    # print(openFile)
    return(readFile)

def count_words():
    text = readfile("C://Users//hi//Downloads//Reading Text Files//story.txt")
    
    splitText = text.split()
    #print(splitText)

    count ={}
    for i in splitText:
        if i in count:
            count[i] += 1
        else:
            count[i] =1
    return count

print(count_words())