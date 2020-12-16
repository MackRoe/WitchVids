from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='WitchVids Coming Soon!!')

playlists = [
    { 'title': 'Intro To Witchcraft', 'description': 'Basic Introduction & Overview' },
    { 'title': 'Pagan Comedy', 'description': 'By Pagans, For Pagans' }
]

@app.route('/playlists')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)

if __name__ == '__main__':
    app.run(debug=True)
