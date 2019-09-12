from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/file/intents/', methods=['GET'])
def get_file():
    data = {'type': 'intents', 'format': 'md', 'content': '## intents\n - primeira'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
