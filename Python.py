import pandas as pd
# read dataset
df = pd.read_csv('correct_twitter_201904.tsv', sep='\t')
print(df.columns) #explore all columns
#term = "music"

# Used NoSQL
def tweets_per_day(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets.groupby('created_at')['id'].count()
# tweets per dat
print("Tweets per day:", tweets_per_day(term))

#count the number of tweets containing a specific term per day
def unique_users(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets['author_id'].nunique()
print("Unique users:", unique_users(term))

#get unique place IDs from tweets containing the term
def places(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets['place_id'].unique()
print("Places:", places(term))

#count the occurrences of tweets by time of day
def tweet_times(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets['created_at'].value_counts()
print("Tweet times:", tweet_times(term))

# Function to find the user who posted the most tweets containing the term
def top_user(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets['author_id'].value_counts().idxmax()
print("Top user:", top_user(term))

