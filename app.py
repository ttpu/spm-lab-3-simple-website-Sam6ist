from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!doctype html>
    <html lang="uz">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Bosh sahifa</title>
    </head>
    <body>
        <h1>Bosh sahifaga xush kelibsiz!</h1>
        <a href="/content"><button>Kontent sahifasiga o'tish</button></a>
    </body>
    </html>'''

@app.route('/content')
def content():
    return '''<!doctype html>
    <html lang="uz">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Kontent sahifasi</title>
    </head>
    <body>
        <h1>Bu kontent sahifasi!</h1>
        <a href="/"><button>Bosh sahifaga qaytish</button></a>
    </body>
    </html>'''

if __name__ == '__main__':
    app.run(debug=True, port=5001)
