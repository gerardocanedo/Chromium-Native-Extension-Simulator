from subprocess import Popen, PIPE
import struct

class ChromiumNativeExtensionSimulator:

    def __init__(self):
        self.proc = None

    def connect(self,cmd,cwd=None):
        self.proc = Popen(cmd, stderr=PIPE, stdout=PIPE, stdin=PIPE, cwd=cwd)   

    def disconnect(self):
        self.proc.kill()

    def send(self, message):
        # Write message size.
        lenght = struct.pack('I', len(message))
        self.proc.stdin.write(lenght)
        # Write the message itself.
        self.proc.stdin.write(message.encode())
        self.proc.stdin.flush()

    def receive(self):
        # Read the message length (first 4 bytes).
        text_length_bytes = self.proc.stdout.read(4)

        if len(text_length_bytes) == 0:
            # empty string
            return ''
        # Unpack message length as 4 byte integer.
        text_length = struct.unpack('i', text_length_bytes)[0]
        # Read the text (JSON object) of the message.
        text = self.proc.stdout.read(text_length).decode()
        return text