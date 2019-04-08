from common.BSTestRunner import BSTestRunner
import sys,time,logging
import unittest

path = r'C:\Users\Administrator\PycharmProjects\huangguan_project'
sys.path.append(path)
test_dir='../test_case'
test_report = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_login_fun.py')
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name= test_report+'/'+now+"test_HG_reports.html"

with open(report_name,'wb') as f:
    runner= BSTestRunner(stream=f,title='HG Test Report',description="HangGuang Android App Test Report")
    logging.info("start run test case.....")
    runner.run(discover)

