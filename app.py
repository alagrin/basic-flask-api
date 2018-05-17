from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {
            'student': name,
            'grade': 'B'
            }

api.add_resource(Student, '/student/<string:name>')
# Gets http://127.0.0.1:8001/student/Name url, no need for app.route

app.run(port=8001, debug=True)