from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token
)
from main import main

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'randomSecretAiSquareConnect'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
jwt = JWTManager(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def home():
    return 'Hello World!', 200


# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'user' or password != 'password': # Hardcoded login for POC
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/processing', methods=['POST'])
@jwt_required
def processing():
    # Access the identity of the current user with get_jwt_identity
    file = request.files['process_file']
    if file:
        file.stream.seek(0)
        try:
            id = main(file)
        except Exception as e:
            error = str(e)
            return jsonify(response=error), 400
    return jsonify(processing_id=id), 200


@app.route('/processing/image/<processingId>', methods=['GET'])
def get_processed_image(processingId):
    img_file_name = processingId + '.png'
    return send_file(img_file_name, mimetype='image/png', attachment_filename='output.png', as_attachment=True)


@app.route('/processing/csv/<processingId>', methods=['GET'])
def get_processed_csv(processingId):
    csv_file_name = processingId + '.csv'
    return send_file(csv_file_name, mimetype='text/csv', attachment_filename='output.csv', as_attachment=True)