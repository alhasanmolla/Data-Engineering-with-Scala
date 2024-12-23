from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import tweepy
import pandas as pd

# Twitter API credentials
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

def fetch_tweets(**kwargs):
    # Set up Tweepy API authentication
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    # Fetch tweets from a specific user (e.g., @elonmusk)
    tweets = tweepy.Cursor(api.user_timeline, screen_name='@elonmusk', tweet_mode='extended').items(100)
    
    # Create a list of dictionaries
    tweet_data = [{'tweet_id': tweet.id_str, 
                   'text': tweet.full_text, 
                   'created_at': tweet.created_at, 
                   'retweet_count': tweet.retweet_count, 
                   'favorite_count': tweet.favorite_count} for tweet in tweets]
    
    # Convert to DataFrame
    df = pd.DataFrame(tweet_data)
    
    # Save to CSV (with execution date to avoid overwriting)
    df.to_csv(f'/path/to/save/elonmusk_tweets_{kwargs["ds"]}.csv', index=False)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'twitter_data_pipeline',
    default_args=default_args,
    description='A Twitter data pipeline for @elonmusk tweets',
    schedule_interval=timedelta(days=1),
)

fetch_tweets_task = PythonOperator(
    task_id='fetch_tweets',
    python_callable=fetch_tweets,
    provide_context=True,
    dag=dag,
)

fetch_tweets_task
