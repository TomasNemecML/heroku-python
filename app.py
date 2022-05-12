from flask import Flask, render_template, request

from pythonScripts.alzaScraper import getPriceAlza
from pythonScripts.webScraperByClass import getPrice
from pythonScripts.debug import getPage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/bestprice')
def bestprice():
    
    
    return "best price"

    

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



# debug ednpoint
@app.route("/debug", methods=["GET"])
def debug():
    link = request.args.get("link")
    return getPage(link)


if __name__ == '__main__':
    # app.config['SERVER_NAME'] = "test.abc"
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=80)
    app.run(debug=True, port=80, host="0.0.0.0")

