from flask import Flask, request, jsonify
from flask.templating import render_template
from inshorts import getNews
from flask_cors import CORS
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
from pygments.formatters import HtmlFormatter


app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"])
    formatter = HtmlFormatter(style="emacs",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    
    md_template = md_css_string + md_template_string
    return md_template

@app.route('/news', methods=['GET', 'POST'])

def news():
    if request.method == 'POST':
        return jsonify(getNews(request.form['category']))
    elif request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(port = int(os.environ.get('PORT', 5000)),threaded=True)

