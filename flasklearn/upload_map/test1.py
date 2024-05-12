from flask import Flask, render_template,request
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = str(uuid.uuid4())+os.path.splitext(file.filename)[1]
        file.save(filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Uploaded successfully'
    else:
        return 'Upload failed'


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.run(debug=True)