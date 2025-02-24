from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=["GET"])
def getcode():
    return jsonify({"Hello W0rld": "aaaa4"})

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
            

@app.route("/plus/<a>/<b>", methods=["GET"])
def plus(a,b):
    try:
        a, b = int(a), int(b)
        return jsonify({"Result is": a+b})
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
        return "Error"
        

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)