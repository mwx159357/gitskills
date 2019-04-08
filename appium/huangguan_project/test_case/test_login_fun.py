from businessView.login_fun import Login_in
from common.Start_End import StartEnd
import logging
import unittest

class Login_test(StartEnd):
    csv_file = '../data/account'
    QQ_file = '../data/QQ_account'
    WX_file = '../data/wx_account'

    @unittest.skip("skip test_login_normal")
    def test_login_normal(self):
        logging.info("========test test_login_normal ============")
        l=Login_in(self.driver)
        data=l.get_csv_data(self.csv_file,2)
        l.login(data[0],data[1])
        self.assertTrue(l.check_login_status())

    @unittest.skip("skip test__passwd_error")
    def test_login_passwd_error(self):
        logging.info("========test test_login_passwd_error ============")
        l = Login_in(self.driver)
        data = l.get_csv_data(self.csv_file, 3)
        l.login(data[0], data[1])
        self.assertFalse(l.check_login_status())

    @unittest.skip("skip the test_third_login_qq_normal")
    def test_third_login_qq_normal(self):
        logging.info("=========test QQ login ========")
        l = Login_in(self.driver)
        data = l.get_csv_data(self.QQ_file, 2)
        l.Third_login(method='qq',username=data[0],passwd=data[1])
        self.assertTrue(l.check_login_status())

    # @unittest.skip("skip test_third_login_wx_normal")
    def test_third_login_wx_normal(self):
        logging.info("=========test weixin login ========")
        l = Login_in(self.driver)
        data = l.get_csv_data(self.WX_file, 2)
        l.Third_login(method='WX', username=data[0], passwd=data[1])
        self.assertTrue(l.check_login_status())

if __name__ == "__main__":
    unittest.main()


