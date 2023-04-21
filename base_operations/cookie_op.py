# -*- coding: utf-8 -*-


def cookie_op(driver):
    # 获取所有cookie
    cookies = driver.get_cookies()
    # 获取某个cookie
    token = driver.get_cookie("cookieName")["value"]
    # set cookie至driver
    cookie_dict = {"token": token}
    driver.add_cookie(cookie_dict)
