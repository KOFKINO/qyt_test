import re
import kamene
from ping_test import qytang_ping
from ssh import qytang_ssh


def get_int_infor(*ips, username='admin', password='H3c.com!123'):
    # device_int_dict = {}
    print(qytang_ping(ips))
    # if qytang_ping(ips):
    #     infor_all = qytang_ssh(ips, username, password, cmd='dis ip int brief')
    #     for x in infor_all.split('\n'):
    #         int_infor = re.findall(r'([A-Z]\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', x)
    #         print(int_infor)


if __name__ == '__main__':
    get_int_infor('172.17.1.3', username='admin', password='H3c.com!123')

