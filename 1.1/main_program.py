# -*- coding: UTF-8 -*- 
"""第二版程序，在第一版的逻辑上封装代码"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Wyy_download:
    """
    download 的方法:
        file_path: the path for the file
        download_speed: the speed for each website renew 
    """
    def __init__(self, file_path, download_speed):
        self.path = file_path
        self.sleep_time = download_speed
        self.url_error = 'https://music.163.com/#/404'
        self.selenium_judge = 0
        self.windows_x = 480
        self.windows_y = 480
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ['enable-automation'])

    """
    open():
        open the file and set something for the web
    """
    def open(self):
        self.file =  open(self.path, 'r')
        self.webop = webdriver.Chrome(options = self.options)#.set_window_size(self.windows_x, self.windows_y)
        self.webop.set_window_size(self.windows_x, self.windows_y)

    """
    download():
        start download.
    """
    def download(self):
        self.file =  open(self.path, 'r')
        for line in self.file.readlines():
            sleep(self.sleep_time)
            # print(line)
            if(line[0] == 'h'):
                web = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%(line[33:])
                print('get the url: ',web)
            else:
                web = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%(line)
                print('get the url :',web)
            self.webop.get(web)
            sleep(self.sleep_time)
            if self.webop.current_url == self.url_error :
                print(self.webop.current_url)
                print("this music does not exist")
                continue
            elif(self.selenium_judge == 0):
                sleep(self.sleep_time)
                ActionChains(self.webop).move_by_offset(370,250).click().perform()
                ActionChains(self.webop).move_by_offset(0,-60).click().perform()
                print('start download %s'%(web))
            elif(self.selenium_judge == 1):
                sleep(self.sleep_time)
                ActionChains(self.webop).move_by_offset(0,40).click().perform()
                ActionChains(self.webop).move_by_offset(0,-60).click().perform()
                print('start download %s'%(web))
            else:
                sleep(self.sleep_time)
                ActionChains(self.webop).move_by_offset(0,60).click().perform()
                ActionChains(self.webop).move_by_offset(0,-60).click().perform()
                print('start download %s'%(web))
            self.selenium_judge += 1
        print("download all")

    """
    close_all():
        close all the file and website
    """
    def close_all(self):
        self.file.close()
        self.webop.close()

if __name__ == '__main__' :
    path = '/home/error/program/wyy_free_download/1.0/wangyiyun_free'
    sleep_time = 0.5
    start = Wyy_download(path, sleep_time)
    print(start.path)
    start.open()
    start.download()
    start.close_all()
