#coding=utf-8
import unittest
import  time
from Driver import Driver
id = input("请选择浏览器：1-火狐，2-谷歌")


class WtLoginTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = Driver(id)

    def tearDown(self):
        self.driver.driver.quit()
        print("test end")

    def test_case1(self):
        '''用户名正确，密码错误（测试教师)'''
        self.driver.start("http://web3.wotime.com.cn")
        time.sleep(2)
        self.driver.login("zhangsanfeng","12345")
        time.sleep(1)
        error_message1 = self.driver.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/p").text
        self.assertEqual(str(error_message1),"登入失败")
        print("用例1测试结束")


    def test_case2(self):
        '''用户名正确，密码正确'''
        self.driver.start("http://web3.wotime.com.cn")
        time.sleep(2)
        self.driver.login("zhangsanfeng","123456")
        time.sleep(1)
        if int(id) == 1:
            error_message2 = self.driver.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[4]/span").text
        elif int(id) == 2:
            error_message2 = self.driver.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[4]/span').text
        self.assertEqual(str(error_message2),"  历史参赛记录")
        print("用例2测试结束")
    def test_case3(self):
        '''不输入用户名，只输入密码'''
        self.driver.start("http://web3.wotime.com.cn")
        time.sleep(2)
        self.driver.login("", "12345")
        time.sleep(1)
        if int(id) == 1:
            error_message3 = self.driver.driver.find_element_by_xpath("/html/body/div[1]/div/nav/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div").text
        elif int(id) == 2:
            error_message3 = self.driver.driver.find_element_by_xpath('//*[@id="login-nav"]/form/div[1]/div[2]/div').text
        self.assertIn("用户名不能为空",str(error_message3))
        print("用例3测试结束")

    def test_case4(self):
        '''只输入用户名，不输入密码'''
        self.driver.start("http://web3.wotime.com.cn")
        time.sleep(2)
        self.driver.login("zhangsanfeng", "")
        time.sleep(1)
        if int(id) == 1:
            error_message4 = self.driver.driver.find_element_by_xpath("/html/body/div[1]/div/nav/div[2]/div/div/div[2]/div/form/div[2]/div[2]/div").text
        elif int(id) == 2:
            error_message4 = self.driver.driver.find_element_by_xpath('//*[@id="login-nav"]/form/div[2]/div[2]/div').text
        self.assertIn("密码不能为空",str(error_message4))
        print("用例4测试结束")

    def test_case5(self):
        '''输入正确的用户名和密码（测试学生）'''
        self.driver.start("http://web3.wotime.com.cn")
        time.sleep(2)
        self.driver.login("zhanggaozhong", "123456")
        time.sleep(1)
        if int(id) == 1:
            error_message5 = self.driver.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[3]/span").text
        elif int(id) == 2:
            error_message5 = self.driver.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[3]/span').text
        self.assertIn("我的历史成绩",str(error_message5))
        print("用例5测试结束")

if __name__ == "__main__":
    unittest.main()

