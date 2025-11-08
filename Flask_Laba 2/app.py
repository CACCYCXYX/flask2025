from flask import Flask, render_template, request, redirect, url_for
import hashlib
import uuid
import os
import re

def gen_uuid():
    return str(uuid.uuid4())

app = Flask(__name__)

root = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(root, 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            file_split = file.filename.rsplit('.', 1)
            print(file_split)
            uuid_filename = gen_uuid()
            fn_extension = str(file_split[-1])
            uuid_filename_full = uuid_filename + '.' + fn_extension
            file_save_path = os.path.join(app.config['UPLOAD_FOLDER'], uuid_filename_full)
            file.save(file_save_path)
            return 'File successfully uploaded'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)