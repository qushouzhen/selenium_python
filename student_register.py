#coding=utf-8
import time
from Driver import Driver
from data import ExcelUnitl
file_path = 'C:\\Users\\test\\Desktop'
file_name = 'register.xls'
boswer_id = input("请选择浏览器类型：1--火狐，2--谷歌: ")
student = Driver(boswer_id)
student_data = ExcelUnitl(file_path,file_name)
username = student_data.getName()
grade_mode = student_data.getGrade()
student.start("http://web3.wotime.com.cn")
time.sleep(2)
for i in range(0,len(username)):
    student.student_register(str(username[i]),"123456","qu","2012-01-23","第一幼儿园","782747526@qq.com","15692153521",
                             str(int(grade_mode[i])+1))
    time.sleep(2)

