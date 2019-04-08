
from baseview.basicview import Basic_fun
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import logging

# desired_caps ={}
# desired_caps["platformName"] ="Android"
#
# # 模拟器设备
# desired_caps["platformVersion"]='4.4.2'
# desired_caps['deviceName']='127.0.0.1:62001'
#
#
# # 皇冠
# desired_caps ['app'] = r'C:\Users\Administrator\Desktop\package\huangguan-release-test.1.9.8.apk'
# desired_caps["appPackage"]='com.huangguan.live'
# desired_caps['appActivity']='com.qiyu.live.activity.StartActivity'
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)


class comm_fun(Basic_fun):
    click_BT=(By.ID,'com.huangguan.live:id/btnPhone')
    user_BT=(By.ID,'com.huangguan.live:id/userId')
    passwd_BT=(By.ID,'com.huangguan.live:id/passWord')
    login_BT=(By.ID,'com.huangguan.live:id/btn_login')
   
    def login(self,username,passwd):
        logging.info("===========login starting========")
        logging.info("username is %s"%username)
        logging.info("username is %s" % passwd)
        self.driver.find_element(*self.click_BT).click()
        self.driver.find_element(*self.user_BT).send_keys(username)
        self.driver.find_element(*self.passwd_BT).send_keys(passwd)
        self.driver.find_element(*self.login_BT).click()





if __name__ == '__main__':
    driver=appium_desired()
    login_cs = comm_fun(driver)
    login_cs.login('90005','12345678')
