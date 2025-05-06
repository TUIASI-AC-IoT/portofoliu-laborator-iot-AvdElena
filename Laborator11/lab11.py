import os
import uuid
from flask import Flask, jsonify, request
app = Flask(__name__)
dir_path = "dir"
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dirList", methods=['GET'])
def list_files():
    return jsonify(os.listdir(dir_path))

@app.route("/fileList/<filename>", methods=['GET'])
def read_file(filename):
    file_path = os.path.join(dir_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            return f.read(), 200
    return jsonify({'error': 'File not found'}), 404

@app.route('/fileCreate', methods=['POST'])
def create_file():
    data = request.get_json()
    filename = data['filename']
    content = data['content']
    
    if not filename:
        return jsonify({'error': 'Filename required'}), 400

    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return jsonify({'message': f'File {filename} created successfully'}), 201

@app.route('/fileAutoCreate', methods=['POST'])
def auto_create_file():
    data = request.get_json()
    content = data['content']
    
    filename = f"file{uuid.uuid4().hex}.txt"

    if not filename:
        return jsonify({'error': 'Filename required'}), 400

    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return jsonify({'message': f'File {filename} created successfully'}), 201

@app.route('/fileDelete/<filename>', methods=['DELETE'])
def delete_file(filename):
    filepath = os.path.join(dir_path, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)
        return jsonify({'message': f'File {filename} deleted'}), 200
    return jsonify({'error': 'File not found'}), 404

@app.route('/fileModify/<filename>', methods=['PUT'])
def modify_file(filename):
    data = request.get_json()
    content = data['content']

    filepath = os.path.join(dir_path, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'w') as f:
            f.write(content)
        return jsonify({'message': f'File {filename} modified'}), 200
    return jsonify({'error': 'File not found'}), 404

if __name__ == "__main__":
    app.run()