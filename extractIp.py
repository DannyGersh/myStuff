ip = None
with open('/main/myStuff/ip', 'r') as f:
	ip = f.read()
f.close()

ip = ip.split(' ')
ip = ip[1]
with open('/main/myStuff/ip', 'w') as f:
	f.write(ip)
f.close()
