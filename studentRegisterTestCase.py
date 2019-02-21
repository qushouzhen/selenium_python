#coding=utf-8
import unittest
from Driver import Driver
import time
import random
id = input("请选择浏览器：1-火狐，2-谷歌")


class StudentRegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver(id)
        self.driver.start("http://web3.wotime.com.cn")
        time.sleep(2)
    def tearDown(self):
        self.driver.driver.quit()
        print("test end")

    def getErrorMessage(self,firefox_xpath,chrome_xpath):
        if int(id) == 1:
            error_message = self.driver.driver.find_element_by_xpath(firefox_xpath).text
        elif int(id) == 2:
            error_message = self.driver.driver.find_element_by_xpath(chrome_xpath).text
        return error_message

    def testCase1(self):
        '''缺少用户名'''
        self.driver.student_register("","123456","Test","2012-01-02","first-scholl","123@qq.com","15692153521",random.radint(2, 6))
        time.sleep(2)
        firefox_xpath = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/div[2]"
        chrome_xpath = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/div[2]'
        error_message = self.getErrorMessage(firefox_xpath,chrome_xpath)
        self.assertIn("用户名不能为空",error_message)

    def testCase2(self):
        '''缺少密码'''
        self.driver.student_register("0215Test"+str(random.randint(1,9999)),"","Test","2012-01-02","first-scholl","123@qq.com","15692153521",random.radint(2, 6))
        time.sleep(1)
        firefox_xpath = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[2]/div/div"
        chrome_xpath = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[2]/div/div'
        error_message = self.getErrorMessage(firefox_xpath, chrome_xpath)
        self.assertIn("该字段不能为空",error_message)

    def testCase3(self):
        '''缺少确认密码'''
        self.driver.student_register("0215Test"+str(random.randint(1,9999)),"","Test","2012-01-02","first-scholl","123@qq.com","15692153521",random.radint(2, 6))
        time.sleep(1)
        firefox = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[3]/div/div"
        chrome = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[3]/div/div'
        error_message = self.getErrorMessage(firefox, chrome)
        self.assertIn("该字段不能为空",error_message)

    def testCase4(self):
        '''缺少真实姓名'''
        self.driver.student_register("0215Test"+str(random.randint(1,9999)),"123456","","2012-01-02","first-scholl","123@qq.com","15692153521",random.radint(2, 6))
        time.sleep(1)
        firefox = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[4]/div/div"
        chrome = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[4]/div/div'
        error_message = self.getErrorMessage(firefox, chrome)
        self.assertIn("该字段不能为空", error_message)

    def testCase5(self):
        '''缺少学校信息'''
        self.driver.student_register("0215Test" + str(random.randint(1, 9999)), "123456", "Test", "2012-01-02",
                                     "", "123@qq.com", "15692153521", random.radint(2, 6))
        time.sleep(1)
        firefox = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[7]/div/div"
        chrome = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[7]/div/div'
        error_message = self.getErrorMessage(firefox, chrome)
        self.assertIn("该字段不能为空", error_message)

    def testCase6(self):
        '''缺少电子邮件'''
        self.driver.student_register("0215Test" + str(random.randint(1, 9999)), "123456", "Test", "2012-01-02",
                                     "first-school", "", "15692153521", random.radint(2, 6))
        time.sleep(1)
        firefox = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[8]/div/div"
        chrome = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[8]/div/div'
        error_message = self.getErrorMessage(firefox, chrome)

        self.assertIn("不能为空", error_message)

    def testCase7(self):
        '''缺少年级信息'''
        self.driver.student_register("0215Test" + str(random.randint(1, 9999)), "123456", "Test", "2012-01-02",
                                     "first-school", "123@qq.com", "15692153521", "")
        time.sleep(1)
        firefox = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div[2]"
        chrome = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div[2]'
        error_message = self.getErrorMessage(firefox, chrome)
        self.assertIn("请选择正确的年级信息", error_message)

    def testCase8(self):
        '''缺少电话号码'''
        self.driver.student_register("0215Test" + str(random.randint(1, 9999)), "123456", "Test", "2012-01-02",
                                     "first-school", "123@qq.com", "", random.randint(2, 6))
        time.sleep(1)
        firefox = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[11]/div/div"
        chrome = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[11]/div/div'
        error_message = self.getErrorMessage(firefox, chrome)
        self.assertIn("该字段不能为空", error_message)


    def testCase9(self):
        '''用户名过短'''
        if int(id) == 1:
            self.driver.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/input").send_keys("asdfg")
        elif int(id) == 2:
            self.driver.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/input').send_keys("asdfg")
        firefox = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/div[2]"
        chrome = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/div[2]'
        error_message = self.getErrorMessage(firefox, chrome)
        self.assertIn(" 用户名必须为6-20个字符 ", error_message)

    def testCase10(self):
        '''用户名过长'''
        if int(id) == 1:
            self.driver.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/input").send_keys("asd123456789123456789")
        elif int(id) == 2:
            self.driver.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/input').send_keys("asd123456789123456789")
        firefox = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/div[2]"
        chrome = '//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/div[2]'
        error_message = self.getErrorMessage(firefox, chrome)
        self.assertIn(" 用户名必须为6-20个字符 ", error_message)






if __name__ == "__main__":
    unittest.main()
