# import os
# print(f"[INFO] Environment: {os.environ}")
# github.com/Nabil-Abdullahi/GATest
from flask import Flask, make_response, request
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
password="127386328297317-39139074309-391070397409"
access_token="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"

app = Flask("Leak password")

@app.route('/')
def index():
    password = request.args.get("password")
    return password
