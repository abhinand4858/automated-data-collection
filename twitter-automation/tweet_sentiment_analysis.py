from twython import Twython
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


con_key = ''
con_key_secret = ''
acc_token = ''
acc_token_secret = ''

twitter = Twython(con_key, con_key_secret, acc_token, acc_token_secret)

analyzer = SentimentIntensityAnalyzer()

max_count = 15
earlier_tweet_id = 0
tweet_count = 0
tweet_score = {}

while max_count > tweet_count:

	tweet_id_list = []

	if earlier_tweet_id <= 0:	
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=10, tweet_mode='extended', exclude_replies='true')
	else:
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=10, max_id=earlier_tweet_id - 1, tweet_mode='extended', exclude_replies='true')

	for tweet in tweets:
		tweet_count += 1
		tweet_id_list.append(tweet['id'])

		#finding and storing sentimental score for each tweet text
		score = analyzer.polarity_scores(tweet['full_text'])
		tweet_score[tweet['id']] = score

	if(len(tweets)):
		earlier_tweet_id = sorted(tweet_id_list)[0]
	else: 
		tweet_count=max_count
	
#print score of each tweet
for t, s in tweet_score.iteritems():
	print t, s


