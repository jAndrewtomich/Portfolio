#!/home/andrew/anaconda3/envs/mega/bin/python 
import unittest
from app import create_app, db
from app.models import Eda
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class EdaBlockCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_text(self):
        # create project text
        t1 = Eda(text="test text 1")
        db.session.add(t1)
        db.session.commit()

    def test_iframe(self):
        # create project iframe entry
        f1 = Eda(source="https://jovian.ai/embed?url=https://jovian.ai/jandrewtomich/netflix-eda-feature-engineering-w-imdb-ratings/v/2&cellId=3", height="443")
        db.session.add(f1)
        db.session.commit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
