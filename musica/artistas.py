from flask import Blueprint, render_template, request, redirect, url_for
from musica.db import get_db

bp = Blueprint('artistas', __name__, url_prefix='/artistas')


@bp.route('/')
def artista():
    db = get_db()
    artistas = db.execute(
        'SELECT Name'
        ' FROM artists '
        ' ORDER BY Name ASC'
    ).fetchall()
    return render_template('artista.html', artistas=artistas)

@bp.route('/new', methods=('GET', 'POST'))
def nuevo():
    if request.method == 'POST':
        Name = request.form['Name']

        con = db.get_db()
        consulta = """INSERT INTO artists (ArtistId, Name) 
                    VALUES (?, ?)
                    """
        
        con.execute(consulta, (Name))
        con.commit()
        return redirect(url_for('artista.artistas'))
    else:
        pagina = render_template('new_artista.html')
        return pagina

