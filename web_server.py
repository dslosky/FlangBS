from flask import Flask, render_template, url_for, request, session, flash, redirect, send_file, send_from_directory, Response, jsonify
import os, sys

def web_path():
    path = os.path.dirname(os.path.abspath(__file__))
    path = path.split(os.sep)
    directory = os.path.normpath(os.sep.join(path))
    return directory

BASE_DIR = os.path.join(web_path(), 'view')
STATIC_DIR = os.path.join(web_path(),'view','static')
app = Flask(__name__,
            template_folder=BASE_DIR,
            static_folder=STATIC_DIR)

################################ Login ################################

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

# send Angular 2 files
@app.route('/<path:filename>')
def client_app_angular2_folder(filename):
    return send_from_directory(os.path.join(BASE_DIR), filename)

@app.route('/')
def index():
    return render_template('index.html')

def start(port=80):
    app.run(host='0.0.0.0', port=port, threaded=True)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            # run in debug mode
            app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    else:
        start()