# import  re
# str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
# vlanid = re.match('\d+',str1).group()
# mac = re.search('(\w{4}\.){2}\w{4}',str1).group()
# type = re.search('[A-Z]+',str1).group()
# int = re.search('G.*',str1).group()
#
# print(f'{"VLAN ID":<12}'+':'+vlanid+'\n'   \
#       +f'{"MAC":<12}'+':'+mac+'\n'          \
#       +f'{"Type":<12}'+':'+type+'\n'        \
#       +f'{"Interface":<12}'+':'+int)

import re
#提取protocol、server、localserver
str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
protocol = re.search('[A-Z]{3}',str1).group()
serverlist = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d+)',str1)
server = serverlist[0]
localserver = serverlist[1]
#提取idle
stridle = str1.split(',')[1]
h = re.findall('(\d+)',stridle)[0]
m = re.findall('(\d+)',stridle)[1]
s = re.findall('(\d+)',stridle)[2]

#提取bytes
strbytes = str1.split(',')[2]
bytes = re.findall('(\d+)',strbytes)[0]
#提取flags
strflags = str1.split(',')[3]
flags = re.findall('([A-Z]+)',strflags)[0]

#输出结果
result=f'{"protocol":<15}'+':'+protocol+'\n'\
        +f'{"server":<15}'+':'+server+'\n'\
        +f'{"localserver":<15}'+':'+localserver+'\n'\
        +f'{"idle":<15}'+':'+f'{h:<3}'+'小时'+f'{m:>3}'+'分钟'+f'{s:>3}'+'秒'+'\n'\
        +f'{"bytes":<15}'+':'+bytes+'\n'\
        +f'{"flags":<15}'+':'+flags
print(result)
