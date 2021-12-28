from flask import render_template
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title="Andrew's Page")


@bp.route('/about')
def about():
    return render_template('about.html', title="About Andrew")


@bp.route('/thoughts')
def thoughts():
    return render_template('thoughts.html', title="Andrew's Thoughts")


@bp.route('/projects')
def projects():
   return render_template("projects.html", title="Projects")


@bp.route('/eda')
def eda():
    #blocks = Eda.query.all()
    #return render_template('eda.html', blocks=blocks, title="Netflix and IMDb EDA")
    return render_template('eda.html', title="Netflix and IMDb EDA")


@bp.route('/flights')
def flights():
    return render_template('flights.html', title="Flight Notifications")


@bp.route('/hn')
def hn():
    return render_template('hackernews.html', title="News Summarization")