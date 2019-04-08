import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep
import warnings

class StartEnd(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        logging.info("=======setup=====")
        self.driver=appium_desired()

    def tearDown(self):
        logging.info("======teardown=====")
        sleep(8)
        self.driver.close_app()