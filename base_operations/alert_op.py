# -*- coding: utf-8 -*-

def by_Alert(driver):
    alert = driver.switch_to.alert  # 通过switch_to.alert切换到alert
    alert.accept()  # 等同于点击“确认”或“OK”
    alert.dismiss()  # 等同于点击“取消”或“Cancel”
    alert.send_keys("发送文本")  # 发送文本，对有提交需求的prompt框（上图3）
    print(alert.text)


def by_ActiveElement(driver):
    # 返回当前焦点的对象。
    ele = driver.switch_to.active_element
    ele.clilk()
