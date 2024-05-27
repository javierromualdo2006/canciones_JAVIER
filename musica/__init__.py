from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
   from . import db
   db.init_app(app)

@app.route('/')
def hello():
    return app

from . import artistas
app.register_blueprint(artistas.bp)

from . import albums
app.register_blueprint(albums.bp)

from . import canciones
app.register_blueprint(canciones.bp)

from . import generos
app.register_blueprint(generos.bp)