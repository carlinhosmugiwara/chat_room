import socket # simple, but powerfrul socket library
import threading # library to create threads

# defining host and port
host_ip = '127.0.0.1' # local machine ip here, but if you're in a domain or something like that put the ip here
port = 5555 # this is a port that uses tcp and this is why it was chosen, tcp makes possible for users and host to exchange packets of data

# defining the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET means that we're creating a internet socket that is ipv4, SOCK_STREAM means that is a tcp socket
server.bind(host_ip, port) # assigning the ip and the port to the server socket
server.listen()

# defining users and their usernames
users = []
usernames = []

# defining the function that'll enable a user to send a message to all other users
def message_to_all(msg):
  for user in users:
    user.send(msg)

# defining the function that'll handle the users making possible for them to send messages or get out of the chat room
def handle_users(user):
  while True: # endless loop
    try:
      msg = user.recv(2048) # receiving the data from the socket with buffsize of 2^11 = 2048
      message_to_all(msg)
    except:
      # removing user
      user_index = users.index(user)
      users.remove(user)
      user.close()
      username = usernames[user_index]
      message_to_all(f'{username} has left the chat'.encode('ascii'))
      usernames.remove(username)
      break
# defining function that'll receive the new users      
def receive():
  while True:
    user, address = server.accept()
    print(f"Connected with {str(address)}") # this part is gonna be seing only by the administrator of the server
    user.send('USER_NAME'.encode('ascii))
    username = user.recv(2048).decode('ascii') # receiving the username
    usernames.append(username) # appending it to the list of usernames
    users.append(user) # appending it to the list of users
    print(f"Username of the user is {username}") # this part is also gonna be seing only by the administrator
    message_to_all(f'{username} has joined the chat, show how awesome this is'.encode('ascii'))
    user.send('Connected successfully to the server'.encode('ascii'))
   
    # defining the thread
    thread = threading.Thread(target=handle_users, args=(user,)) # putting the target function and it's argument
    thread.start()
                      
# calling the receive function
receive()
