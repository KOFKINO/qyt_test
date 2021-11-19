import re
import os

# 获取当前路径:
path = (os.getcwd())
print(path)
# 输入文件名
filename = input('请输入配置文件名：')

with open('{}\{}'.format(path,filename),'r',encoding = 'utf-8') as f:
    str1 = f.read()
with open('{}\{}_sn.txt'.format(path,filename), 'w', encoding='utf-8') as f2:
    #slot cpu sn
    slot = re.findall('(Slot\s+\d+\s+CPU\s+\d+):\s+\w+\s+:\s+\S+\s+DEVICE_(SERIAL_NUMBER\s+:\s+\S+)',str1)
    for i in range(len(slot)):
        print(slot[i][0],file = f2)
        print(slot[i][1],file = f2)
    #fan sn
    fan = re.findall('(FAN\s+\d+\s):\s+\w+\s+:\s+\S+\s+DEVICE_(SERIAL_NUMBER\s+:\s+\S+)', str1)
    for i in range(len(fan)):
        print(fan[i][0],file = f2)
        print(fan[i][1],file = f2)


    #接口sn
    interface = re.findall('(\w+-?Gig\S+)\s+transceiver\s+manufacture\s+information:\s+Manu. (Serial Number :\s+\w+)',str1)

    for i in range(len(interface)):
        print(interface[i][0],file = f2)
        print(interface[i][1],file = f2)


