from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=["GET"])
def getcode():
    return jsonify({"Hello W0rld": "aaaa4"})

@app.route('/isprime/<a:int>', methods=["GET"])
def getprime(a):
    for i in range (2,(int(a / 2) + 1)):
        if a % i == 0:
            return jsonify({"Result": "Not Prime"})
    
    return jsonify({"Result": "Is Prime"})
            

@app.route("/plus/<a>/<b>", methods=["GET"])
def plus(a,b):
    try:
        a, b = int(a), int(b)
        return jsonify({"Result is": a+b})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404 
        

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)