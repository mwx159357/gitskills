from appium import webdriver
import yaml
import logging
import logging.config
import os

CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    with open('../config/HG.yaml',encoding='utf-8') as file:
        data = yaml.load(file)
    desired_caps = {}
    desired_caps["resetKeyboard"] =data["resetKeyboard"]
    desired_caps["appActivity"] =data["appActivity"]
    desired_caps["appPackage"] =data["appPackage"]
    desired_caps["unicodeKeyboard"] =data["unicodeKeyboard"]

    basic_path = os.path.dirname(os.path.dirname(__file__))
    app_dir=basic_path+"/app/"+data["appname"]
    desired_caps["app"]=app_dir
    # desired_caps["appname"] =data["appname"]

    desired_caps["platformName"] =data["platformName"]
    desired_caps["platformVersion"] =data["platformVersion"]
    desired_caps["deviceName"] =data["deviceName"]

    logging.info("start app......")
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver


if __name__ =="__main__":
    driver = appium_desired()