import allure
import pytest


class Test01:
    @allure.step("新增步骤被执行")
    def test01(self):
        allure.attach("","")
        print("test01被执行")
    # @allure.serivritpyte
    def test02(self):
        print("test02被执行")