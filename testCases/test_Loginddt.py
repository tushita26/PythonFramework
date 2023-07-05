import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.logger.info("********************Test_002_DDT_Login*************************")
        self.logger.info("********************Verifying Login DDT test*************************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginPage = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("No of Rows in excel", self.rows)
        lst_status = []  # empty list variable

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
            self.loginPage.setUserName(self.user)
            self.loginPage.setPassword(self.password)
            self.loginPage.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***Passed****")
                    self.loginPage.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed****")
                    self.loginPage.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***Failed****")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Passed****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***********Login DDT Test passed********88")
            self.driver.close()
            assert True
        else:
            self.logger.info("***********Login DDT Test failed********88")
            self.driver.close()
            assert False

        self.logger.info("***********End of Login DDT Test********88")
        self.logger.info("***********Completed Test_002_DDT_Login********88")
