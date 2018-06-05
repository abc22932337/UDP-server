import socket

bind_ip = "127.0.0.1"
bind_port = 9998

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((bind_ip, bind_port))

print "[*] Listening on %s:%d" %(bind_ip, bind_port)

while True:
	
	data, addr = s.recvfrom(2048)
	if not data:
		
		print "No data."
		break

	print "[*] Received: %s from %s" %(data, addr)

s.close()

