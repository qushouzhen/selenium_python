# -*- coding:utf-8 -*-
from selenium import webdriver
import time


class Driver:
    def __init__(self,m):
        self.m = m
        if int(self.m) == 1:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

    def start(self,url):
        self.driver.get(url)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[6]/div/div/div/div/div").click()

    def student_register(self,username,pwd,trueName,birth_date,school,email,telphone,grade_code):
        if int(self.m) == 1:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/nav/div[1]/ul/li[11]/a").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/label/input").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/input").send_keys(username)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[2]/div/input").send_keys(pwd)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[3]/div/input").send_keys(pwd)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[4]/div/input").send_keys(trueName)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[5]/div/div/input").send_keys(birth_date)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[1]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[1]/option[18]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[2]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[2]/option[8]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[3]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[3]/option[9]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[7]/div/input").send_keys(school)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[8]/div/input").send_keys(email)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[11]/div/input").send_keys(telphone)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div/div/div/select[1]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div/div/div/select[1]/option["+grade_code+"]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div/div/div/select[2]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div/div/div/select[2]/option[2]").click()
            if int(grade_code) in [2,3]:
                self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[13]/fieldset/div/div[2]/div[2]/label/input").click()

            elif int(grade_code) in [4,5,6]:
                for i in range(1, 3):
                    self.driver.find_element_by_xpath(
                        "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[13]/fieldset/div/div[2]/div[2]/label["+str(i)+"]/span").click()
                self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[13]/fieldset/div/div[3]/div[2]/label/input").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[14]/div/input").click()
            time.sleep(1)
            #self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button").click()
        elif int(self.m) == 2:
            self.driver.find_element_by_xpath('//*[@id="top-nav"]/ul/li[11]/a').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[2]/label/img').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/input').send_keys(username)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[2]/div/input').send_keys(pwd)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[3]/div/input').send_keys(pwd)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[4]/div/input').send_keys(trueName)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[5]/div/div/input').send_keys(birth_date)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[1]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[1]/option[17]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[2]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[2]/option[8]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[3]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[3]/option[5]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[7]/div/input').send_keys(school)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[8]/div/input').send_keys(email)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div/div/div/select[1]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div/div/div/select[1]/option['+grade_code+']').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div/div/div/select[2]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[10]/div/div/div/select[2]/option[2]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[11]/div/input').send_keys(telphone)
            if int(grade_code) in [2,3]:
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[13]/fieldset/div/div[2]/div[2]/label/input').click()
            elif int(grade_code) in [4,5,6]:
                for i in range(1,4):
                    self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[13]/fieldset/div/div[2]/div[2]/label['+str(i)+']/input').click()
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[13]/fieldset/div/div[3]/div[2]/label/input').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[14]/div/input').click()
            time.sleep(1)
            #self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button/span').click()

    def teacher_regisiter(self,username,pwd,trueName,school,email,tel):
        if int(self.m) == 1:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/nav/div[1]/ul/li[11]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/input").send_keys(username)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[2]/div/input").send_keys(pwd)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[3]/div/input").send_keys(pwd)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[4]/div/input").send_keys(trueName)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[1]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[1]/option[15]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[2]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[2]/option[5]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[3]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[3]/option[11]").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[7]/div/input").send_keys(school)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[8]/div/input").send_keys(email)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[11]/div/input").send_keys(tel)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/form/div[14]/div/input").click()
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button").click()
        elif int(self.m) == 2:
            self.driver.find_element_by_xpath('//*[@id="top-nav"]/ul/li[11]/a').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/input').send_keys(username)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[2]/div/input').send_keys(pwd)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[3]/div/input').send_keys(pwd)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[4]/div/input').send_keys(trueName)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[1]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[1]/option[6]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[2]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[2]/option[4]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[3]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/select[3]/option[3]').click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[7]/div/input').send_keys(school)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[8]/div/input').send_keys(email)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/form/div[11]/div/input').send_keys(tel)
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

    def login(self,username,password):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/nav/div[1]/ul/li[12]/a").click()
        if int(self.m) == 1:
            self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/nav/div[2]/div/div/div[2]/div/form/div[1]/div[2]/input").send_keys(username)
            self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/nav/div[2]/div/div/div[2]/div/form/div[2]/div[2]/input").send_keys(password)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/nav/div[2]/div/div/div[2]/div/div/div/button[1]").click()

        elif int(self.m) == 2:
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '//*[@id="login-nav"]/form/div[1]/div[2]/input').send_keys(username)
            self.driver.find_element_by_xpath(
                '//*[@id="login-nav"]/form/div[2]/div[2]/input').send_keys(password)
            self.driver.find_element_by_xpath(
                '//*[@id="login-nav"]/div/div/button[1]').click()



    def joinPractice_kindergarten(self):
        if int(self.m) == 1:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[1]/ul/li[2]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/button[2]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[4]/button").click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="confirm"]').click()
        elif int(self.m) == 2:
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/button[2]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[4]/button').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="confirm"]').click()

    def joinCompetion_kindergarden(self):
        if int(self.m) == 1:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[1]/ul/li[2]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/button[1]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[4]/div/button").click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="confirm"]').click()
        elif int(self.m) == 2:
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/button[1]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[4]/div/button').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="confirm"]').click()

    def joinPractice_middleSchool(self):
        if int(self.m) == 1:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[1]/ul/li[2]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[4]/button").click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="confirm"]').click()
        elif int(self.m) == 2:
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[4]/button').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="confirm"]').click()

    def joinCompetion_middleSchool(self):
        if int(self.m) == 1:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[1]/ul/li[2]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[1]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[4]/div/button").click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="confirm"]').click()
        elif int(self.m) == 2:
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[1]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[4]/div/button').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="confirm"]').click()


    def playGame_Chinese(self,word_num,game_type):
        if int(self.m) ==1:
            for num in range(0,word_num):
                input_num = num + 1
                self.driver.find_element_by_id("input_" + str(num)).send_keys(self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div[3]/div/div/div[5]/div[1]/div[1]/div[' + str(
                        input_num) + ']').text)
        elif int(self.m) == 2:
            time.sleep(1)
            for num in range(0,word_num):
                input_num = num + 1
                self.driver.find_element_by_id("input_" + str(num)).send_keys(self.driver.find_element_by_xpath(
                    '//*[@id="target_area"]/div[' + str(input_num) + ']').text)
        time.sleep(180)
        if game_type == 1:
            score = float(self.driver.find_element_by_xpath('//*[@id="praticescoreid"]').text)
            print(score)
            return score
        elif game_type == 2:
            score = float(self.driver.find_element_by_xpath('//*[@id="scoreid"]').text)
            print(score)
            return score



    def end_game(self):
        if int(self.m) == 1:
            self.driver.find_element_by_id('exit-link').click()
            time.sleep(3)
            self.driver.close()
        if int(self.m) == 2:
            self.driver.find_element_by_id('exit-link').click()
            time.sleep(3)
            self.driver.close()



