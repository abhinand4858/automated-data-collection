from twython import Twython
from highcharts import Highchart

chart = Highchart()
options = {
	'chart': {'type': 'line'},
	'title': {'text': 'Tweets Timeline'},
	'legend': {'enabled':True},
	'xAxis': {
		'categories': ['Jan-Jun09','Jul-Dec09','Jan-Jun10','Jul-Dec10','Jan-Jun11','Jul-Dec11','Jan-Jun12','Jul-Dec12','Jan-Jun13','Jul-Dec13','Jan-Jun14','Jul-Dec14','Jan-Jun15','Jul-Dec15','Jan-Jun16','Jul-Dec16','Jan-Jun17','Jul-Dec17',]
	},
	'yAxis':{
			'title': {'text': 'Number of tweets'}
	},
}



con_key = ''
con_key_secret = ''
acc_token = ''
acc_token_secret = ''

twitter = Twython(con_key, con_key_secret, acc_token, acc_token_secret)

max_count = 1930
earlier_tweet_id = 0
tweet_count = 0

y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18 = [0 for i in range(0,18)]  

while max_count > tweet_count:

	tweet_id_list = []

	if earlier_tweet_id <= 0:	
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=100, tweet_mode='extended', exclude_replies='true')
	else:
		tweets = twitter.get_user_timeline(screen_name='ponguru', count=100, max_id=earlier_tweet_id - 1, tweet_mode='extended', exclude_replies='true')

	for tweet in tweets:
		noise_reduced_token = []

		tweet_count += 1
		#print tweet['full_text']
		tweet_id_list.append(tweet['id'])

		if tweet['created_at'][-4:] == '2009':
			if 'Jan' in tweet['created_at'] or 'Feb' in tweet['created_at'] or 'Mar' in tweet['created_at'] or 'Apr' in tweet['created_at'] or 'May' in tweet['created_at'] or 'Jun' in tweet['created_at']:
				y1+=1
			elif 'Jul' in tweet['created_at'] or 'Aug' in tweet['created_at'] or 'Sept' in tweet['created_at'] or 'Oct' in tweet['created_at'] or 'Nov' in tweet['created_at'] or 'Dec' in tweet['created_at']:
				y2+=1

		elif tweet['created_at'][-4:] == '2010':
			if 'Jan' in tweet['created_at'] or 'Feb' in tweet['created_at'] or 'Mar' in tweet['created_at'] or 'Apr' in tweet['created_at'] or 'May' in tweet['created_at'] or 'Jun' in tweet['created_at']:
				y3+=1
			elif 'Jul' in tweet['created_at'] or 'Aug' in tweet['created_at'] or 'Sept' in tweet['created_at'] or 'Oct' in tweet['created_at'] or 'Nov' in tweet['created_at'] or 'Dec' in tweet['created_at']:
				y4+=1
		elif tweet['created_at'][-4:] == '2011':
			if 'Jan' in tweet['created_at'] or 'Feb' in tweet['created_at'] or 'Mar' in tweet['created_at'] or 'Apr' in tweet['created_at'] or 'May' in tweet['created_at'] or 'Jun' in tweet['created_at']:
				y5+=1
			elif 'Jul' in tweet['created_at'] or 'Aug' in tweet['created_at'] or 'Sept' in tweet['created_at'] or 'Oct' in tweet['created_at'] or 'Nov' in tweet['created_at'] or 'Dec' in tweet['created_at']:
				y6+=1
		elif tweet['created_at'][-4:] == '2012':
			if 'Jan' in tweet['created_at'] or 'Feb' in tweet['created_at'] or 'Mar' in tweet['created_at'] or 'Apr' in tweet['created_at'] or 'May' in tweet['created_at'] or 'Jun' in tweet['created_at']:
				y7+=1
			elif 'Jul' in tweet['created_at'] or 'Aug' in tweet['created_at'] or 'Sept' in tweet['created_at'] or 'Oct' in tweet['created_at'] or 'Nov' in tweet['created_at'] or 'Dec' in tweet['created_at']:
				y8+=1
		elif tweet['created_at'][-4:] == '2013':
			if 'Jan' in tweet['created_at'] or 'Feb' in tweet['created_at'] or 'Mar' in tweet['created_at'] or 'Apr' in tweet['created_at'] or 'May' in tweet['created_at'] or 'Jun' in tweet['created_at']:
				y9+=1
			elif 'Jul' in tweet['created_at'] or 'Aug' in tweet['created_at'] or 'Sept' in tweet['created_at'] or 'Oct' in tweet['created_at'] or 'Nov' in tweet['created_at'] or 'Dec' in tweet['created_at']:
				y10+=1
		elif tweet['created_at'][-4:] == '2014':
			if 'Jan' in tweet['created_at'] or 'Feb' in tweet['created_at'] or 'Mar' in tweet['created_at'] or 'Apr' in tweet['created_at'] or 'May' in tweet['created_at'] or 'Jun' in tweet['created_at']:
				y11+=1
			elif 'Jul' in tweet['created_at'] or 'Aug' in tweet['created_at'] or 'Sept' in tweet['created_at'] or 'Oct' in tweet['created_at'] or 'Nov' in tweet['created_at'] or 'Dec' in tweet['created_at']:
				y12+=1
		elif tweet['created_at'][-4:] == '2015':
			if 'Jan' in tweet['created_at'] or 'Feb' in tweet['created_at'] or 'Mar' in tweet['created_at'] or 'Apr' in tweet['created_at'] or 'May' in tweet['created_at'] or 'Jun' in tweet['created_at']:
				y13+=1
			elif 'Jul' in tweet['created_at'] or 'Aug' in tweet['created_at'] or 'Sept' in tweet['created_at'] or 'Oct' in tweet['created_at'] or 'Nov' in tweet['created_at'] or 'Dec' in tweet['created_at']:
				y14+=1
		elif tweet['created_at'][-4:] == '2016':
			if 'Jan' in tweet['created_at'] or 'Feb' in tweet['created_at'] or 'Mar' in tweet['created_at'] or 'Apr' in tweet['created_at'] or 'May' in tweet['created_at'] or 'Jun' in tweet['created_at']:
				y15+=1
			elif 'Jul' in tweet['created_at'] or 'Aug' in tweet['created_at'] or 'Sept' in tweet['created_at'] or 'Oct' in tweet['created_at'] or 'Nov' in tweet['created_at'] or 'Dec' in tweet['created_at']:
				y16+=1
		elif tweet['created_at'][-4:] == '2017':
			if 'Jan' in tweet['created_at'] or 'Feb' in tweet['created_at'] or 'Mar' in tweet['created_at'] or 'Apr' in tweet['created_at'] or 'May' in tweet['created_at'] or 'Jun' in tweet['created_at']:
				y17+=1
			elif 'Jul' in tweet['created_at'] or 'Aug' in tweet['created_at'] or 'Sept' in tweet['created_at'] or 'Oct' in tweet['created_at'] or 'Nov' in tweet['created_at'] or 'Dec' in tweet['created_at']:
				y18+=1

	if(len(tweets)):
		earlier_tweet_id = sorted(tweet_id_list)[0]
	else: tweet_count=max_count

g_data = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18]
chart.set_dict_options(options)
chart.add_data_set(g_data,'line', 'PK')
chart.save_file('./highcharts')