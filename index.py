#coding=utf-8
import random
 
#初始化列表
ll=[]
 
#将10个数字转化成字符串形式并添加到列表里
for i in range(10):
    ll.append(str(i))
    
#将A-Z添加到列表里
for i in range(65,91):
    ll.append(chr(i))
 
#将a-z添加到列表里
for i in  range(97,123):
    ll.append(chr(i))
 
#生成激活码的函数
def get_code(length):
    code=''
    for i in range(length):
        #从列表里随机选择一个元素
        ss=random.choice(ll)
        code=code+ss
    print(code)
 
if __name__=='__main__':
    #自己决定激活码的长度
    l=int(input('please input the length of the code: '))
    #自己决定要生成的激活码的个数
    x=int(input('please input the number of the code: '))
    for i in range(x):
        get_code(l)

