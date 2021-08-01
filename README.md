# Chromium-Native-Extension-Simulator

I use this simulator to do unary testing over a digital sign native application (multi platform).
Simulating the browser allow me to identify bugs before integration.
A particular annoying one arises from a I/O buffer on a MacOS terminal.
Simulating the browser give me enough information to focus on the extension.

## Chromium Native Extension Simulator for Native apps unit testing

This class was created with the aim of unit testing the I/O Mechanism between Chromium browsers and a java native app

* Instead of usign a browser, this class allows to programm specific flows in testing, and automate its execution.
* Synchronic communication is good enought in my case.
* Messages are encoded and decoded as 'utf-8' by default

## Source Code

* `ChromiumNativeExtensionSimulator.py` contains the Python Class
* `example.py` is a test flow.
* `echo-example-host.py` responses the messages sent. Instead of calling this executable, the Native Application should be called (the same way it's done by the browser)



### API Reference
https://developer.chrome.com/docs/apps/nativeMessaging/

### Reference of a very usefull extension:
https://github.com/GoogleChrome/chrome-extensions-samples/blob/main/mv2-archive/api/nativeMessaging/host/native-messaging-example-host
