from baseview.basicview import Basic_fun
from common.desired_caps import appium_desired
from common.comm_fun import Common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging,time



class Login_in(Common):
    click_BT = (By.ID, 'com.huangguan.live:id/btnPhone')
    user_BT = (By.ID, 'com.huangguan.live:id/userId')
    passwd_BT = (By.ID, 'com.huangguan.live:id/passWord')
    login_BT = (By.ID, 'com.huangguan.live:id/btn_login')
    close_recivecoin = (By.ID, 'com.huangguan.live:id/btn_close_attendance')
    ME_button = (By.ID, "com.huangguan.live:id/me")

    #weixin
    wx_user_list = (By.ID,'com.tencent.mm:id/bwk')
    wx_pwd_list= (By.ID,'com.tencent.mm:id/bwl')
    wx_bt = (By.ID,'com.tencent.mm:id/bwn')
    # WX_author = ()

    #QQ
    qq_user =(By.CLASS_NAME,'android.widget.EditText')
    qq_pwd = (By.ID,'com.tencent.mobileqq:id/password')
    qq_pwd_login=(By.ID,'com.tencent.mobileqq:id/login')
    qq_author = (By.CLASS_NAME,'android.widget.Button')

    #选择登录方式
    QQ_login_bt =(By.ID,"com.huangguan.live:id/btnQQ")
    WX_login_bt =(By.ID,"com.huangguan.live:id/btnWeChat")

    '''第三方登录'''
    def Third_login(self,method,username,passwd):
        if method.upper() == "QQ":
            self.driver.find_element(*self.QQ_login_bt).click()
            try:
                qq_login_bt=self.driver.find_element(*self.qq_author)
            except NoSuchElementException:
                try:
                    qq_pwd_login=self.driver.find_element(*self.qq_pwd_login)
                except NoSuchElementException:
                    logging.info("======第三方登录跳转失败，或已登录成功=======")
                else:
                    self.login_Qq(username,passwd)
                    self.get_ScreenShor("qq登录成功")
            else:
                qq_login_bt.click()
        elif method.upper()=="WX":
            self.driver.find_element(*self.WX_login_bt).click()
            try:
                WX_login_author = self.driver.find_element(*self.wx_bt)
            except NoSuchElementException:
                try:
                    WX_pwd_login = self.driver.find_element(*self.wx_bt)
                except NoSuchElementException:
                    logging.info("======第三方登录跳转失败，或已登录成功=======")
                else:
                    self.login_WeiXin(username,passwd)
                    self.get_ScreenShor("qq登录成功")
            else:
                WX_login_author.click()

    '''账号登录'''
    def login(self, username, passwd):
        logging.info("===========login starting========")
        self.driver.find_element(*self.click_BT).click()
        logging.info("username is %s" % username)
        self.driver.find_element(*self.user_BT).send_keys(username)
        logging.info("passwd is %s" % passwd)
        self.driver.find_element(*self.passwd_BT).send_keys(passwd)
        self.driver.find_element(*self.login_BT).click()

    def login_Qq(self,username,passwd):
        logging.info("=========login QQ=========")
        self.driver.find_elements(*self.qq_user).clear()
        self.driver.find_elements(*self.qq_user).send_keys(username)
        self.driver.find_elements(*self.qq_pwd).clear()
        self.driver.find_elements(*self.qq_pwd).send_keys(passwd)
        self.driver.find_element(*self.qq_pwd_login).click()
        time.sleep(5)

    def login_WeiXin(self,username,passwd):
        logging.info("=========login weixin=========")
        user_bt = self.driver.find_elements(*self.wx_user_list)
        user_bt[1].clear()
        user_bt[1].send_keys(username)
        pwd_bt = self.driver.find_elements(*self.wx_pwd_list)
        pwd_bt[1].clear()
        pwd_bt[1].send_keys(passwd)

        self.driver.find_element(*self.wx_bt).click()
        time.sleep(5)

    '''检查登录状态'''
    def check_login_status(self):
        logging.info("==============check close_recivecoin tips============")
        try:
            close_Recoin=self.driver.find_element(*self.close_recivecoin)
        except NoSuchElementException:
            logging.info("no recivecoin  Tips，check me tips")
            try:
                me_bt=self.driver.find_element(*self.ME_button)
            except NoSuchElementException:
                return False
            else:
                logging.info("=========login success======")
                me_bt.click()
                return True
        else:
            logging.info("=========login success======")
            close_Recoin.click()
            return True

if __name__ == '__main__':
    file_csv = '../data/account'
    driver = appium_desired()
    login_cs = Login_in(driver)
    data = login_cs.get_csv_data(file_csv,2)
    login_cs.login(data[0],data[1])
    resu=login_cs.check_login_status()
    print(resu)
