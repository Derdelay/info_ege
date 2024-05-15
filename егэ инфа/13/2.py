from ipaddress import *

for mask in range(33):
    net = ip_network(f'122.159.136.144/{mask}', 0)
    print(net, net.netmask)