from flask import Blueprint, render_template

bp = Blueprint('artistas', __name__, url_prefix='/artistas')
from musica.db import get_db

@bp.route('/')
def artista():
    db = get_db()
    artistas = db.execute(
        'SELECT Name'
        ' FROM artists '
        ' ORDER BY Name ASC'
    ).fetchall()
    return render_template('artista.html', artistas=artistas)

