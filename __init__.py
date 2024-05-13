from flask import Flask

def create_app():

    app = Flask(__name__)

    from flask import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

@app.route('/')
def hello():
    return app

with app.app_context():
   from . import db
   db.init_app(app)





