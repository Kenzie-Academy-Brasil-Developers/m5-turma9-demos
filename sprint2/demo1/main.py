from demo_classes.person import Person


def class_attrs():
    # p1 = new Person()
    p1 = Person()
    p2 = Person()
    p3 = Person()

    print(f"{p1=}")
    print(f"{p2=}")
    print(f"{p3=}")

    # print(f"{id(p1)=}")
    # print(hex(id(p1)))
    print("-" * 50)

    # Atributo de classe imutável (int)
    p1.life_expectancy = 1000
    print(f"{p1.life_expectancy=}")
    print(f"{p2.life_expectancy=}")
    print(f"{p3.life_expectancy=}")
    print("-" * 50)

    # Atributo de classe mutável (lista)
    p1.wishlist.append("Poltrona Gamer")
    print(f"{p1.wishlist=}")
    print(f"{p2.wishlist=}")
    print(f"{p3.wishlist=}")


def inst_attrs():
    p1 = Person("person1", "1111")
    p2 = Person("person2", "2222")
    p3 = Person("person3", "3333")

    print("-" * 10)

    print(f"{p1.name=}")
    print(f"{p2.name=}")
    print(f"{p3.name=}")
    print("-" * 10)

    p1.instruments.append("Teclado")
    print(f"{p1.instruments=}")
    print(f"{p2.instruments=}")
    print(f"{p3.instruments=}")
    print("-" * 10)

    print(f"{p1.__dict__=}")
    # print(f"{p2.instruments=}")
    # print(f"{p3.instruments=}")
    print("-" * 10)

    p1.save()
    # p2.save()
    print(f"{p1.retrieve()=}")
    # p1.save(self=p2)
    # Person.save(p2)


def inst_methods():
    p1 = Person("person1", "1111", "03/03/1993")
    p2 = Person("person2", "2222", "17/03/1995")
    p3 = Person("person3", "3333", "10/06/1995")

    p1.save()
    print(f"{p1.retrieve()=}")


if __name__ == "__main__":
    # class_attrs()
    # inst_attrs()
    inst_methods()
