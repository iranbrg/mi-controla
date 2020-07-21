from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'eb454e679befdf7e65c62a77137c0725'

from backend import views