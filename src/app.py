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
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)