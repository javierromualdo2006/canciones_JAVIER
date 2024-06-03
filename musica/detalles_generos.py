@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consultal = """
        SELECT Name FROM genres WHERE GenreId = ?
    """
    consultal2 = """
        SELECT t.Name, g.Name FROM genres g JOIN tracks t ON t.GenreId = g.GenreId
        JOIN film f ON fa.film_id = f.film_id
        WHERE a.actor_id = ?:
    """

    res = con.execute(consultal, (id,))
    genero = res.fetchone()
    res = con.execute(consultal2, (id,))
    lista_tracks = res.fetchone()
    pagina = render_template('detalle_generos.html',
                             genero=genero,
                             canciones=lista_tracks)
    return pagina