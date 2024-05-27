from flask import Blueprint, render_template

bp = Blueprint('canciones', __name__, url_prefix='/canciones')
from musica.db import get_db

@bp.route('/')
def songs():
    db = get_db()
    canciones = db.execute(
        'SELECT Name'
        ' FROM tracks '
        ' ORDER BY Name ASC'
    ).fetchall()
    return render_template('canciones.html', canciones=canciones)
