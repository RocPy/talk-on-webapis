import flask
import books
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return """<h1>Distant Reading Archive</h1>
    <p>This site is a prototype API for distant reading of 
       science fiction novels.</p>"""

@app.route("/api/v1/resources/books/all", methods=["GET"])
def api_all():
    return jsonify(books.books)


@app.route("/api/v1/resources/books/", methods=["GET"])
def api_id():
    # Check if an ID was provided as part of the URL
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser
    if 'id' in request.args:
        _id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id.", 500

    results = []

    for liber in books.books:
        if liber['id'] == _id:
            results.append(liber)
            break

    return jsonify(results)


app.run()
