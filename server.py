import os
import uuid
from flask import Flask, request

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  # this has changed from the original example because the original did not work for me
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route('/image', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        print '**found file', file.filename
        filename = str(uuid.uuid4()) + '.jpg'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # for browser, add 'redirect' function on top of 'url_for'
        return "{ \"message\": \"Successfully uploaded file\"}"