ips = ['192.168.1.1','192.168.1.1','192.168.1.2','192.168.1.1','192.168.1.3','192.168.1.2','192.168.1.2','192.168.1.3','192.168.1.4','192.168.1.4','192.168.1.4']

window = 4
treshhold = 3

# number of occurences in the window each of ip from current window 
ip_occurrences = {}

for i in ips[0:window]:
	ip_occurrences[i] = ip_occurrences.get(i, 0) + 1

[print(k) for k,v in ip_occurrences.items() if v >= treshhold]

for idx in range(window, len(ips)):
	# decrease number of occurences of first elem in current window
	ip_occurrences[ips[idx - window]] -= 1

	# just give it an alias 
	ip = ips[idx]

	if ip in ip_occurrences.keys():
		ip_occurrences[ip] += 1
	else:
		ip_occurrences[ip] = 1

	if ip_occurrences[ip] >= treshhold:
		print(ip)		
