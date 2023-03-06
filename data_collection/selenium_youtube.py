# pip install selenium
# download chrome driver

import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys
def mysearch(search_word="지브리 영화") :
	#---------------------------------------------- 크롬 옵션 객체 생성
	# options = webdriver.ChromeOptions()
	# options.add_argument("window-size=1000x800") # 화면크기(전체화면)
	# user_agent = "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36 "
	# options.add_argument('user-agent=' + user_agent)
	# options.add_argument('headless') # headless 모드 설정
	# options.add_argument("disable-gpu")
	# options.add_argument("disable-infobars")
	# options.add_argument("--disable-extensions")
	# options.add_argument("--mute-audio") #mute
	# options.add_argument('--blink-settings=imagesEnabled=false') #브라우저에서 이미지 로딩을 하지 않습니다.
	# options.add_argument('incognito') #시크릿 모드의 브라우저가 실행됩니다.
	# options.add_argument("--start-maximized")
	# driver = webdriver.Chrome('./chromedriver_102.0.5005.27.exe', options=options)

	print("search_word", search_word)
	#---------------------------------------------- 크롬 드라이버 로드  110.0.5481.177
	# https://chromedriver.chromium.org/downloads
	# https://chromedriver.storage.googleapis.com/index.html?path=110.0.5481.77/
	# ----------------------------------------------
	driver = webdriver.Chrome('chromedriver_110.exe')
	driver.get("https://www.youtube.com/results?search_query="+search_word)

	#---------------------------------------------- 스크롤 다운
	endkey = 4  # 스크롤 다운 시 30개목록씩 추가  -- 총 30*4=120개
	while endkey:
		# driver.find_element_by_tag_name('body').send_keys(Keys.END)
		driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

		time.sleep(1.5)
		endkey -= 1

	#---------------------------------------------- lxml
	# soup = BeautifulSoup(htmlstr, 'lxml')
	# video_list0 = soup.find('div', {'id': 'contents'})
	# print(video_list0)
	#---------------------------------------------- html.parser
	htmlstr = driver.page_source
	soup = BeautifulSoup(htmlstr, features="html.parser")
	div_list = soup.select("#contents > ytd-video-renderer")
	#----------------------------------------------

	movie_list = []
	for div in div_list:
		url     = div.select_one("div#dismissible > ytd-thumbnail > a#thumbnail").get('href')
		url     = "https://www.youtube.com" + url
		title   = div.select_one("a#video-title > yt-formatted-string").text
		try:
			rdate   = div.select_one("div#metadata-line > span:nth-child(2)").text
		except:
			rdate  = ""
		cnt_str = div.select_one("div#metadata-line > span:nth-child(1)").text
		cnt_str = cnt_str.replace("조회수 ","")[:-1]

		try :
			img = div.select_one("img#img").get('src')
		except:
			img = "data:image/png;base64,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"
		# if "만" in cnt_str:
		# 	print(cnt_str, float(cnt_str[:-1])*10000, url, img, title)
		# elif "천" in cnt_str:
		# 	print(cnt_str, float(cnt_str[:-1])*1000, url, img, title)
		# else :
		# 	print(cnt_str, url, img, title)
		print(title, cnt_str, url, img, rdate[:-2])
		movie_list.append([url, title, rdate, cnt_str, img])

	print(len(movie_list))
	df = pd.DataFrame(movie_list, columns=["url","title","rdate","cnt_str","img"])
	print(df.head())
	print(df.info())
	df.to_csv("youtebe_sel_res.csv", index=False)
	return movie_list

mysearch(search_word="지브리 영화")