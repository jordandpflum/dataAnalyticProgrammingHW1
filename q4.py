import re
from collections import defaultdict

quotesRaw = open('Data/quotes.txt', 'r')



def oddNum(num):
    if (num % 2) == 0:
        return False
    else:
        return True


def compileQuotes(quotesRaw):
    # Initialize Quotes
    quotes = []

    # Initialize Line with first line
    line = quotesRaw.readline()
    lineNum = 1
    while line is not '':
        # Clear Spaces From Line
        line = line.rstrip()
        line = line.lstrip()

        # Determine if quote or author line
        if oddNum(lineNum):
            # Save Quote
            quote = line
        else:
            # Save Author
            author = line

            # Append quote + author to quotes list
            quotes.append(str(quote) + " - " + str(author))



        # Advance to next line
        line = quotesRaw.readline()
        lineNum += 1

    return quotes

#print(compileQuotes(quotesRaw))

quotes = compileQuotes(quotesRaw)


def extractQuoteWords(quote):
    return quote.split('. - ')[0].lower().split(" ")


def extractAllQuotes(quotes):
    for quote in quotes:
        print(quote)
        print(extractQuoteWords(quote))
    pass

def buildPostingListDict(quotes):
    postingListDict = {}
    for quote in quotes:
        simpQuote = extractQuoteWords(quote)
        postingListDict[quote] = defaultdict(int)
        for word in simpQuote:
            postingListDict[quote][word] += 1

    return postingListDict

postingListDict = buildPostingListDict(quotes)

# Testing
print(postingListDict["The heart has its reasons, of which the mind knows nothing. - Blaise Pascal"])
