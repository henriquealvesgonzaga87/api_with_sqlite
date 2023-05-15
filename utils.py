from models import People


def create():
    person = People(name="Gisa", age=38)
    print(person)
    person.save_person()


def read():
    person = People.query.all()
    filter_person = People.query.filter_by(name="Henrique")
    for p in filter_person:
        print(f"Name: {p.name}, age: {p.age}")
    for i in person:
        print(f"Name: {i.name}, age: {i.age}")


def update():
    person = People.query.filter_by(name="Henrique").first()
    person.age = 36
    person.save_person()


def delete():
    person = People.query.filter_by(name="Henrique").first()
    person.delete_person()


if __name__ == "__main__":
    #create()
    #update()
    delete()
    read()
