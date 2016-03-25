import socket as s
from ftplib import FTP

def startServer():

	ServerSocket = s.socket(s.AF_INET,s.SOCK_STREAM)
	ServerSocket.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
	print ServerSocket
	try:
		ServerSocket.bind(('127.0.0.1',7000))
	except:
		print 'BIND ERROR'
		ServerSocket.close()
		try:
			ServerSocket.bind(('127.0.0.1',7000))
			print 'REBIND SUCCESSFUL'
		except:
			print 'REBIND ERROR'

	ServerSocket.listen(1)

	while True:
			client_connection,client_addr = ServerSocket.accept()
			request = client_connection.recv(2048)
			print request
			send_response = """\
			HTTP/1.1 200 OK

			Hello, World!
			"""
			client_connection.sendall(send_response)
			client_connection.close()

if __name__ == '__main__' :

	print 'This is Server 1'

	startServer()