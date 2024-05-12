from flask import Flask
from flask_restful import Api,Resource,reqparse


app = Flask(__name__)
api = Api(app)

class Todolists(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('task',type=str,help = 'Task name')
        super().__init__()


    def get(self):
        return {'todos':  [ 1,2,3]}

    def post(self):
        args = self.parser.parse_args()
        task = args['task']
        return {'task':task},201

api.add_resource(Todolists,'/todos')


if __name__ == '__main__':
    app.run(debug=True)