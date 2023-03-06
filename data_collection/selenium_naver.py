# pip install selenium
# download chrome driver

import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys


def mysearch(search_word="제주관광지") :
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
	driver.get("https://travel.naver.com/domestic/14/guide/tour?limit=12")

	#---------------------------------------------- 스크롤 다운
	endkey = 4  # 스크롤 다운 시 12개목록씩 추가  -- 총 12*4=48개
	while endkey:
		# driver.find_element_by_tag_name('body').send_keys(Keys.END)
		#ele_path = driver.find_element(By.CSS_SELECTOR, "# __next > div > div.mainContainer_container__1GEbx > div > div > main > div:nth-child(2) > div.guide_GuidePanel__3S6xd > div > div > button")
		ele_path = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/main/div[2]/div[2]/div/div/button')
		## click button
		driver.execute_script("arguments[0].click();", ele_path);
		time.sleep(2)
		endkey -= 1
	#---------------------------------------------- lxml
	# soup = BeautifulSoup(htmlstr, 'lxml')
	# video_list0 = soup.find('div', {'id': 'contents'})
	# print(video_list0)
	#---------------------------------------------- html.parser
	htmlstr = driver.page_source
	soup = BeautifulSoup(htmlstr, features="html.parser")
	"#__next > div > div.mainContainer_container__1GEbx > div > div > main > div:nth-child(2) > div.guide_GuidePanel__3S6xd > div > ul > li:nth-child(1)"
	div_list = soup.select("div#__next > div > div.mainContainer_container__1GEbx > div > div > main > div:nth-child(2) > div.guide_GuidePanel__3S6xd > div > ul > li")
	#----------------------------------------------

	movie_list = []
	for div in div_list:
		url     = div.select_one("div > a").get('href')
		title   = div.select_one("div > a > b").text
		img = div.select_one("div > a > figure > img").get('src')
		print(title, url, img)
		movie_list.append([title, url, img])

	print(len(movie_list))
	df = pd.DataFrame(movie_list, columns=["title","url","img"])
	print(df.head())
	print(df.info())
	df.to_csv("youtebe_sel_res.csv", index=False)
	return movie_list

mysearch(search_word="제주관광지")