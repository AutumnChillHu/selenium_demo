# -*- coding: utf-8 -*-


def handle_operation(driver):
    # 获取当前窗口
    current_handle = driver.current_window_handle
    # 获取所有窗口
    all_handles = driver.window_handles
    # 切换窗口
    driver.switch_to.window(all_handles[-1])
    # 打开新窗口。
    driver.execute_script("window.open();")
