#coding=utf-8
import time
from Driver import Driver
from data import ExcelUnitl
import  unittest

file_path = 'C:\\Users\\test\\Desktop'
file_name = 'teacher_register.xls'
boswer_id = input("请选择浏览器类型：1--火狐，2--谷歌: ")
teacher = Driver(boswer_id)
teacher_data = ExcelUnitl(file_path, file_name)
username = teacher_data.getName()
teacher.start("http://web3.wotime.com.cn")
time.sleep(2)
for i in range(0,len(username)):
    teacher.teacher_regisiter(username[i],"123456","qu","第一学校","123@qq.com",
                              "15692153521")
    time.sleep(2)

