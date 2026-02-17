import os
os.chdir("cs4300/homework1")    # doesnt run without specifying the directory

# open the file as 'r' (read) and count each word
def word_counter(fileName):
    with open(fileName, 'r') as file:
        content = file.read()
        wordsOnly = content.split() #removes whitespaces, tabs, newlines, spaces, etc.
        wordCount = len(wordsOnly)
        return wordCount


word_counter('task6_read_me.txt')