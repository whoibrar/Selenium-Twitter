# selinium twitter like main file

import os
from credentials import *
from time import sleep
from selenium import webdriver
from selenium import common


# Variables
post_to_like = 5 #no of posts to like on each iteration
wait_like = 1.5 #seconds to wait before liking next post
user = "whoibrar" #twitter username to like posts of
wait_pageload = 3 #seconds to wait for page to load
list_link = "https://twitter.com/i/lists/1376140126904934406" #link to the twitter list 
chromedriver = "D:/archive/setup/chromedriver_win32/chromedriver.exe" #path to the chromedriver
hastag='devsnest' #hastag to search


# setting up
os.environ["webdriver.chrome.driver"]=chromedriver
driver = webdriver.Chrome(chromedriver)

def login():
    driver.get("https://twitter.com/login")
    sleep(wait_pageload)
    driver.find_element_by_name("session[username_or_email]").send_keys(user_id)
    driver.find_element_by_name("session[password]").send_keys(user_pass)
    driver.find_element_by_css_selector(".r-jwli3a").click()
    sleep(wait_pageload)

def logout():
    driver.get("https://twitter.com/logout")
    sleep(wait_pageload)
    driver.find_element_by_xpath("//div[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]").click()
    sleep(wait_pageload)

def like_user_posts():
    driver.get("https://twitter.com/"+user)
    sleep(wait_pageload)

    for i in range(post_to_like):
        driver.find_element_by_xpath("//div[@data-testid='like']").click()
        sleep(wait_like)

def like_a_list():
    driver.get(list_link)
    sleep(wait_pageload)

    for i in range(post_to_like):
        driver.find_element_by_xpath("//div[@data-testid='like']").click()
        sleep(wait_like)

def like_by_hastag():
    driver.get("https://twitter.com/search?q=%23" + str(hastag))
    sleep(wait_pageload)

    for i in range(post_to_like):
        driver.find_element_by_xpath("//div[@data-testid='like']").click()
        sleep(wait_like)

def like_homepage():
    for i in range(post_to_like):
        driver.find_element_by_xpath("//div[@data-testid='like']").click()
        sleep(wait_like)

login()
like_user_posts()
like_a_list()
like_by_hastag()
like_homepage()
logout()
