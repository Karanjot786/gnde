from flask import Flask, request, jsonify
from flask.templating import render_template
from inshort import getNews
from flask_cors import CORS
from pygments.formatters import HtmlFormatter
import os

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        return jsonify(getNews(request.form['category']))
    elif request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(port = int(os.environ.get('PORT', 5000)),threaded=True)
