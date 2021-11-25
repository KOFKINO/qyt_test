import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *


def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()  # 制造一个Ping包
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)  # Ping并且把返回结果复制给ping_result

    if ping_result:
        return ip
    else:
        return


if __name__ == '__main__':
    result = qytang_ping('172.17.1.3')
    if result:
        print(result + '通！')
        print(type(result))
    else:
        print(result+ '不通！')
