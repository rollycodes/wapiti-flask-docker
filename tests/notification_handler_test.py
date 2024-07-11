from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notification', methods=['POST'])
def notification():
    data = request.json
    print("Notification received:", data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5001)
