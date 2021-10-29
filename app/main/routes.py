import os
from flask import render_template, url_for, current_app
from app.main import bp
from app import db
from app.models import Eda


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/eda')
def eda():
    blocks = Eda.query.all()
    return render_template('eda.html', blocks=blocks)


