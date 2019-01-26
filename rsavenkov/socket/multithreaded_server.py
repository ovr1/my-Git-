import socket
import _thread as thread

'''
������� ������� ��������� ������ ���������� � ���������� �����.
�������� �� ���������� ����� ������ � �������� ���. ������ ���� � ���������� � ���������� �������.
��������������� ��� ������� ����� �������� � ����� �� ����������.
'''


def on_new_client(connection, address):
    while True:
        message = connection.recv(1024).decode()
        if not message:
            break
        print("From {} >> {}".format(address, message))

        response = input(" ? ")
        connection.send(response.encode())
    # ��������� ����������
    connection.close()


# ������� ��������� �����
mySocket = socket.socket()
# ����������� ��� � ����� � �����
mySocket.bind(('192.168.43.164', 5001))

# �������� ������� �������� ����������, �� 5 ����
mySocket.listen(5)

# � ����������� ����� ���� ����������� �� ���� �� ������ .accept()
# ��� ������ � ��� ���-�� ��������, �� ���������� ���������� �������� �� ����� ��������� ����� �����
# ����� ������� ������ ����� ������ �� ���� ����� ������������� � ��������� ������
while True:
    connection, address = mySocket.accept()
    thread.start_new_thread(on_new_client, (connection, address))

# ��������� ��������� �����
mySocket.close()
