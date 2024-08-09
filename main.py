from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # print("Полученные данные:", data)
    return jsonify({'status': 'success', 'message': 'Данные получены!'}), 200

if __name__ == '__main__':
    app.run()
