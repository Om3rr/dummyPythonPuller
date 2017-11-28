from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack

app = Flask(__name__)


@app.route('/getPull')
def hello_world():
    print(request.data)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
