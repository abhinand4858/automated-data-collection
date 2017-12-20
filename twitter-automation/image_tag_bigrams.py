from twython import Twython
import json, urllib
import os
from nltk import ngrams 
from collections import Counter


con_key = ''
con_key_secret = ''
acc_token = ''
acc_token_secret = ''

twitter = Twython(con_key, con_key_secret, acc_token, acc_token_secret)

max_count = 100
earlier_tweet_id = 0
tweet_count = 0
image_count = 0
image_tags = []

while max_count > tweet_count:

	tweet_id_list = []
	

	if earlier_tweet_id <= 0:	
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=10, tweet_mode='extended', exclude_replies='true')
	else:
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=10, max_id=earlier_tweet_id - 1, tweet_mode='extended', exclude_replies='true')

	for tweet in tweets:
		tweet_count += 1
		tweet_id_list.append(tweet['id'])

		if 'entities' in tweet and 'media' in tweet['entities']:
				if '.png' in  str(tweet['entities']['media'][0]['media_url']):
					
					image_count += 1
					urllib.urlretrieve( tweet['entities']['media'][0]['media_url'], 'image'+str(image_count)+'.png' )
		
					score = os.popen('python /home/before0ne/git/repos/models/tutorials/image/imagenet/classify_image.py --image_file image' + str(image_count) + '.png').read()
				
				elif '.jpg' in  str(tweet['entities']['media'][0]['media_url']):
					
					image_count += 1
					urllib.urlretrieve( tweet['entities']['media'][0]['media_url'], 'image'+str(image_count)+'.jpg' )
					
					score = os.popen('python /home/before0ne/git/repos/models/tutorials/image/imagenet/classify_image.py --image_file image' + str(image_count) + '.jpg').read()
				temp = score.splitlines()

				image_tags += temp[0][:temp[0].find('(')].split(',')


	if(len(tweets)):
		earlier_tweet_id = sorted(tweet_id_list)[0]
	else: 
		tweet_count=max_count

bigrams = list(ngrams(image_tags,2))

freq = Counter(bigrams)

for bi, count in freq.most_common(10):
	print bi, count
#print bigrams
	
#print score of each tweet
# for t, s in tweet_score.iteritems():
# 	print t, s


