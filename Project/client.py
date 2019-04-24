# Project/server/hole_punching/rendez_vous.py

"""
    UDP client.
        1) Run server.py script (UDP server)
        2) Run this script
        2) Run this script on another computer
        4) You should see server response message on both clients
        5) You should see client talking to each other
"""

import socket
import pickle
from threading import Timer
from typing import Tuple, List


def close_socket(mutableBool):
    del mutableBool[0]


def spam_clients(sock: socket.socket, other_clients: List[Tuple[str, int]]):
    # Only other clients should arrive here
    for client in other_clients:
        for x in range(10):
            # Spam them
            msg = "{0} send to {2}, try={1}".format(sock.getsockname(), x, client)
            sock.sendto(msg.encode(), client)


if __name__ == '__main__':
    isRunning = [True]  # Mutable trick / hack ...
    other_clients = []
    message = 'UnrealHost dispo for a game !'.encode()
    timer = Timer(20.0, close_socket, kwargs=dict(mutableBool=isRunning))

    server_address = ('localhost', 5000)  # LAN (same computer)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Bind to any IP with dynamic port
        # Works with or without it (default to localhost and dynamic IP)
        # sock.bind(('', 0))

        # To avoid waiting forever
        sock.settimeout(3)

        print("Server addr = {0}:{1}".format(server_address[0], server_address[1]))
        print('---------------\n')

        # Send a fake message to test server response
        sent = sock.sendto(message, server_address)
        print("Current interface: {0}:{1}".format(*sock.getsockname()))
        print('---------------\n')

        # Keep client up and running a certain time
        timer.start()
        try:
            while isRunning:
                # Check response
                msg, addr = sock.recvfrom(4096)
                print("Current interface: {0}:{1}".format(*sock.getsockname()))
                print(addr, server_address)

                if (addr[1] == server_address[1]):
                    print("SERVER ::: From dedicated server !")
                    new_client = pickle.loads(msg)
                    print(new_client)
                    # Keep track of all clients except yourself
                    if (new_client != sock.getsockname() and new_client not in other_clients):
                        other_clients.append(new_client)
                        print(other_clients)
                    # Spam them all
                    spam_clients(sock, other_clients)
                else:
                    print("CLIENT ::: A client made contact, praise the sun !")
                    print(msg.decode(), addr)
                print('---------------\n')
        except socket.error as err:
            if (err == socket.timeout):
                timer.cancel()
