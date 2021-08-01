#!/bin/python3

from subprocess import Popen, PIPE
from ChromiumNativeExtensionSimulator import ChromiumNativeExtensionSimulator
import os

simulator = ChromiumNativeExtensionSimulator()
simulator.connect(['python3','echo-example-host.py'],cwd='.')
print(f'PID: {simulator.proc.pid}')

message= '{"message":"eyJ0ZXh0IjoidGVzdENvbm5lY3Rpb24ifQ=="}'
print(f'Sending {message}')
simulator.send(message)

response = simulator.receive()
print(f'Receiving {response}')

simulator.disconnect()
print(f'Native APP Destroyed')