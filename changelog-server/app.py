from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/parameters', methods=['GET'])
def fetch_data():
    user = request.args['user']
    repo = request.args['repo']

    #create directory and then the latest file in it
    directory = f'./data/{user}/{repo}/'
    files = [os.path.join(directory, x) for x in os.listdir(directory) if x.endswith(".txt")]
    newest = max(files, key = os.path.getctime)

    # read the file
    lines = []
    with open(newest, 'r') as fp:
        lines = [line for line in fp]

    return jsonify(
        {"user": f"{user}",
         "logs": f"{lines}",
         "repo": f"{repo}",
         "file": f"{newest}",
         })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')