import socket # simple, but powerfrul socket library
import threading # library to create threads

# defining host and port
host_ip = '127.0.0.1' # local machine ip here, but if you're in a domain or something like that put the ip here
port = 5555 # this is a port that uses tcp and this is why it was chosen, tcp makes possible for hosts to exchange packets of data

# defining the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET means that we're creating a internet socket that is ipv4, SOCK_STREAM means that is a tcp socket
server.bind(host_ip, port) # assigning the ip and the port to the server socket
server.listen()

