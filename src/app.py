from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=["GET"])
def getcode():
    return jsonify({"Hello W0rld": "bbbb4"})

@app.route('/is_prime/<a>', methods=["GET"])
def is_prime(a):
    try:
        a = int(a)
        if a <= 1:
            return "False"

        for i in range (2,(int(a / 2) + 1)):
            if a % i == 0:
                return "False"
        
        return "True"
    except ValueError:
        return "Error"
    
@app.route('/Ascii/<a>', methods=["GET"])
def Ascii(a):
    try:
        a = ord(a)
        return jsonify({"Result is": a})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404

            

@app.route("/plus/<a>/<b>", methods=["GET"])
def plus(a,b):
    try:
        a, b = int(a), int(b)
        return jsonify({"Result is": a+b})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404
    
@app.route("/minus/<a>/<b>", methods=["GET"])
def minus(a,b):
    try:
        a, b = int(a), int(b)
        return jsonify({"Result is": a-b})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404
    
@app.route("/palindrome/<a>", methods=["GET"])
def palindrome(a):
    try:
        a = str(a)
        if a == a[::-1]:
            return "True"
        else:
            return "False"
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404
    
@app.route('/factorial/<a>', methods=["GET"])
def factorial(a):
    try:
        a = int(a)
        if a <= 1:
            return "False"
        ans = 1
        for i in range (2, a + 1):
            ans *= i
        return jsonify({"Result is": ans})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404 
    

@app.route("/samechar/<a>", methods=["GET"])
def samechar(a):
    try:
        character = set(a)
        if len(character) == len(a):
            return "True"
        else:
            return "False"
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404

@app.route('/is_even/<a>', methods=["GET"])
def is_even(a):
    try:
        a = int(a)
        if a <= 1:
            return "False"

        
        if a % 2 == 1:
            return "False"
        
        return "True"
    except ValueError:
        return "Error"

@app.route('/is_odd/<a>', methods=["GET"])
def is_odd(a):
    try:
        a = int(a)
        if a < 1 or a % 2 == 0:
            return "False"
        else:
            return "True"
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404
    

@app.route("/multiple/<a>/<b>", methods=["GET"])
def multiple(a,b):
    try:
        a, b = int(a), int(b)
        return jsonify({"Result is": a*b})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404
    
@app.route("/divide/<a>/<b>")
def divide(a,b):
    try:
        a, b = int(a), int(b)
        if b > 0 :
            return jsonify({"Result is": a/b})
        else:
            return jsonify({"error": "cannot divided by 0"})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)