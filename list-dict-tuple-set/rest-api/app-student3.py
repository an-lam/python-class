from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {'student': name}

# No need to do @app.route like previous example
api.add_resource(Student, '/student/<string:name>') # http://127.0.0.1:5000/student/Mickey

app.run(port=5000)