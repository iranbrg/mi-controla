import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'eb454e679befdf7e65c62a77137c0725'
app.config['UPLOADED_IMAGES_DEST'] = os.path.join(os.path.dirname(app.instance_path), "backend", "static", "images", "produtos")

from backend import views