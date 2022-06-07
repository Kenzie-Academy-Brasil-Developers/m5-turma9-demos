from persons.json_handler import JSONParser
from persons.person_model import Person


def dunder_methods():
    print(p1)  # print(str(p1)) / print(p1.__str__())
    print(p2)
    print(p3)

    print("-" * 50)

    print(f"{p1=}")
    print(f"{p2=}")
    print(f"{p3=}")

    print(repr(p1))
    print(p1.__repr__())

    # print(p1.__len__())
    print(len(p1))


def methods():
    print(f"{p1.__dict__=}")
    print(f"{p2.__dict__=}")
    print(f"{p3.__dict__=}")

    print("-" * 50)

    p1.save()
    p2.save()
    print(f"{Person.retrieve()=}")


def json_class():
    print(f"{JSONParser.retrieve()=}")
    print(f"{JSONParser().save({'name': 'Chrystian'})=}")


def heritance():
    p1.save()
    p2.save()
    p3.save()


if __name__ == "__main__":
    p1 = Person("person1", "1111", "03/03/1993")
    p2 = Person("person2", "2222", "17/03/1995")
    p3 = Person("person3", "3333", "10/06/1993")

    # dunder_methods()
    # methods()
    # json_class()
    heritance()
