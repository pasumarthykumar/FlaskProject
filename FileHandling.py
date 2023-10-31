from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define the folder for uploaded files
UPLOAD_FOLDER = 'C:/Project/myflaskapp/Uploads'  # Create a folder named 'uploads' in your project's directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define a set of allowed file extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Maximum file size (in bytes)
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'photo' not in request.files:
            return jsonify({'message': 'No file part'}), 400

        photo = request.files['photo']
        if photo.filename == '':
            return jsonify({'message': 'No file selected'}), 400

        if not allowed_file(photo.filename):
            return jsonify({'message': 'File type not allowed'}), 400

        if len(photo.read()) > MAX_FILE_SIZE:
            return jsonify({'message': 'File size exceeds the limit'}), 400

        filename = secure_filename(photo.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(filepath)

        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
