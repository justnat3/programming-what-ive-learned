import socket
import tkinter

def CheckPort(host, port):\
    # Create a socket

    s=socket.socket()
    try:
        s.connect ((host, port))
    except:
        return True
    else:
        return False


# Host Portion

host = input('Enter a Host: ')

print('Scanning....')

try:
    for port in [7,20,21,22,23,26,43,53,69,79,80,88,107,115,118,156,389,443,464,513,547,902]:
        if CheckPort(host, port):
            print(f'{host}:{port} is open')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    else:
        print(f'{host}:{port} is closed')
except ValueError:
    print(ValueError)

print('')

print('Scan Finished...')

print('')

input('Hit enter to exit:')