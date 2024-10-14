from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/parameters', methods=['GET'])
def fetch_data():
    try:
        user = request.args['user']
        repo = request.args['repo']

        #create directory and then the latest file in it
        directory = f'./data/{user}/{repo}/'
        files = [os.path.join(directory, x) for x in os.listdir(directory) if x.endswith(".txt")]
        newest = max(files, key = os.path.getctime)

        # read the file
        changeLines = ""
        with open(newest, 'r') as fp:
            changeLines = [line for line in fp]

        lines = "\n".join(changeLines)

    except Exception as exc:
        print(exc)
        newest, lines = None, "No change logs were returned"

    return jsonify(
        {"user": f"{user}",
         "logs": f"{lines}",
         "repo": f"{repo}",
         "file": f"{newest}",
         })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')