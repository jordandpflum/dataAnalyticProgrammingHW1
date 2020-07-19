import re
from collections import defaultdict
import math

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


# print(compileQuotes(quotesRaw))

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


def buildReversePostingListDict(quotes):
    reversePostingListDict = {}
    for quote in quotes:
        simpQuote = extractQuoteWords(quote)
        for word in simpQuote:
            if reversePostingListDict.get(word) == None:
                reversePostingListDict[word] = {quote: 1}
            else:
                if reversePostingListDict[word].get(quote) == None:
                    reversePostingListDict[word][quote] = 1
                else:
                    reversePostingListDict[word][quote] += 1

    return reversePostingListDict


postingListDict = buildPostingListDict(quotes)

# Testing
# print(postingListDict["The heart has its reasons, of which the mind knows nothing. - Blaise Pascal"])


reversePostingListDict = buildReversePostingListDict(quotes)


# print(reversePostingListDict["entertainer"])


def TF(word, postingListDict_quote):
    pass


def IDF(word, postingListDict_quote):
    pass


def TF_IDF(word, quote, quotes):
    postingListDict = buildPostingListDict(quotes)
    reversePostingListDict = buildReversePostingListDict(quotes)

    # TF Calculation
    tf_val = postingListDict[quote][word] / max(postingListDict[quote].values())

    # IDF Calculation
    idf_val = math.log(len(quotes) / len(reversePostingListDict[word]))

    # TF-IDF Calculation
    tfidf_val = tf_val * idf_val

    return tfidf_val


tfidf_val = TF_IDF(word="entertainer",
                   quote="An actor is at most a poet and at least an entertainer. - Marlon Brando",
                   quotes=quotes
                   )
print(tfidf_val)


def quoteSearchSingleWord(word, quotes):
    postingListDict = buildPostingListDict(quotes)
    reversePostingListDict = buildReversePostingListDict(quotes)

    quoteSearchResult = {}
    for quote in reversePostingListDict[word].keys():
        quoteSearchResult[quote] = TF_IDF(word, quote, quotes)

    return quoteSearchResult


singleSearchResult = quoteSearchSingleWord(word="entertainer",
                                           quotes=quotes
                                           )
print(singleSearchResult)


def quoteSearchMultipleWords(words, quotes):
    postingListDict = buildPostingListDict(quotes)
    reversePostingListDict = buildReversePostingListDict(quotes)

    quoteSearchResult = {}
    for word in words:
        if reversePostingListDict.get(word) == None:
            pass
        else:
            for quote in reversePostingListDict[word].keys():
                if quoteSearchResult.get(quote) == None:
                    quoteSearchResult[quote] = TF_IDF(word, quote, quotes)
                else:
                    quoteSearchResult[quote] += TF_IDF(word, quote, quotes)

    return quoteSearchResult


multipleSearchResult = quoteSearchMultipleWords(words=["heart", "mind", "disease"],
                                                quotes=quotes
                                                )
print(multipleSearchResult)

tfidf_val_1 = TF_IDF(word="heart",
                   quote="The heart has its reasons, of which the mind knows nothing. - Blaise Pascal",
                   quotes=quotes
                   )

tfidf_val_2 = TF_IDF(word="mind",
                   quote="The heart has its reasons, of which the mind knows nothing. - Blaise Pascal",
                   quotes=quotes
                   )

print(sum([tfidf_val_1, tfidf_val_2]))
