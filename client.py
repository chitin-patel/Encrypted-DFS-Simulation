import socket

def send_to_server(message):
    # HOST = '10.200.137.77'
    # HOST = socket.gethostbyname(socket.gethostname())
    host = socket.gethostbyname('localhost')
    port = 9090
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.connect((host, port))
    s_socket.send(message.encode('utf-8'))
    message_recv_from_server = None
    if (message.split('|')[0] in ["ls"]) or (
            message.split(' ')[0] in ["create", "read", "cd", "delete", "mkdir", "write", "rename"]):
        message_recv_from_server = s_socket.recv(1024)
    s_socket.close()
    return message_recv_from_server

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
        message_recv_from_server = send_to_server(client_message)
        client_message_0 = client_message.split()[0]
        if client_message_0 == "ls":
            pass
        if client_message_0 == "create":
            print(message_recv_from_server)
        if client_message_0 == "delete":
            pass
        if client_message_0 == "read":
            pass
        if client_message_0 == "write":
            content = input()
            message_recv_from_server = send_to_server(content)
            print(message_recv_from_server)
        if client_message_0 == "rename":
            pass
        if client_message_0 == "cd":
            pass
        if client_message_0 == "mkdir":
            pass


if __name__ == "__main__":
    main()
