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

client = MongoClient()
client = MongoClient('mongodb://eevibe:tjdals2@52.78.192.23', 27017)
db = client.dbsparta

driver = webdriver.Chrome('/Users/eevibe/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://instagram.com')
driver.find_element_by_name('username').send_keys('gaebalzar')
driver.find_element_by_name('password').send_keys('tjdals2')
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()


driver.get('https://www.instagram.com/explore/tags/2020plur/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('#react-root > section > main > article > div.EZdmt > div > div > div > div.v1Nh3.kIKUG._bz0w > a > div > div.KL4Bh > img')

db.photos.drop()

for post in posts:

    alt = post.get('alt')
    src = post.get('src')
    size = post.get('sizes')

    photo = {
        'post_alt': alt,
        'post_size' : size,
        'post_url': src
    }
    
    
    db.photos.insert(photo)