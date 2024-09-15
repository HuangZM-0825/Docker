from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square', methods=['POST'])
def square():
    data = request.get_json()
    number = data.get('number')
    if number is not None:
        return jsonify({'result': number ** 2})
    else:
        return jsonify({'error': 'No number provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
