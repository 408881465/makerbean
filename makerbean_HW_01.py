#makerbean Homework 1 2018-2-9
#codeing with UTF-8

import time

name = input("请输入你的名字:")
print("你的名字是： %s"%name)
sex = input("请输入您的性别：")
print("您的性别是： %s "%sex)
age = int(input("请输入你的年龄："))
print("您的年龄是： %d"%age)
school = input("请输入您的学校")
print("您的学校是： %s"%school)
print("正在生成您的简历......")
time.sleep(2)
print("********************")
print("       简历         ")
print("姓名:  %s"%name)
print("性别:  %s"%sex)
print("年龄:  %s"%age)
print("学校:  %s"%school)
