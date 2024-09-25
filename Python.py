import pandas as pd

df = pd.read_csv('correct_twitter_201904.tsv', sep='\t')
print(df.columns)
#term = "music"
def tweets_per_day(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets.groupby('created_at')['id'].count()

print("Tweets per day:", tweets_per_day(term))
def unique_users(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets['author_id'].nunique()
print("Unique users:", unique_users(term))

def places(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets['place_id'].unique()
print("Places:", places(term))
def tweet_times(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets['created_at'].value_counts()
print("Tweet times:", tweet_times(term))

def top_user(term):
    term_tweets = df[df['text'].str.contains(term, case=False, na=False)]
    return term_tweets['author_id'].value_counts().idxmax()
print("Top user:", top_user(term))

