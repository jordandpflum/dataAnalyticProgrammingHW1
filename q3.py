import re

santaTweets = open('Data/Santa.txt', 'r')






def collapseLst(lst):
    return str(''.join(lst))

def removeSybmbolsWord(str):
    str = str.split('')
    matches = re.findall('[a-zA-Z]', word)
    return collapseLst(matches)








# Initialize Phrase Length
phraseLen = 3

# Initialize Line with first line
line = santaTweets.readline()
while line is not '':
    # Clear Spaces From Line
    line = line.rstrip()
    line = line.lstrip()

    # Clear Symbols Before and After Line
    line = line.lstrip('^[a-zA-Z]')

    # Get Rid of @names

    line = line.split(' ')
    print(line)
    tmpLine = []
    for word in line:
        matches = re.findall('[a-zA-Z]', word)
        if len(matches) > 0:
            print(collapseLst(matches))
            tmpLine.append(collapseLst(matches))


    print("Tmpline: " + str(tmpLine))

    # Advance to next line


    print(line)
    line = santaTweets.readline()



