# https://github.com/alexmercerind/youtube-search-python
#Sync
# pip install youtube-search-python

import pandas as pd
from youtubesearchpython import VideosSearch
import json

#------------------------------------------------------------
def my_youtube_search(search_str='이누야샤', nrows=7) :
	videosSearch = VideosSearch(search_str, limit=nrows)
	json_res = videosSearch.result()

	#print(videosSearch.result())  ## [{},{},{}]
	#print(json.dumps(videosSearch.result(), sort_keys=True, indent=4))

	movie_list = json_res['result']
	print(json.dumps(movie_list, sort_keys=True, indent=4))

	tot_list = []
	for movie in movie_list:
		dict = {}
		# print(movie['thumbnails'][0]['url'])
		# print(movie['link'])
		# print(movie['title'])
		dict["title"] 	 = movie['title']
		try :
			dict["movie"] = movie['richThumbnail']['url']
		except :
			dict["movie"] = movie['thumbnails'][0]['url']

		dict["img"] 	 = movie['thumbnails'][0]['url']
		dict["duration"] = movie['duration']
		dict["url"] 	 = movie['link']
		dict["rdate"] 	 = movie['publishedTime']
		dict["cnt"]  = movie['viewCount']['text']
		tot_list.append(dict)
	return tot_list  #[{},{}]

tot_list = my_youtube_search('중구 명동', 1)
df = pd.DataFrame(tot_list)
# print(df.img)
# print(df.info())

