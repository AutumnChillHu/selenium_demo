# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def start(url="https://www.baidu.com/"):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(100)
    element = driver.find_element(By.ID, "extensionId")
    element.get










if __name__ == "__main__":
    url = "https://www.cnblogs.com/haifeima/p/10209383.html"
    start(url)
