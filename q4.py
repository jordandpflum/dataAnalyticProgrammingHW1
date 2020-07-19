import re
from collections import defaultdict
import math
import numpy as np

quotesRaw = open('Data/quotes.txt', 'r')


def oddNum(num):
    """
    Deterimine if number is odd or even

    Parameters
    ----------
    num = int, a number

    Returns
    -------
    Boolean :  bool, True if number is odd, False if number is even
    """
    if (num % 2) == 0:
        return False
    else:
        return True


def compileQuotes(quotesRaw):
    """
    Compile txt file of quotes into list of the form ["Quote - Author",...]

    Parameters
    ----------
    quotesRaw = raw txt file of quotes read in

    Returns
    -------
    quotes :  lst, list of quotes
    """
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

quotes = compileQuotes(quotesRaw)

def collapseLst(lst):
    return str(''.join(lst))

def extractQuoteWords(quote):
    """
    Extract author of quote from quote+author

    Parameters
    ----------
    quote = str, quote of the form "Quote - Author"

    Returns
    -------
    lst, list strings of words contained in the quote
    """
    words = quote.split(" ")
    quote_alt = []
    for word in words:
        matches = re.findall('[a-zA-Z]', word)
        word_alt = collapseLst(matches)
        if len(word_alt) > 0:
            quote_alt.append(word_alt.lower())
    return quote_alt


def buildPostingListDict(quotes):
    """
    Build posting list dicitonary of compiled Quotes of the form "Quote - Author"

    Parameters
    ----------
    quotes = lst, list of quotes of the form ["Quote - Author",...]

    Returns
    -------
    postingListDict, list representing posting list dicitonary of compiled Quotes
                     of the form postingListDict[quote][word] = num of times word appears in that quote
    """
    postingListDict = {}
    for quote in quotes:
        simpQuote = extractQuoteWords(quote)
        postingListDict[quote] = defaultdict(int)
        for word in simpQuote:
            postingListDict[quote][word] += 1

    return postingListDict


def buildReversePostingListDict(quotes):
    """
    Build reverse posting list dicitonary of compiled Quotes of the form "Quote - Author"

    Parameters
    ----------
    quotes = lst, list of quotes of the form ["Quote - Author",...]

    Returns
    -------
    reversePostingListDict, list representing reverse posting list dicitonary of compiled Quotes
                     of the form reversePostingListDict[word][quote] = num of times word appears in that quote
    """
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
print(postingListDict["The heart has its reasons, of which the mind knows nothing. - Blaise Pascal"])


reversePostingListDict = buildReversePostingListDict(quotes)


print(reversePostingListDict["entertainer"])


def TF_IDF(word, quote, quotes):
    """
    Calculate TF-IDF of word in quote

    Parameters
    ----------
    word = str, string of word for TF-IDF calculation
    quote = str, string of quote for TF-IDF calculation
    quotes = lst, list of quotes of the form ["Quote - Author",...]

    Returns
    -------
    tfidf_val, TF-IDF value of word in quote
    """
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
    """
    Search quotes for word, returning dictionary whose keys are quotes containing word and values
    the TF-IDF calculation of that word and quote

    Parameters
    ----------
    word = str, string of word to search for in quotes
    quotes = lst, list of quotes of the form ["Quote - Author",...]

    Returns
    -------
    quoteSearchResult, dictionary whose keys are quotes containing word and values
                       the TF-IDF calculation of that word and quote
    """
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
    """
    Search quotes for multples words, returning dictionary whose keys are quotes containing one or more of the
    input words and values the sum of TF-IDF calculation of those word and quote

    Parameters
    ----------
    words = lst, list of strings of words to search for in quotes
    quotes = lst, list of quotes of the form ["Quote - Author",...]

    Returns
    -------
    quoteSearchResult, dictionary whose keys are quotes containing word and values
                       the TF-IDF calculation of that word and quote
    """
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
