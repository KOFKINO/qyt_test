import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

ping_pkt = IP(dst='192.168.186.129')/ICMP()
ping_res = sr1(ping_pkt,timeout=2,verbose=False)

ping_res.show()