#!~/anaconda3/envs/mega/bin/python
from app import create_app, db
from app.models import Eda

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Eda': Eda}



