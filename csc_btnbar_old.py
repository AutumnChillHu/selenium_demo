# -*- coding: utf-8 -*-
"""
客服中心 buttonbar跳转
1.不同角色btnlist 展示不同
2.不同角色 相同按钮 跳转不同
"""

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By

role_btn_map = {"CS1": ["用户画像", "查看密码"]}
btn_urls = {"用户画像": "http://ai.vipkid.com.cn/lab/dist/index.html#/serverUser?id=329",
            "查看密码": "https://csc.vipkid.com.cn/searchCode"}


def main():
    # 1.实例化浏览器
    browser = webdriver.Chrome()
    # 2.打开网页
    browser.get(
        "https://sso.vipkid.com.cn/user/login?redirect_url=https%3A%2F%2Fcsc.vipkid.com.cn%2Fcall%2FpopWindow%3FstudentId%3D329")
    # 3.登录：查找元素并输入
    browser.find_element_by_xpath(
        "/html/body/div/div[2]/div/div/div[1]/div[2]/div/div/form/div[1]/div/div/input").send_keys("huxiajie")
    browser.find_element_by_xpath(
        "/html/body/div/div[2]/div/div/div[1]/div[2]/div/div/form/div[2]/div/div/input").send_keys("Jessie36Fall")
    browser.find_element_by_xpath("//*[@id='btn']").click()
    # 4.关闭弹窗+显示等待
    # 传递一个locator
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div[3]/button[1]")))
    browser.find_element_by_xpath("/html/body/div[6]/div/div[3]/button[1]").click()
    # 5.找到btn_bar
    btns = browser.find_element_by_xpath(
        "//*[@id=\"app\"]/div/div[3]/section/div/div[1]/div/div/div[1]/div[2]").find_elements_by_tag_name("dl")
    # todo 比较下总数 # 因为涉及页面的刷新，所以不能遍历元素，要实时获取
    for i in range(len(role_btn_map["CS1"])):
        btn = browser.find_element_by_xpath(
            "//*[@id=\"app\"]/div/div[3]/section/div/div[1]/div/div/div[1]/div[2]/dl[{}]".format(i + 1))
        # 根据按钮名称判断该按钮是否应该存在
        btn_name = btn.text
        if btn_name not in role_btn_map["CS1"]:
            print("ERROR!该按钮不应该存在")
            continue
        btn.click()
        # 6.判断句柄,分新窗口/新tab页两种情况
        # 窗口的唯一标志是句柄
        handles = browser.window_handles
        if len(handles) > 1:
            browser.switch_to.window(handles[-1])
            if browser.current_url != btn_urls[btn_name]:
                print("ERROR!url不符合预期", browser.current_url, btn_urls[btn_name])
                continue
                browser.close()
                browser.switch_to.window(handles[0])
            else:
                time.sleep(2)
        if browser.current_url != btn_urls[btn_name]:
            print("ERROR!url不符合预期", browser.current_url, btn_urls[btn_name])
            continue
            browser.back()
            # 关闭浏览器、退出驱动
            browser.quit()


if __name__ == "__main__":
    pass
