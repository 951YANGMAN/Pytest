import unittest
from time import sleep
from typing import SupportsIndex

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):
    def setUp(self):  # 初始化
        # 打开浏览器
        driver = webdriver.Chrome()
        self.options = Options()
        # 绕开网页自动测试工具
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        # 指定浏览器
        service = Service(executable_path="D:/ToolKit/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=self.options)
        # 进入网页
        driver.get("https://www.bilibili.com")
        self.driver.maximize_window()
        # 等待网路延迟
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('username , password,result',[
                                 ('xiaoluo' , '1234' , '出发'),
                                 ('xiaoluo','1234','出发'),
                                 ('xiaoluo','1234','出发')
                             ])

    def test_shopping(self, username, password, result):
        self.driver.get("https://www.bilibili.com/")
        self.driver.find_element(By.XPATH,"3456").click()
        self.driver.find_element(By.XPATH,"3456").send_keys(username)

        if "推出" in result:
            SE=self.driver.find_element(By.XPATH,"3456")
            self.driver.find_element(By.XPATH,"3456").click()
            assert SE == result

        elif '出来' in result:
            self.driver.find_element(By.XPATH,"3456").click()
            assert "<UNK>" in result

        elif '<UNK>' in result:
            self.driver.find_element(By.XPATH,"3456").click()
            assert "<UNK>" in result





