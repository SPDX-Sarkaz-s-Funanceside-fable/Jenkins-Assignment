from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=["GET"])
def getcode():
    return jsonify({"Hello W0rld": "good"})

@app.route("/plus/<a>/<b>", methods=["GET"])
def plus(a,b):
    try:
        a, b = int(a), int(b)
        return jsonify({"Result is": a+b})
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 404 
        

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)