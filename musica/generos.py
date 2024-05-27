from flask import Blueprint, render_template

bp = Blueprint('generos', __name__, url_prefix='/generos')
from musica.db import get_db

@bp.route('/')
def generos():
    db = get_db()
    genres = db.execute(
        'SELECT Name'
        ' FROM genres '
        ' ORDER BY Name ASC'
    ).fetchall()
    return render_template('generos.html', genres=genres)
