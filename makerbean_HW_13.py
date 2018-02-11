#这个程序使用类作为存储个人简历的数据结构
#Author tangmingsh@163.com

import time


class Person:

    def __init__(self,name,sex,age,school):
        self.name = name
        self.sex = sex
        self.age = age
        self.school = school
    def print_profile(slef):
        print("您的姓名是 %s:" % slef.name)
        print("您的性别是 %s:" % slef.sex)
        print("您的年龄是 %s:" % slef.age)
        print("您的学校是 %s:" % slef.school)

person =Person('','','','')

person.name = input("请输入您的姓名: ")
person.sex = input("请输入您的性别: ")
person.age = input("请输入您的年龄: ")
person.school = input("请输入您的学校: ")

time.sleep(0.5)
print("正在生成您的简历......")
print("********简历*******")
person.print_profile()





