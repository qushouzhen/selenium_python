#coding=utf-8
n = input("输入编号（学前/小低：练习-1，比赛-2；小低/初中/高中：练习-3，比赛-4）:")
print(n)
student = Driver()
student.start("http://web3.wotime.com.cn")
time.sleep(2)
student.login('zhanggaozhong',123456)

time.sleep(2)

if int(n) == 1:
    student.joinPractice_kindergarten() #测试学前组/小低组练习模式
    print("测试学前组/小低组练习模式")
elif int(n) == 2:
    student.joinCompetion_kindergarden()    #测试学前组/小低组比赛模式
    print("测试学前组/小低组比赛模式")
elif int(n) == 3:
    student.joinPractice_middleSchool()   #测试小高/初中/高中练习模式
    print("测试小高/初中/高中练习模式")
else:
    student.joinCompetion_middleSchool()  #测试小高/初中/高中比赛模式
    print("测试小高/初中/高中比赛模式")
time.sleep(3)
student.playGame_Chinese()
