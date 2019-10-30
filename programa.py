# -*- coding: UTF-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from time import sleep
import os

path = '/home/error/wangyiyun_free'
common_sleep_time = 0.8

options=webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
selenium_error = 0
with open(path,'r') as file:
    webop = webdriver.Chrome(options=options)
    webop.maximize_window()
    for line in file.readlines():
        if(line[0]=='h'):
            web = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%(line[33:])
            print('read the file wait to download the music:%s'%(web))
        else :
            web = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%(line)
            print('read the file wait to download the music:%s'%(web))
        webop.get(web)
        if selenium_error==0 :
            sleep(common_sleep_time)
            ActionChains(webop).move_by_offset(1038,515).click().perform()
            sleep(common_sleep_time)
            ActionChains(webop).move_by_offset(0,0).click().perform()
            print('start download %s'%(web))
        else :
            sleep(common_sleep_time)
            ActionChains(webop).click().perform()
            sleep(common_sleep_time)
            ActionChains(webop).click().perform()
            print('start download %s'%(web))
        sleep(common_sleep_time)
        selenium_error+=1
    sleep(common_sleep_time)
    print('download all ')
    file.close()
    webop.close()