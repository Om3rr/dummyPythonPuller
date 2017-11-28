from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from subprocess import call
app = Flask(__name__)
SECRET = "sha1=86262701ee3d6a58a320ebac31bfc7de0cbdf9a4"

@app.route('/getPull', methods = ['GET', 'POST'])
def hello_world():
    if(request.headers.get("X-Hub-Signature") != SECRET):
        return redirect(404)
    else:
        call(['bash','myUpdateScript.sh'])
        return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
