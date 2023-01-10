from app import app
from flask import render_template

@app.route('/')
def hello_world():
    singers = ['Nina Simone', 'Joni Mitchell', 'Georgia Ann Muldrow', 'Dolly Parton', 'Billie Holiday']
    return render_template('index.html', name='Matty', singers=singers)

@app.route('/posts')
def posts():
    return 'These are the posts'

@app.route('/home')
def home_index():
    return render_template ('home_index.html')

@app.route('/favorites')
def favorite_lady_singers():
    singers = ['Nina Simone', 'Joni Mitchell', 'Georgia Ann Muldrow', 'Dolly Parton', 'Billie Holiday']
    return render_template('favorites.html', singers=singers)

