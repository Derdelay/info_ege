from ipaddress import *
for m in range(33):
    n = ip_network(f'157.127.182.76/{m}',0) 
    n2 = ip_network(f'157.127.190.80/{m}',0)
    if n!=n2:
        print(n,n2)