#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   run.py
@Time    :   2021/12/15 10:32:57
@Author  :   LittleMu 
@Contact :   hunt_hak@outlook.com
@License :   (C)Copyright 2020-2021, WangShuai
'''


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests


class NetAutoLink:
    def __init__(self, url='http://10.10.43.3/', username='', passwd='') -> None:
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        # self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='')
        self.url = url
        self.username = username
        self.passwd = passwd

    def send_message(self):
        self.browser.get(self.url)
        try:
            logout_btn = WebDriverWait(self.browser, 3, 0.5).until(
                EC.presence_of_element_located((By.XPATH, '//form[@name="f1"]/input[@name="logout"]'))
            )
            if logout_btn:
                self.browser.close()
                return True
        except:
            pass

        try:
            username_btn = WebDriverWait(self.browser, 3, 0.5).until(
                EC.presence_of_element_located((By.XPATH, '//form[@name="f1"]/input[@name="DDDDD"]'))
            )
            username_btn.send_keys(self.username)

            passwd_btn = WebDriverWait(self.browser, 3, 0.5).until(
                EC.presence_of_element_located((By.XPATH, '//form[@name="f1"]/input[@name="upass"]'))
            )
            passwd_btn.send_keys(self.passwd)

            click_btn = WebDriverWait(self.browser, 1, 0.5).until(
                EC.presence_of_element_located((By.XPATH, '//form[@name="f1"]/input[@name="0MKKey"]'))
            )
            click_btn.click()
        except:
            self.browser.close()
            return False
        if self.browser:
            self.browser.close()
        return True


def test_net(username, passwd, times=10):
    for i in range(times):
        spider = NetAutoLink(username=username, passwd=passwd)
        flag = spider.send_message()
        if flag:
            break
    print(flag)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    res = requests.get('https://www.baidu.com/', headers=headers)   # 请求一次百度判断连接是否成功
    if res.status_code == 200:
        print('Net Linked!') 
    else:
        print('Sending Message Failed!')


if __name__ == "__main__":
    username = ''
    passwd = ''
    # 默认重复请求10次
    test_net(username, passwd, 10)
    
