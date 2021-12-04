import sys
import argparse

import socket
from select import select

to_monitor = []

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(('localhost', 15000))
server_sock.listen()


def accept_conn(server_sock):
    client_sock, addr = server_sock.accept()
    print('Connect', addr)
    to_monitor.append(client_sock)


def respond(client_sock):
    data = client_sock.recv(4096)

    if data:
        client_sock.send(data.decode().upper().encode())
    else:
        client_sock.close()
        to_monitor.remove(client_sock)


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])  # read, write, err
        for sock in ready_to_read:
            if sock is server_sock:
                accept_conn(sock)
            else:
                respond(sock)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--worker', default=1)
    parser.add_argument('-k', default=1)
    return parser


if __name__ == '__main__':
    # parser = create_parser()
    # namespace = parser.parse_args()
    # print(namespace.worker)

    to_monitor.append(server_sock)
    event_loop()

