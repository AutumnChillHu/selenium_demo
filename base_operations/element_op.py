# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


def find_element_fromDOM_by(driver):
    """在整个DOM Tree中查找元素"""

    '''获取单个元素的常见方式，返回匹配的第一个元素'''
    # 1.最准确：元素的ID在页面中是唯一的，而且一般不会变。
    driver.find_element(By.ID, "extensionId")
    # 2.次准确：元素的name也经常会用来作为标志，但是原则上是允许重复的，所以在chrome中检查一下。
    driver.find_element(By.NAME, "user_name")
    # 3.最常用：Xpath是用来定位XML文档节点的语言。不过HTML可以看成是XML(XHTML)的一种实现。
    #   用chrome获取xpath非常方便。但是页面改动了就需要更新。
    #   经常在[]中加上对name、id属性的筛选来提高准确性。
    driver.find_element(By.XPATH, "//*[@id='rso']/div[2]/div/div/div[1]/div/a")
    # 4.定位超链接
    driver.find_element(By.LINK_TEXT, "Continue")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Conti")  # 子串匹配
    # 其他不太常用的
    driver.find_element(By.TAG_NAME, "div")
    driver.find_element(By.CLASS_NAME, 'content')
    driver.find_element(By.CSS_SELECTOR, "#\\31  > div > div:nth-child(1) > h3")

    '''获取多个元素，加s'''
    elements = driver.find_elements(By.NAME, "extensionId")
    for ele in elements:
        # 不符合断言会报错AssertionError
        assert ele.text == "Hello from JavaScript!"


def find_element_fromElement_by(driver):
    """缩小范围查找元素：在确定元素中查找元素"""

    fruits = driver.find_element(By.ID, "fruits")
    fruit = fruits.find_element(By.CLASS_NAME, "tomatoes")


def element_operation(element):
    """元素常见操作"""

    element.click()
    # 模拟输入
    element.send_keys("需要输入的内容")


def element_info(element):
    # 获取元素属性，如name、id
    element.get_property("name")
    # 元素本身的文字显示
    print(element.text)
