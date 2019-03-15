import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.crm_homepage import CrmHomePage
from logs.logger import Logger

class CrmSearch(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)  # 读取浏览器类型

    def tearDown(self):
        self.driver.quit()

    def test_case1(self):
        homepage = CrmHomePage(self.driver)
        homepage.login("heshuiming@pxjy.com","heshuiming@123") #调用方法，传入用户名和密码
        homepage.login_btn() #调用方法，点击登录按钮
        time.sleep(2)

        homepage.skip_crm() #进入crm
        time.sleep(2)
        #窗口切换
        search_window = self.driver.current_window_handle
        time.sleep(2)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != search_window:
                self.driver.switch_to.window(handle)
                time.sleep(2)
        #点击我的学员
        homepage.alreadyStudent()

    def test_case2(self):
        homepage = CrmHomePage(self.driver)
        homepage.login("heshuiming@pxjy.com","heshuiming@123") #调用方法，传入用户名和密码,登录并跳转至青龙系统
        # homepage.login_btn() #调用方法，点击登录按钮
        # time.sleep(5)
        #
        # homepage.skip_crm() #进入crm
        # time.sleep(2)
        # #窗口切换
        # search_window = self.driver.current_window_handle
        # time.sleep(2)
        # all_handles = self.driver.window_handles
        # for handle in all_handles:
        #     if handle != search_window:
        #         self.driver.switch_to.window(handle)
        #         time.sleep(2)
        # #点击我的学员
        homepage.AllResourceInMarket()
        # self.assertTrue(self.driver.find_element_by_xpath("//h1[@class='page-header']"))
        time.sleep(5)

if __name__== '__main__':
    unittest.main()
