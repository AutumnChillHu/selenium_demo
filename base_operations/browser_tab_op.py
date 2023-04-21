# -*- coding: utf-8 -*-


def browser_tab_operation(driver):
    # url
    print(driver.current_url)
    # 标签tab展示的文字
    print(driver.title)
    # 关闭当前窗口
    driver.close()
    # 后一个页面
    driver.back()
    # 前一个页面
    driver.forward()
    # 刷新页面
    driver.refresh()
