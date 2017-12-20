from __future__ import division
from twython import Twython
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

con_key = ''
con_key_secret = ''
acc_token = ''
acc_token_secret = ''

twitter = Twython(con_key, con_key_secret, acc_token, acc_token_secret)

analyzer = SentimentIntensityAnalyzer()

max_count = 1939
earlier_tweet_id = 0
tweet_count = 0
tweet_score = {'positive' : 0, 'neutral' : 0, 'negative' : 0}

while max_count > tweet_count:

	tweet_id_list = []

	if earlier_tweet_id <= 0:	
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=100, tweet_mode='extended', exclude_replies='true')
	else:
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=100, max_id=earlier_tweet_id - 1, tweet_mode='extended', exclude_replies='true')

	for tweet in tweets:
		tweet_count += 1
		tweet_id_list.append(tweet['id'])

		#finding and storing sentimental score for each tweet text
		score = analyzer.polarity_scores(tweet['full_text'])

		#calulating sentiment
		#print score['compound']
		if score['compound'] >= 0.5:
			tweet_score['positive'] += 1
		elif score['compound'] > -0.5 and score['compound'] < 0.5:
			tweet_score['neutral'] += 1
		elif score['compound'] <= -0.5:
			tweet_score['negative'] += 1

	if(len(tweets)):
		earlier_tweet_id = sorted(tweet_id_list)[0]
	else: 
		tweet_count=max_count


pos_frac = float(tweet_score['positive'] / (tweet_score['negative'] + tweet_score['neutral']))
neu_frac = float(tweet_score['neutral'] / (tweet_score['positive'] + tweet_score['negative']))
neg_frac = float(tweet_score['negative'] / (tweet_score['neutral'] + tweet_score['positive'])) 
 
print 'Positive sentiment=', pos_frac
print 'Neutral sentiment=', neu_frac
print 'Negative sentiment=', neg_frac
	
#print score of each tweet
# for t, s in tweet_score.iteritems():
# 	print t, s


