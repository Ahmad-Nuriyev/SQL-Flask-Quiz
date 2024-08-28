from flask import render_template, request

from app import app
from models import *
from extensions import db


@app.route('/movies/', methods=['GET'])
def movies():
    movie = Movie.query.all()
    return render_template ('index.html', movie=movie)

@app.route('/movies/<int:id>/', methods=['GET', 'POST'])
def movie(id):
    movie = Movie.query.get(id)
    message = None
    if movie is None:
        message = " Movie is not found"
    return render_template ('movie.html', movie=movie, message=message)
