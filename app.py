from crypt import methods
from flask import Flask, render_template, request
from pythonScripts.alzaScraper import getPriceAlza
from pythonScripts.amazonScraper import getPriceAmazon
from pythonScripts.webScraperByClass import getPrice

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/getprice")
def getprice():
    link = request.args.get("link")
    tag = request.args.get("tag")
    classToSearch = request.args.get("class")
    return f"{getPrice(str(link), classToSearch, tag)}"


@app.route('/alza', methods=["GET"])
def alza():
    link = request.args.get("link")
    return f"{getPriceAlza(str(link))}"


@app.route('/amazon', methods=["GET"])
def amazon():
    link = request.args.get("link")
    return f"{getPriceAmazon(str(link))}"


# debug ednpoint
@app.route("/debug", methods=["GET"])



# @app.route("/", subdomain="api")
# def api():
#     return "api"

if __name__ == '__main__':
    # app.config['SERVER_NAME'] = "test.abc"
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=80)
    app.run(debug=True, port=80, host="0.0.0.0")

