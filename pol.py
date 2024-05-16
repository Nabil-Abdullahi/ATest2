# import os
# print(f"[INFO] Environment: {os.environ}")
# github.com/Nabil-Abdullahi/GATest
from flask import Flask
app = Flask(__name__)


import traceback

def do_computation():
    raise Exception("Secret info")

# BAD
@app.route('/bad')
def server_bad():
    try:
        do_computation()
    except Exception as e:
        return traceback.format_exc()
api_key="127386328297317-39139074309-391070397409"
access_token="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"
print("hello")
d = input((str("Hello: ")))
if type(d) == str:
  for i in range(0, 5):
    print(access_token)
print("hello")
print("hello")
print("hello")
print("hello")
