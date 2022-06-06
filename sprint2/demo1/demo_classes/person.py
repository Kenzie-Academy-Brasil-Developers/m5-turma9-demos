# class Person(object)
from datetime import datetime as dt

from db import PERSONS

# pandas -> pd
# numpy -> np


class Person:
    # print("Olá")
    # Atributos de Classe
    life_expectancy = 90
    wishlist = ["Faca Ginzu 2000"]

    # __new__

    # Método de instancia
    def __init__(self, name: str, cpf: str, birthdate: str):
        self.name = name
        self.cpf = cpf
        self.birthdate = birthdate
        self.instruments = ["Violão"]
        self.created_at = dt.now()

    def save(self):
        # print(f"{self=}")
        # print(f"{type(self)=}")
        # print(f"{self.__dict__=}")
        PERSONS.append(self.__dict__)

    def retrieve(self) -> list:
        return PERSONS
