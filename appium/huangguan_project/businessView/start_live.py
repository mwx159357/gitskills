from common.comm_fun import Common
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from businessView.login_fun import Login_in
from common.desired_caps import appium_desired
import logging


'开播，密码房，聊天室'
class Start_live(Login_in):
    kb_button=(By.ID,'com.huangguan.live:id/img_live')
    live_broadcast = (By.ID,'com.huangguan.live:id/iv_start_live')

    Whisper_button = (By.ID,'com.huangguan.live:id/liveTitle')
    Start_Live_Button = (By.ID,'com.huangguan.live:id/startLive')

    # 聊天室
    voice_Button = (By.ID,'com.huangguan.live:id/iv_chat_creat')
    chatroom_title = (By.ID,'com.huangguan.live:id/chatRoomTitle')
    creat_chatroom = (By.ID,'com.huangguan.live:id/tv_creat_chat_room')

    # 私密直播
    Private_passwd = (By.ID,'com.huangguan.live:id/tv_import_password')
    Private_Button = (By.ID,'com.huangguan.live:id/iv_private_space')
    confim_passwd = (By.ID,'com.huangguan.live:id/btn_affirm_password')

    # 主播头像
    Anchor_head = (By.ID,'com.huangguan.live:id/layout_head_hat')
    '''直播间'''
    def start_to_live(self,Whisper):

        logging.info("========starting live broadcast======== ")
        self.driver.find_element(*self.kb_button).click()
        self.driver.find_element(*self.live_broadcast).click()
        logging.info("=========input Whisper======== ")
        self.driver.find_element(*self.Whisper_button).send_keys(Whisper)
        self.driver.find_element(*self.Start_Live_Button).click()
        self.driver.implicitly_wait(5)

    '''聊天室'''
    def start_to_voice(self,Whisper):
        logging.info("========starting live chatroom======== ")
        self.driver.find_element(*self.kb_button).click()
        self.driver.find_element(*self.voice_Button).click()
        self.driver.find_element(*self.chatroom_title).clear()
        self.driver.find_element(*self.chatroom_title).send_keys(Whisper)
        self.driver.find_element(*self.creat_chatroom).click()
        self.driver.implicitly_wait(8)

    '''私密直播'''
    def start_to_private_live(self,Password,Whisper):
        logging.info("========starting private live========")
        self.driver.find_element(*self.kb_button).click()
        self.driver.find_element(*self.Private_passwd).clear()
        self.driver.find_element(*self.Private_passwd).send_keys(Password)
        self.driver.find_element(*self.confim_passwd).click()
        self.driver.find_element(*self.Whisper_button).send_keys(Whisper)
        self.driver.find_element(*self.Start_Live_Button).click()
        self.driver.implicitly_wait(5)

    def check_live_success(self):
        try:
            self.driver.find_element(*self.Anchor_head)
        except NoSuchElementException:
            return False
        else:
            return True


if __name__ == '__main__':
    driver = appium_desired()
    l=Start_live(driver)
    l.login('11111138','12345678')
    l.check_closecoin()
    l.start_to_voice(Whisper='90005开播了')
    result = l.check_live_success()
    print(result)





