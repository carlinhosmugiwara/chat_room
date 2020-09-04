import socket
import threading

username = input("Choose your username: ")
user = socket.socket(sokcet.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 55555 
user.connect((ip, port))

# defining the function to receive the user's data 
def receive():
  while True:
    try:
      msg = user.recv(2048).decode('ascii')
      if(msg == 'USER_NAME':
        user.send(username.encode('ascii'))
      else:
        print(msg)
    except:
      print("Something went wrong")
      user.close()
      break

# defining the function to enable the user to send new messages
def new_message():
  while True:
    msg = f'{username}: {input("")}'
    user.send(msg.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

new_message_thread = threading.Thread(target=new_message)
new_message_thread.start()
