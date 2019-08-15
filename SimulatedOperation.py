#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
写于 2019-8-15 后续如果网页有更新可能就不能用了
原网页
https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=python3
通过模拟操作的方式来执行代码并获取返回
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


def run_py3_code(code):
    driver = webdriver.Chrome('C:\\MyProgram\\chromedriver.exe')
    driver.get('https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=python3')

    # 等待加载
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector('div.CodeMirror'))
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector('#submitBTN'))

    # 模拟人工操作过程
    code_input = driver.find_element_by_css_selector('div.CodeMirror')
    code_input.click()
    input_area = driver.execute_script('return document.activeElement')
    input_area.send_keys(Keys.CONTROL, 'a')
    input_area.send_keys(Keys.BACKSPACE)
    input_area.send_keys(code)
    run_btn = driver.find_element_by_css_selector('#submitBTN')
    run_btn.click()

    # 等待结果
    time.sleep(3)  # 给JS那边一点反应时间，让他把上一次执行的结果删除掉
    res_frame = driver.find_element_by_css_selector("#iframeResult")
    driver.switch_to.frame(res_frame)
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('/html/body/pre'))
    run_result = driver.find_element_by_xpath('/html/body/pre')
    res_str = None
    if run_result is not None:
        res_str = run_result.text
    driver.close()
    return res_str


if __name__ == '__main__':
    code = '#!/usr/bin/python3\nprint("Hello, World")\nprint("\\n\\nlueluelue")'
    res = run_py3_code(code)
    print('response:\n' + res)
