# -*- coding: UTF-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#路径设置与参数设置
path = '/home/error/program/wyy_free_download/1.0/wangyiyun_free'
common_sleep_time = 0.5

#浏览器初始化设置
options=webdriver.ChromeOptions()

#使浏览器同意使用自动化，没有这个浏览器可能检测到机器人且拦截
options.add_experimental_option("excludeSwitches", ['enable-automation'])
selenium_judge = 0
url_error = 'https://music.163.com/#/404'
#读取文件且打开
with open(path,'r') as file:
    webop = webdriver.Chrome(options=options)
    webop.set_window_size(480, 480) #调整窗口大小
    for line in file.readlines(): #读取每行信息，读取出来是字符串
        '''
        文件有两种形式：
            第一种直接是网易云歌曲的id
            第二种是歌曲的网址
        以下是判断那种形式
        '''
        #第一种的判断，舍去无用的即前三十二个字符
        if(line[0]=='h'):
            web = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%(line[33:])
            print('read the file wait to download the music:%s'%(web))
        else :
            web = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%(line)
            print('read the file wait to download the music:%s'%(web))
        
        #打开网址
        webop.get(web)
        sleep(common_sleep_time)
        #判断是否出错（歌曲是否存在）
        if webop.current_url == url_error :
            print(webop.current_url)
            print("this music does not exist")
            continue

        #因为免费下载的网站无法定位到元素因此物理定位，以下是模拟鼠标移动点击
        '''
        需要判断模拟鼠标存在的位置，影响因素：
            1.第一次在左上角（0，0）
            2。第一次点击下载后最低下会弹出下载框，影响坐标
        所以得区分第一次，第二次与第三次及以后
        '''
        if selenium_judge== 0 :
            sleep(common_sleep_time)
            ActionChains(webop).move_by_offset(370,250).click().perform()
            ActionChains(webop).move_by_offset(0,-60).click().perform()
            print('start download %s'%(web))
        else :
            if selenium_judge == 1:
                sleep(common_sleep_time)
                ActionChains(webop).move_by_offset(0,40).click().perform()
                ActionChains(webop).move_by_offset(0,-60).click().perform()
                print('start download %s'%(web))
            else:
                sleep(common_sleep_time)
                ActionChains(webop).move_by_offset(0,60).click().perform()
                ActionChains(webop).move_by_offset(0,-60).click().perform()
                print('start download %s'%(web))
        sleep(common_sleep_time)
        selenium_judge+=1
        #selenium_error用于判断是否是第一次下载与判断鼠标位置
    sleep(common_sleep_time)
    print('download all ')
    #关闭文件及浏览器
    file.close()
    webop.close()


