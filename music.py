from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlretrieve

song_name = input('input song name:')
url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(song_name)
outer_url = 'http://music.163.com/song/media/outer/url?id='
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.switch_to.frame('g_iframe')
req = driver.find_element_by_id('m-search')
song_id_list_req = req.find_element_by_xpath('//div[@class="srchsongst"]/div/div[2]/div/div/a')
song_id = song_id_list_req.get_attribute('href').split('=')[1]
urlretrieve(outer_url+song_id+'.mp3', 'songs/{}.mp3'.format(song_name))
# print(song_id)
