from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Heroku!'

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

if __name__ == '__main__':
    app.run(debug=True)