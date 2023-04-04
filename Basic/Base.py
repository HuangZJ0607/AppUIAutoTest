from selenium.webdriver.common.by import By

from Basic.Log import Logger
from selenium.webdriver.support.ui import WebDriverWait

log = Logger().get_logger()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _format_args(self, agrs, kwargs):
        """解析元素"""
        agrs_list = []
        for ag in agrs:
            if type(ag) is dict:
                kwargs = {**ag, **kwargs}
            else:
                agrs_list.append(ag)
        agrs = tuple(agrs_list)
        return agrs, kwargs

    def find_element(self, *agrs, **kwargs):
        """封装查找元素函数"""
        timeout = 10
        poll = 1.0
        agrs, kwargs = self._format_args(agrs, kwargs)
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(*agrs, **kwargs))

    def click(self, *agrs, **kwargs):
        """封装点击操作函数"""
        self.find_element(*agrs, **kwargs).click()

    def get_toast_content(self, message):
        """自定义一个获取 toast内容的方法"""
        tmp_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        ele = self.find_element(tmp_feature)
        return ele.text

    def is_toast_exits(self, msg):
        """用传参来的msg去判断包含该内容的toast是否存在"""
        try:
            self.get_toast_content(msg)
            return True
        except Exception:
            return False
