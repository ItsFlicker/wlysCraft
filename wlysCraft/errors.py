from flask import render_template

from wlysCraft import app


@app.errorhandler(400)
def bad_request(e):
    return render_template('errors/400.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html')