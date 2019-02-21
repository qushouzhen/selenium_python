# -*- coding:utf-8 -*-
from selenium import webdriver
import time,os
driver = webdriver.Firefox()
driver.get("http://web3.wotime.com.cn")
driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/div/div/div/div/div").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/nav/div[1]/ul/li[12]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/div/div[2]/div/form/div[1]/div[2]/input").send_keys("saishi")
driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/div/div[2]/div/form/div[2]/div[2]/input").send_keys("123456")
driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/div/div[2]/div/div/div/button[1]").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[1]/ul/li[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/button[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[4]/button").click()
driver.find_element_by_xpath('//*[@id="confirm"]').click()
for num in range(0,200):
    input_num=num+1
    driver.find_element_by_id("input_"+str(num)).send_keys(driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div/div[5]/div[1]/div[1]/div['+str(input_num)+']').text)





