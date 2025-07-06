from flask import Flask, request, jsonify
import re
from  flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
@app.route('/calc', methods=['POST'])
def calculate():
    data = request.get_json()

    a = data.get("a")
    b = data.get("b")
    operation = data.get("operation")

    if a is None or b is None or operation is None:
        return jsonify({"error": "Missing input values"}), 400
    
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400
    
    try:
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                return jsonify({"error": "Division by zero not allowed"}), 400
            result = a / b
        else:
            return jsonify({"error": "Invalid operation"}), 400
        
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 

@app.route('/evaluate', methods=['POST'])
def evaluate():
    txt = request.get_json()

    expression = txt.get("expression")

    if not expression:
        return jsonify({"error": "Missing input"}), 400

    if not re.match(r'^[0-9+\-*/(). ]+$', expression):
        return jsonify({"error": "invalid characters"}), 400
    
    expression = expression.replace(",", ".")
    
    try:
        result = eval(expression)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": "Invalid expression"}), 400
    
@app.route("/")
def index():
    return "Backend is running"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)