from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/tools', methods=['GET'])
def get_tools():
    tools = [
        {"name": "Carving Knife", "use": "For shaping and detailing wood"},
        {"name": "Gouge", "use": "For scooping out wood"},
        {"name": "Chisel", "use": "For cutting straight lines"}
    ]
    return jsonify(tools)

@app.route('/api/safety', methods=['GET'])
def get_safety():
    tips = [
        {"tip": "Wear gloves", "description": "Protect hands from cuts"},
        {"tip": "Use a clamp", "description": "Secure wood to prevent slipping"}
    ]
    return jsonify(tips)

@app.route('/api/test', methods=['GET'])
def get_test():
    tips = [
        {"tip": "testsss", "description": "test3"},
    ]
    return jsonify(tips)

if __name__ == '__main__':
    app.run(port=5000)