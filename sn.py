import re


with open(r'C:\Users\admin.MENGFANDE3-PC\Desktop\S6800C.TG-CC.JXF','r',encoding = 'utf-8') as f:
    str1 = f.read()

    #slot cpu sn
    slot = re.findall('(Slot\s+\d+\s+CPU\s+\d+):\s+\w+\s+:\s+\S+\s+DEVICE_(SERIAL_NUMBER\s+:\s+\S+)',str1)
    for i in range(len(slot)):
        print(slot[i][0])
        print(slot[i][1])
    #fan sn
    fan = re.findall('(FAN\s+\d+\s):\s+\w+\s+:\s+\S+\s+DEVICE_(SERIAL_NUMBER\s+:\s+\S+)', str1)
    for i in range(len(fan)):
        print(fan[i][0])
        print(fan[i][1])


    #接口sn
    interface = re.findall('(\w+-?Gig\S+)\s+transceiver\s+manufacture\s+information:\s+Manu. (Serial Number :\s+\w+)',str1)

    for i in range(len(interface)):
        print(interface[i][0])
        print(interface[i][1])
