from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/json')
def json():
    return {
        "test": "test",
        "list": [1, 2, 3, 5, 8, 13, 21],
        "items": [{
            "name": "item 1",
            "ID": 1
        },
        {
            "name": "item 2",
            "ID": 2
        }]
    }

@app.route('/image')
def image():
    return '<img src="https://tomasnemec.eu/gallery/Memoji transparent .png">'

if __name__ == '__main__':
    app.run(debug=True)
