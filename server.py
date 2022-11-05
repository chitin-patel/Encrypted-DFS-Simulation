import socket
import os

def send_response_to_client(data, communication_socket):
    communication_socket.send(data.encode('utf-8'))

def listing_files_in_folder():
    directory_path = "."

    existing_files = [file for file in os.listdir(directory_path) if os.path.isfile(file) or os.path.isdir(file)]

    file_list = ""
    for file in existing_files:
        file_list += file + "\n"
    return file_list

def creating_file(wanted_filename, communication_socket, client_address):
    # content = write(filename, communication_socket, server, current_dir)

    if wanted_filename not in (listing_files_in_folder()):
        with open(wanted_filename, "w") as f:
            print("Created the file in Server 1")
            data = "Created the file in Server 1"
            send_response_to_client(data, communication_socket)
    else:
        data = "File already exist"
        send_response_to_client(data, communication_socket)
    communication_socket.close()
    print(f'Communication with {client_address} ended!')


def main():

    host = socket.gethostbyname('localhost')
    # host = '130.85.243.2'
    port = 9090
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((host, port))
    s_socket.listen(5)
    main_dir = os.getcwd()
    print('Server 1 is listening!......')

    while True:
        communication_socket, client_address = s_socket.accept()
        print(f'Connected to {client_address}')
        # getting username
        # getting password
        # authorizing the client or users
        # users exist? or else create new directory

        print("Processing the message received from client...")
        client_message = communication_socket.recv(1024).decode('utf-8')
        print(f'Message from client is: {client_message}')

        client_message_0 = client_message.split()[0]
        if len(client_message.split()) > 1:
            wanted_filename = client_message.split()[1]

        if client_message_0 == "create":
            creating_file(wanted_filename, communication_socket, client_address)

if __name__ == "__main__":
    main()
