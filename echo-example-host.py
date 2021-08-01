# This is incluided as an example for the user to understand the communication
# If you are interested in this example, you should check
# https://github.com/GoogleChrome/chrome-extensions-samples/blob/main/mv2-archive/api/nativeMessaging/host/native-messaging-example-host

import struct
import sys

def send_message(message):
    bytesize= struct.pack('I', len(message))
    sys.stdout.buffer.write(bytesize)
    sys.stdout.buffer.write(message.encode())
    sys.stdout.flush()

while True:
    text_length_bytes = sys.stdin.buffer.read(4)

    if len(text_length_bytes) == 0:
        sys.exit(0)

    text_length = struct.unpack('i', text_length_bytes)[0]
    text = sys.stdin.read(text_length)
    send_message('{"echo": '+text+'}')
