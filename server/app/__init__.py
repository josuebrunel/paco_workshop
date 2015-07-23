import os
import pdb
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/yosuke/workspace/paco/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return "Working"

@app.route('/upload_file', methods = ['GET','POST'])
def upload_file():

    if request.method == 'POST':
        fname = request.files['filename']
        if fname :
            file_name = secure_filename(fname.filename)
            path_location = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            fname.save(path_location)
            print("File {0} uploaded successfully".format(file_name))
            return "File uploaded OK"
    else:
        print("{0} is not a valid method for this resource".format(request.method))
        return "Invalid method"
