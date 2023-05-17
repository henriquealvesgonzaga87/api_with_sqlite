from flask import Flask, request
from flask_restful import Resource, Api
from models import People, Activities, User
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#USER ={
#    "Henrique": "123",
#    "Gonzaga": "321"
#}


#@auth.verify_password
#def verification(login, pasw):
#    if not (login, pasw):
#        return False
#    return USER.get(login) == pasw

@auth.verify_password
def verification(login, password):
    if not (login, password):
        return False
    return User.query.filter_by(login=login, password=password).first()

class Person(Resource):
    @auth.login_required
    def get(self, name):
        person = People.query.filter_by(name=name).first()
        try:
            response = {
                "name": person.name,
                "age": person.age,
                "id": person.id
            }
        except AttributeError:
            response = {"status": "error", "message": "person not found"}

        except Exception:
            response = {"status": "error", "message": "unknown error"}

        return response

    def put(self, name):
        person = People.query.filter_by(name=name).first()
        datas = request.json
        if "name" in datas:
            person.name = datas["name"]
        if "age" in datas:
            person.age = datas["age"]
        person.save_person()
        response = {
            "name": person.name,
            "age": person.age,
            "id": person.id
        }
        return response

    def delete(self, name):
        filters = People.query.filter_by(name=name).first()
        message = f"The person '{name}' the person has been deleted"
        filters.delete()
        return {"status": "success", "message": message}


class ListPeople(Resource):

    @auth.login_required
    def get(self):
        filters = People.query.all()
        response = [{"id": i.id, "name": i.name, "age": i.age} for i in filters]
        return response

    @auth.login_required
    def post(self):
        datas = request.json
        person = People(name=datas['name'], age=datas['age'])
        person.save()
        response = {
            "id": person.id,
            "name": person.name,
            "age": person.age
        }
        return response


class ListActivities(Resource):

    @auth.login_required
    def get(self):
        activities = Activities.query.all()
        response = [{"id": i.id, "name_activities": i.name_activities, "person": i.person.name}for i in activities]
        return response

    @auth.login_required
    def post(self):
        datas = request.json
        person = People.query.filter_by(name=datas["person"]).first()
        activity = Activities(name_activities=datas["name_activities"], person=person)
        activity.save()
        response = {
            "person": activity.person.name,
            "name_activities": activity.name_activities,
            "id": activity.id
        }
        return response


api.add_resource(Person, "/person/<string:name>/")
api.add_resource(ListPeople, "/person/")
api.add_resource(ListActivities, "/activities/")

if __name__ == '__main__':
    app.run(debug=True)
