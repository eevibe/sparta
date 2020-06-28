import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from flask import Flask, render_template, jsonify, request
import datetime as dt
import os
import zipfile   
import shutil
from selenium.webdriver.support.ui import WebDriverWait
from pymongo import MongoClient
from jsonify import convert

client = MongoClient()
# client = MongoClient('mongodb://eevibe:tjdals2@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta



app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index5.html')




# 인스타그램 자동 로그인하기
# driver = webdriver.Chrome('/Users/eevibe/Downloads/chromedriver')
# driver.implicitly_wait(3)
# driver.get('https://instagram.com')
# driver.find_element_by_name('username').send_keys('eevibe')
# driver.find_element_by_name('password').send_keys('tjdals2')
# driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
# driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()


# driver.get('https://www.instagram.com/explore/tags/cybeerfeestival/')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# posts = soup.select('#react-root > section > main > article > div.EZdmt > div > div > div > div.v1Nh3.kIKUG._bz0w > a > div > div.KL4Bh > img')

# for post in posts:
    
#     alt = post.get('alt')
#     src = post.get('src')
#     size = post.get('sizes')

#     photo = {
#         'post_alt': alt,
#         'post_size' : size,
#         'post_url': src
#     }
       
#     db.photos.insert(photo)

    # return jsonify({'result': 'success'})

@app.route('/api/hashtag', methods=['GET'])
def hashtag_list():
    photos = list(db.photos.find({},{'_id':False}))
    # print(photos)
    return jsonify({'result':'success', 'photos': photos})



# @app.route('/')
# def hashtag():
#     photos = list(db.photos.find({},{'_id':False}))
#     return jsonify({'result':'success', 'photos': photos})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)








    


# url = 'https://www.instagram.com/explore/tags/cybeerfeestival'
# driver.get(url)
# sleep(5)

# for img in imgs:
#     req = Request(url, headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'})
#     webpage = urlopen(req).read()
#     soup = BeautifulSoup(data.text, 'html.parser')

#     imgs = soup.find_all("img", attrs = {"class" : "FFVAD"})
#     imgs_url = imgs

    







# 타겟 URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.instagram.com/explore/tags/cybeerfeestival/',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.




#############################
# (입맛에 맞게 코딩)
#############################