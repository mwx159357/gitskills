from baseview.basicview import Basic_fun
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time,os
import csv


class Common(Basic_fun):
    close_coin = (By.ID,'com.huangguan.live:id/btn_close_attendance')

    def check_closecoin(self):
        try:
            close_coin=self.driver.find_element(*self.close_coin)
        except NoSuchElementException:
            pass
        else:
            close_coin.click()


    def get_size(self):
        x=self.driver.get_windoes_size()['width']
        y=self.driver.get_windoes_size()['height']
        return x,y

    '''左划'''
    def swipLeft(self):
        l=self.get_size()
        x1 =int(l[0]*0.9)
        y1 =int(l[1]*0.5)
        x2 = int(l[0]*0.1)
        self.swip(x1,y1,x2,y1,1000)

        '''右划'''
    def swipRight(self):
        l = self.get_size()
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.9)
        self.swip(x1, y1, x2, y1, 1000)


    def get_time(self):
        self.now_time=time.strftime('%Y-%m-%d %H-%M-%S')
        return self.now_time

    def get_ScreenShor(self,module):
        time=self.get_time()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png'%(module,time)
        logging.info("=========Screenshots in progress========")
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self,csv_file,line):
        logging.info("=========get_csv_data=======")
        with open(csv_file,encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row




if __name__ =="__main__":
    csv_file = '../data/account'
    reader=Common()
    data=reader.get_csv_data(csv_file,2)
    print(data)
