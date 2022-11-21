ip = Null
with open('ip', 'r') as f:
	ip = f.read()
f.close()

ip = ip.split(' ')
ip = ip[1]
with open('ip', 'w') as f:
	f.write(ip)
f.close()
