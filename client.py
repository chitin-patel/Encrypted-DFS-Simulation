import socket

def main():

    HOST = socket.gethostbyname('localhost')
    PORT = 9090

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((HOST, PORT))

    socket.send('Hello Geetha'.encode('utf-8'))
    print(socket.recv(1024).decode('utf-8'))


    while True:
        print("Hello..")
        client_message = input("Enter the command you want to perform: ")
        client_message_0 = client_message.split()[0]
        if client_message_0 == "ls":
            pass
        if client_message_0 == "create":
            pass
        if client_message_0 == "delete":
            pass
        if client_message_0 == "read":
            pass
        if client_message_0 == "write":
            pass
        if client_message_0 == "rename":
            pass
        if client_message_0 == "cd":
            pass
        if client_message_0 == "mkdir":
            pass


if __name__ == "__main__":
    main()
