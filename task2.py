# !python3
# script to print out the valid IPs of a specified network
# ipaddress - ipv4/ipv6 manipulation library
import ipaddress 

print("Enter a network in the following format xxx.xxx.xxx.0/xx:")
network = input()
netobj = ipaddress.ip_network(network)

for i in netobj.hosts():
	print(i)

print('\nHit enter to escape.')
input()
