import aiorun
import hl7
from hl7.mllp import open_hl7_connection
import os
from hl7.client import MLLPClient, mllp_send

server = "10.229.11.48"
port = 20003


def send_message(server, port):
    client = MLLPClient(server, port)


    f = open('test.dat', 'r')
    ff = f.read()

    messages = hl7.parse_batch(ff)

    for message in messages:

        client.send_message(str(message))

if __name__ == '__main__':
    send_message(server, port)