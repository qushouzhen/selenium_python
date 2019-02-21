# -*- coding:utf-8 -*-
from selenium import webdriver
from getwordNum import getNum
import time
from Driver import Driver
from data import ExcelUnitl
file_path = 'C:\\Users\\test\\Desktop'
file_name = "register.xls"
student_info = ExcelUnitl(file_path,file_name)
student_name = student_info.getName()  #获取表格中的学生姓名
student_pwd = student_info.getPwd() #获取表格中学生的密码
student_grade = student_info.getGrade()  #获取表格中学生的年级
boswer_id = input("请选择浏览器类型：1--火狐，2--谷歌: ")
game_mode = input("请选择比赛类型：1--练习，2--正式比赛：")
game_time = input("请选择比赛次数： ")
print("正在执行"+file_name+"中的学生进行中英文对抗赛的比赛")
 # 循环执行表格内学生的比赛
for j in range(0,int(game_time)):
    for i in range(0,len(student_name)):
        student_driver = Driver(boswer_id)
        student_driver.start("http://web3.wotime.com.cn")
        time.sleep(2)
        student_driver.login(student_name[i],student_pwd[i])
        time.sleep(2)
        if int(game_mode) == 1 and int(student_grade[i]) in [1,2]:
            student_driver.joinPractice_kindergarten()  # 测试学前组/小低组练习模式
            print("测试学前组/小低组练习模式"+student_name[i])
        elif int(game_mode) == 2 and int(student_grade[i])in [1,2]:
            student_driver.joinCompetion_kindergarden()  # 测试学前组/小低组比赛模式
            print("测试学前组/小低组比赛模式"+student_name[i])
        elif int(game_mode) == 1 and int(student_grade[i]) in[3,4,5]:
            student_driver.joinPractice_middleSchool()  # 测试小高/初中/高中练习模式
            print("测试小高/初中/高中练习模式"+student_name[i])
        elif int(game_mode) == 2 and int(student_grade[i]) in [3,4,5]:
            student_driver.joinCompetion_middleSchool()  # 测试小高/初中/高中比赛模式
            print("测试小高/初中/高中比赛模式"+student_name[i])
        time.sleep(3)
        student_driver.playGame_Chinese(getNum(student_grade[i]),int(game_mode))
        time.sleep(5)
        student_driver.end_game()
