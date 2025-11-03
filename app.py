from flask import Flask, jsonify
import os

app = Flask(__name__)

def get_secret(secret_name):
    "Read Docker Secrets from file"
    secret_path = f'/run/secrets/{secret_name}'
    if os.path.exists(secret_path):
        with open(secret_path, 'r') as f:
            return f.read().strip()
    #if path doesn't exists
    return os.getenv('APP_SECRET', 'no_secret_set')

@app.route('/')
def home():
    secret = get_secret('app_secret')
    return jsonify({
        "message" : "Hi from Application!!",
        "secret" : secret,
        "version" : "1.0"
    })

@app.route('/health')
def health():
    return jsonify({
        "status" : "healthy"
    })

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5000)
    