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
from selenium.webdriver.common.by import By

urls = {
    "login": "https://sso.vipkid.com.cn/user/login?redirect_url=https%3A%2F%2Fcsc.vipkid.com.cn%2Fcall%2FpopWindow%3FstudentId%3D329", }
xpath = {
    "input_login_username": "/html/body/div/div[2]/div/div/div[1]/div[2]/div/div/form/div[1]/div/div/input",
    "input_login_pwd": "/html/body/div/div[2]/div/div/div[1]/div[2]/div/div/form/div[2]/div/div/input",
    "btn_login": "//*[@id='btn']",
    "btn_closealert_afterlogin": "/html/body/div[6]/div/div[3]/button[1]",
    "dl_btnbar": "//*[@id=\"app\"]/div/div[3]/section/div/div[1]/div/div/div[1]/div[2]",
    "traverse_btnbar": "//*[@id=\"app\"]/div/div[3]/section/div/div[1]/div/div/div[1]/div[2]/dl[{}]",
}

role_btnbar_map = {"CS1": ["用户画像", "查看密码"]}
btn_urls = {"用户画像": "http://ai.vipkid.com.cn/lab/dist/index.html#/serverUser?id=329",
            "查看密码": "https://csc.vipkid.com.cn/searchCode"}


def main():
    driver = webdriver.Chrome()
    driver.get(urls["login"])

    # 登录
    driver.find_element(By.XPATH, xpath["input_login_username"]).send_keys("huxiajie")
    driver.find_element(By.XPATH, xpath["input_login_pwd"]).send_keys("Jessie36Fall")
    driver.find_element(By.XPATH, xpath["btn_login"]).click()

    # 关闭弹窗
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath["btn_closealert_afterlogin"])))
    driver.find_element(By.XPATH, xpath["btn_closealert_afterlogin"]).click()

    # 找到btn_bar
    btn_bar = driver.find_element(By.XPATH, xpath["dl_btnbar"]).find_elements(By.TAG_NAME, "dl")
    # todo 比较下总数 因为涉及页面的刷新，所以不能遍历元素，要实时获取
    for role in role_btnbar_map.keys():
        for index in range(len(role_btnbar_map[role])):
            # 遍历btn_bar
            btn = driver.find_element(By.XPATH, xpath["traverse_btnbar"].format(index + 1))
            # 根据按钮名称判断该按钮是否应该存在
            btn_name = btn.text
            assert btn_name in role_btnbar_map[role], "ERROR!{}角色{}按钮不应该存在".format(role, btn_name)
            btn.click()
            # 判断跳转页面，有可能会打开新窗口
            handles = driver.window_handles
            if len(handles) > 1:
                driver.switch_to.window(handles[-1])
                assert driver.current_url == btn_urls[btn_name], "ERROR!{}角色{}按钮跳转链接{}不符合预期".format(role, btn_name,
                                                                                                    driver.current_url)
                # 关闭当前新窗口
                driver.close()
                driver.switch_to.window(handles[0])
            else:
                assert driver.current_url == btn_urls[btn_name], "ERROR!{}角色{}按钮跳转链接{}不符合预期".format(role, btn_name,
                                                                                                    driver.current_url)
                # 后退到上一页
                driver.back()
    # 退出浏览器。结束。
    driver.quit()
