#这个程序使用字典作为存储个人简历的数据结构
#Author tangmingsh@163.com

import time

#定义Person字典用来存储数据，初始值为空
person = {
    '姓名': '',
    '性别': '',
    '年龄': '',
    '学校': ''
    }
#利用循环接受用户输入，并赋值给相应的键
for key,value in person.items():
    value = input("请输入您的%s: "%(key))
    person[key] = value

print("正在生成您的简历......")
#利用时间模拟正在生成简历
time.sleep(1)

#利用循环打印个人简历
print("************************")
print("       您的简历         ")
for key,value in person.items():
    print("%s ： %s"%(key,value))



