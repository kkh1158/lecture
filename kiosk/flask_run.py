from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)