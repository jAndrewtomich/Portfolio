from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Andrew's Page")

@app.route('/eda')
def eda():
    return render_template('eda.html', title="Netflix and IMDb EDA")

@app.route('/nlp')
def nlp():
    return render_template('nlp.html', title="NLP")

@app.route('/walrus')
def walrus():
    return render_template('walrus1.slides.html', title="Walrus")

@app.route('/hn')
def hn():
    return render_template('hackernews.html', title="News Summarization")