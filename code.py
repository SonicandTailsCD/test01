import base64

base64_message = 'U29uaWNhbmRUYWlsc0NEJ3MgZmF0LiBBbHNvLCB5b3UgbWF5IGJlIGZhdCB0b28hIFdoaWNoLCBvZiBjb3Vyc2UsIHlvdSB3aWxsIGJlIGZhdCBzb29uIDop'
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)
