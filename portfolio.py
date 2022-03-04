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

@app.route('/flights')
def flights():
    return render_template('flights.html', title="Flight Notifications")


@app.route('/hn')
def hn():
    return render_template('hackernews.html', title="News Summarization")