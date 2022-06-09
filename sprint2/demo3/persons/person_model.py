from datetime import datetime as dt

from .csv_handler import CSVParser
from .json_handler import DatabaseNotFoundError, JSONParser


class Person(JSONParser, CSVParser):
    life_expectancy = 90
    wishlist = ["Faca Ginzu 2000"]
    last_id = 0
    db_name = "person_db.json"

    def __init__(self, name: str, cpf: str, birthdate: str):
        self.id = None
        self.name = name
        self.cpf = cpf
        self.birthdate = birthdate
        self.created_at = dt.now().strftime("%d/%m/%Y %H:%M:%S.%f")

    def save(self):
        print("save() Person")
        self.id = self.get_next_id()
        super().save(self.__dict__)

    # @classmethod
    # def retrieve(cls) -> list:
    #     print("retrieve Person")
    #     return super().retrieve()

    @classmethod
    def get_next_id(cls):
        try:
            exinsting_data = cls.retrieve()
            next_id = exinsting_data[-1]["id"] + 1
        except (DatabaseNotFoundError, IndexError):
            next_id = 1
        return next_id

    def __str__(self) -> str:
        return f"{self.name} - {self.cpf}"

    def __repr__(self) -> str:
        return f"{self.name} - {self.cpf}"

    def __len__(self) -> int:
        return int(self.cpf)
