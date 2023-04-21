# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def start(url="https://www.baidu.com/"):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(100)
    element = driver.find_element(By.ID, "extensionId")
    alert = driver.switch_to.alert  # 通过switch_to.alert切换到alert
    alert.accept()  # 等同于点击“确认”或“OK”
    alert.dismiss()  # 等同于点击“取消”或“Cancel”
    alert.send_keys("发送文本")  # 发送文本，对有提交需求的prompt框（上图3）
    alert.text  # 获取alert文本内容，对有信息显示的alert框










if __name__ == "__main__":
    url = "https://www.cnblogs.com/haifeima/p/10209383.html"
    start(url)
