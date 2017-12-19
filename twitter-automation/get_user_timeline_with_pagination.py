from twython import Twython
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
from nltk import ngrams




con_key = ''
con_key_secret = ''
acc_token = ''
acc_token_secret = ''

stopwords_english = stopwords.words("english")
stemmer = PorterStemmer()

twitter = Twython(con_key, con_key_secret, acc_token, acc_token_secret)

max_count = 1900
earlier_tweet_id = 0
tweet_count = 0
bigrams = []

while max_count > tweet_count:

	tweet_id_list = []

	if earlier_tweet_id <= 0:	
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=200, tweet_mode='extended', exclude_replies='true')
	else:
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=200, max_id=earlier_tweet_id - 1, tweet_mode='extended', exclude_replies='true')

	for tweet in tweets:
		noise_reduced_token = []

		tweet_count += 1
		#print tweet['full_text']
		tweet_id_list.append(tweet['id'])
		
		tweet_text_tokens = word_tokenize(tweet['full_text'].lower())
		for token in tweet_text_tokens:
			if len(token) > 3 and token not in stopwords_english:
				stemmed_tokens = stemmer.stem(token)
				if stemmed_tokens != 'http':
					noise_reduced_token.append(stemmed_tokens)

		bigrams += list(ngrams(noise_reduced_token,2))


	if(len(tweets)):
		earlier_tweet_id = sorted(tweet_id_list)[0]
	else: tweet_count=max_count
	
freq = Counter(bigrams)
	#print tweets[0]
for token, count in freq.most_common(10):
	print token, count

