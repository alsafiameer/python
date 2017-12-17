from netaddr import *
import pprint 

ADDRESSES_25 = []
ADDRESSES_25_all = []

ADDRESSES_27 = []

ip = IPNetwork('192.168.0.0/19') 
subnets_25 = list(ip.subnet(25))

for i in subnets_25:
	ADDRESSES_25.append(str(i))
	ADDRESSES_25_all.append(i)

ip_27 = ADDRESSES_25_all[2]
subnets_27 = list(ip_27.subnet(27))

for ip in subnets_27:
	ADDRESSES_27.append(str(ip))

print ADDRESSES_27
print ADDRESSES_25[2]

#ALL_HOSTS.append(H.strip())
