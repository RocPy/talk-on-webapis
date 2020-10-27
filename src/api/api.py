import flask
import books
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse

app = flask.Flask(__name__)
api = Api(app)

app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return """<h1>Distant Reading Archive</h1>
    <p>This site is a prototype API for distant reading of 
       science fiction novels.</p>"""

parser = reqparse.RequestParser()
parser.add_argument('task')

class Library(Resource):
    def get(self, _id=None):
        if _id:
            results = []
            for liber in books.books:
                if liber['id'] == int(_id):
                    results.append(liber)
                    break
            return results
        else:
            return books.books

    def put(self, _id=None):
        _id = int(_id)
        json_data = request.get_json(force=True)
        if _id:
            for liber in books.books:
                if liber['id'] == _id:
                    print(json_data)
                    print(liber)
                    liber['id'] = int(json_data['new_id'])
                    break

api.add_resource(Library,
                 '/api/v1/resources/books/',
                 '/api/v1/resources/books/<_id>')

app.run()
