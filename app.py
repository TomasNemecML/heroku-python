from crypt import methods
from flask import Flask, render_template, request
from pythonScripts.alzaScraper import getPriceAlza

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/alza', methods=["GET"])
def alza():
    print(request.args.get("link"))
    return "success"



# @app.route("/", subdomain="api")
# def api():
#     return "api"

if __name__ == '__main__':
    # app.config['SERVER_NAME'] = "test.abc"
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=80)
    app.run(debug=True, port=80, host="0.0.0.0")

