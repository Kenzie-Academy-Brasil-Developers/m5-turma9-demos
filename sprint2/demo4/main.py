from persons.json_handler import JSONParser
from persons.person_model import Person
from persons.serializer import PersonSerializer, ValidationError


def json_class():
    JSONParser.db_name = "outro_db.json"
    # print(f"{JSONParser.retrieve()=}")
    JSONParser.save({"name": "Chrystian"})


def heritance():
    ...
    # p1.save()
    # p1.retrieve()
    # p1.uma_funcao()
    # print(Person.__mro__)
    # p2.save()
    # p3.save()


def serializer_test():
    data_0 = {
        "name": True,
        "cpf": "1234",
        "birthdate": 1,
        "extra_key": "extra_value",
    }
    data_1 = {"birthdate": "03/03/1993"}
    data_2 = {
        "name": "Chrystian",
        "cpf": "1234",
        "birthdate": "03/03/1993",
        "extra_key": "extra_value",
    }

    dirty_data = {
        "cpf": "1234",
        "birthdate": "03/03/1993",
    }

    serializer = PersonSerializer(**dirty_data)

    # try:
    #     # print(serializer.__data)
    #     # print(serializer._atributo)
    #     serializer.__validate_required_keys()
    # except ValidationError:
    #     ...
    #     # print(serializer.errors)

    if not serializer.is_valid():
        print(serializer.errors)
    else:
        print(serializer.validated_data)


if __name__ == "__main__":
    # p1 = Person(1, "1111", "03/03/1993")
    # p2 = Person("person2", "2222", "17/03/1995")
    # p3 = Person("person3", "3333", "10/06/1993")

    # json_class()
    # heritance()
    serializer_test()
