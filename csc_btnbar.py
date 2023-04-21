# -*- coding: utf-8 -*-
import time

from selenium import webdriver


def start(url="https://www.baidu.com/"):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(100)










if __name__ == "__main__":
    url = "https://www.cnblogs.com/haifeima/p/10209383.html"
    start(url)
