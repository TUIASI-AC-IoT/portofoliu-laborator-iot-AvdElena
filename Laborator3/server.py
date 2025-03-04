import io
from flask import Flask, send_file, jsonify
import os.path

app = Flask(__name__)

@app.route('/firmware.bin')
def firm():
    with open(".pio\\build\\esp-wrover-kit\\firmware.bin", 'rb') as bites:
        print(bites)
        return send_file(
                     io.BytesIO(bites.read()),
                     mimetype='application/octet-stream'
               )

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/version")
def version():
    version_file_path = "include/version.h"
    if os.path.exists(version_file_path):
        with open(version_file_path, 'r') as f:
            version_data = f.read()
        return version_data, 200
    else:
        return jsonify({"error": "Version file not found!"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context=('ca_cert.pem', 'ca_key.pem'), debug=True)