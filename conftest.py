# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
#
# # 定义一个 类级别
# @pytest.fixture(scope='class')
# def login():  # 初始化
#     # 打开浏览器
#     driver = webdriver.Chrome()
#     options = Options()
#
#     # 绕开网页自动测试工具
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     # 指定浏览器
#     service = Service(executable_path="D:/ToolKit/chromedriver-win64/chromedriver-win64/chromedriver.exe")
#     driver = webdriver.Chrome(service=service, options=options)
#     # 等待网路延迟
#     driver.implicitly_wait(5)
#     # 进入网页
#     driver.get("https://www.bilibili.com")
#     driver.maximize_window()
#
#     # yield 相当于返回
#     yield driver
#     driver.quit()