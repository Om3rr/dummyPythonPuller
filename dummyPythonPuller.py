from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from subprocess import call
app = Flask(__name__)
SECRET = "YourSecret."

@app.route('/getPull', methods = ['GET', 'POST'])
def hello_world():
    print("Cool..")
    call(['bash', 'myUpdateScript.sh'])
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
