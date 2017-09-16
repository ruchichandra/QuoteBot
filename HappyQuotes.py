# Dependencies
import tweepy
import json
import time
import random

# Twitter API Keys
consumer_key = "IBGGnfEVkiWyiy378JZUGTa7R"
consumer_secret = "kKLPE1KsUjyQAZyuo1RVFD3wncEZ7ByTJfxtAz32RkIibTpG0o"
access_token = "857769437113577472-F9b6yeB1bLZuWoTGDtLWftwHC6y307S"
access_token_secret = "m3K1meWntHu7V8koLPag4C5RCp64PgQXhBPOH2PjRDE0p"

# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]

    # Create function for tweeting
def HappyQuotes():

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet a random quote
    api.update_status(random.choice(happy_quotes))

    # Print success message
    print("Tweeted successfully!")


# Set timer to run every minute
while(True):
    HappyQuotes()
    time.sleep(60)

   # Add 1 to the counter prior to re-running the loop
    counter = counter + 1
