from datetime import datetime

ip = None
with open('ip', 'r') as f:
	ip = f.read()
f.close()

ip = ip.split(' ')
ip = ip[1]
with open('ip', 'w') as f:
	f.write(ip)
f.close()

with open('track', 'a') as f:
	f.write(datetime.now().strftime("%H:%M:%S"))+'\n'
f.close()
