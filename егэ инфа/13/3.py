from ipaddress import *

net = ip_network(f'122.159.136.144/255.255.255.248', 0)
print(net, net.netmask)