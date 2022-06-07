# class Person(object)
from datetime import datetime as dt

from db import PERSONS

from .json_handler import JSONParser


# class Person(object)
class Person(JSONParser):
    life_expectancy = 90
    wishlist = ["Faca Ginzu 2000"]
    last_id = 0

    def __init__(self, name: str, cpf: str, birthdate: str):
        self.id = self.auto_increment_id()
        self.name = name
        self.cpf = cpf
        self.birthdate = birthdate
        self.instruments = ["Violao"]
        # self.created_at = dt.now()
        self.created_at = dt.now().strftime("%d/%m/%Y %H:%M:%S.%f")

    def save(self):
        # PERSONS.append(self.__dict__)
        print("save Person")
        super().save()

    # @staticmethod
    @classmethod
    def retrieve(cls) -> list:
        # return PERSONS
        print("retrieve Person")
        # return JSONParser.retrieve()
        return super().retrieve()

    @classmethod
    def auto_increment_id(cls):
        cls.last_id += 1
        return cls.last_id

    def __str__(self) -> str:
        return f"{self.name} - {self.cpf}"

    def __repr__(self) -> str:
        return f"{self.name} - {self.cpf}"

    def __len__(self) -> int:
        return int(self.cpf)
