# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def expected_conditions_explain(driver):
    locator = (By.ID, 'CSDN')
    element = driver.find_element(By.ID, "extensionId")
    WebDriverWait(driver, timeout=50, poll_frequency=0.5, ignored_exceptions=[TypeError, IndexError]).until(
        EC.presence_of_element_located(locator))

    # 判断元素是否出现
    EC.presence_of_element_located(locator)
    EC.presence_of_all_elements_located(locator)

    # 判断元素是否可点击
    EC.element_to_be_clickable(locator)

    # 验证元素是否可见。 1 2 等同。
    EC.visibility_of(element)
    EC.visibility_of_element_located(locator)
    EC.invisibility_of_element_located(locator)

    # 判断是否出现alert
    EC.alert_is_present()

    # 判断text是否出现在element.text中、是否出现在element.value中。
    EC.text_to_be_present_in_element(locator, "text")
    EC.text_to_be_present_in_element_value(locator, "text")

    # 判断元素是否被选中
    EC.element_to_be_selected(element)
    EC.element_located_to_be_selected(locator)
    # 判断元素element.is_selected()的状态
    EC.element_selection_state_to_be(element, False)
    EC.element_located_selection_state_to_be(locator, False)

    # 判断元素是否在DOM中，可以判断页面是否刷新了
    EC.staleness_of(element)

    # 验证driver.title
    EC.title_is("title_name")
    EC.title_contains("title_name")

    # 判断frame是否可切入
    EC.frame_to_be_available_and_switch_to_it(locator)
