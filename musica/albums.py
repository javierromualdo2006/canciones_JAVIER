
from flask import Blueprint, render_template

bp = Blueprint('albums', __name__, url_prefix='/albums')
from musica.db import get_db

@bp.route('/albums')
def albums():
    db = get_db()
    albums = db.execute(
        'SELECT Title'
        ' FROM albums '
        ' ORDER BY Title ASC'
    ).fetchall()
    return render_template('albums.html', albums=albums)