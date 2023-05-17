from models import People, User


def create_person():
    person = People(name="Henrique", age=35)
    print(person)
    person.save()


def read_person():
    person = People.query.all()
    filter_person = People.query.filter_by(name="Henrique")
    for p in filter_person:
        print(f"Name: {p.name}, age: {p.age}")
    for i in person:
        print(f"Name: {i.name}, age: {i.age}")


def update_person():
    person = People.query.filter_by(name="Henrique").first()
    person.age = 36
    person.save()


def delete_person():
    person = People.query.filter_by(name="Henrique").first()
    person.delete()


def insert_user(login, password):
    user = User(login=login, password=password)
    user.save()


def read_all_users():
    users = User.query.all()
    print(users)


if __name__ == "__main__":
    insert_user("henrique", "1234")
    insert_user("gonzaga", "4321")
    read_all_users()
    #create_person()
    #update_person()
    #delete_person()
    #read_person()
