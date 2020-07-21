from collections import defaultdict
import math


def moving_window(tweet, window):
    """
    Create Phrases of length(window) rolling through tweet

    Parameters
    ----------
    tweet: str, tweet to break into phrases
    window: int, number representing number of words in phrase

    Returns
    -------
    phrases :  Boolean, True if line contains county name
    """
    words = tweet.split()
    phrasesDictTweet = defaultdict(int)

    # Error Handling If Window > Tweet length
    if len(words) - (window - 1) >= 0:
        # loop through words in tweet
        for i in range(len(words) - (window - 1)):
            # Create Phrase
            phrase = ""
            for j in range(window):
                phrase = str(phrase + " " + str(words[i + j]))

            # Add Phrase to Dict
            phrasesDictTweet[phrase] += 1

    return phrasesDictTweet

## Testing
tweet = "SPECIAL SECRET HEARTS: A Child's Introduction to Dementia and Pink Curls - A Santa ... - http://t.co/UWCdc8FA9a http://t.co/meexKLGTKl"
window = 3
print(moving_window(tweet, window))


def cosine(tweet1, tweet2, window):
    """
    Calculates Cosine (similarity) between two tweets

    Parameters
    ----------
    tweet1: str, first tweet to compare in Cosine calculation
    tweet2: str, first tweet to compare in Cosine calculation

    Returns
    -------
    cosine_value :  float, representing cosine value between tweet1 and tweet2
    """

    matches = 0

    # Load Tweets
    tweet1_dict = moving_window(tweet1, window)
    tweet2_dict = moving_window(tweet2, window)
    n1 = sum(tweet1_dict.values())
    n2 = sum(tweet2_dict.values())

    # Return 0 if one argument is empty
    if n1 == 0 or n2 == 0:
        return 0

    # Count how many phrases match
    for phrase1, appearances1 in tweet1_dict.items():
        for phrase2, appearances2 in tweet2_dict.items():
            if phrase1 == phrase2:
                matches += appearances1 * appearances2
    cosine_value = matches / math.sqrt((n1 * n2))
    return cosine_value

# Testing
tweet1 = "SPECIAL SECRET HEARTS: A Child's Introduction to Dementia and Pink Curls - A Santa ... - http://t.co/UWCdc8FA9a http://t.co/meexKLGTKl"
tweet2 = "RT @BuyBookstore: SPECIAL SECRET HEARTS: A Child's Introduction to Dementia and Pink Curls - A Santa ... - http://t.co/UWCdc8FA9a http://t."
window = 3

print(cosine(tweet1, tweet2, window))

# Test to show different matches calculation
tweet1 = "This is a random This is a nothing This is a Test"
tweet2 = "This is a random1 This is a nothing1 This is a Test1"
window = 3

print(cosine(tweet1, tweet2, window))


def near_duplicate(tweet1, tweet2, window, duplicateThreshold):
    """
    Determine if two tweets are near duplicates (Cosine Value > duplicateThreshold)

    Parameters
    ----------
    tweet1: str, first tweet to compare in Cosine calculation
    tweet2: str, first tweet to compare in Cosine calculation
    window: int, number representing number of words in phrase
    duplicateThreshold: float, threshold cosine value has to exceed (strictly), in order
                        for two tweets to be considered near duplicates

    Returns
    -------
    near_duplicate_tweets :  bool, True if tweets are near duplicates, False otherwise
    """
    # Initialize near_duplicate_tweets bool as False
    near_duplicate_tweets = False

    # Determine if cosine of two tweets exceed duplicateThreshold
    if cosine(tweet1, tweet2, window) > duplicateThreshold:
        near_duplicate_tweets = True

    return near_duplicate_tweets


def near_duplicate_analysis_tweets(tweets, window, duplicateThreshold):
    """
    Determine what tweets of collection of tweets in txt file are near duplicates

    Parameters
    ----------
    tweets: txt file read in
    window: int, number representing number of words in phrase
    duplicateThreshold: float, threshold cosine value has to exceed (strictly), in order
                        for two tweets to be considered near duplicates

    Returns
    -------
    near_duplicate_tweets :  lst, lists duplicates tweets and their respective cosine values
    """
    tweet_collection = []
    tweet = tweets.readline()
    while tweet is not '':
        # Add tweet to tweet collection
        tweet_collection.append(tweet)

        # Read next line of file to get next tweet (or end the loop)
        tweet = tweets.readline()

    near_duplicate_tweets = []
    num_tweets = len(tweet_collection)

    # Loop Through Tweets, avoiding duplicates and avoiding repeat analysis of tweets
    for tweet1_index in range(num_tweets):
        for tweet2_index in range(tweet1_index + 1, num_tweets):
            # Store Both Tweets To Analyze
            tweet1 = tweet_collection[tweet1_index - 1]
            tweet2 = tweet_collection[tweet2_index - 1]

            # If Tweets near duplicates, add to list
            if near_duplicate(tweet1, tweet2, window, duplicateThreshold):
                message = str("Tweet: " + tweet_collection[tweet1_index] + " is a near duplicate to Tweet: "
                              + tweet_collection[tweet2_index] + " with a Cosine Value of: " +
                              str(cosine(tweet1, tweet2, window))
                              )
                near_duplicate_tweets.append(message)

    return near_duplicate_tweets

# Testing
tweets = open('Data/Santa.txt', 'r')
window = 3
duplicateThreshold = 0.5

print(near_duplicate_analysis_tweets(tweets, window, duplicateThreshold))







