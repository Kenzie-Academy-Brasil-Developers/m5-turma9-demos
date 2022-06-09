import json


class DatabaseNotFoundError(Exception):
    ...


class JSONParser:
    db_name = "default_db.json"

    @classmethod
    def retrieve(cls) -> list | dict:
        print("retrieve() JSONParser")
        try:
            with open(cls.db_name, "r") as json_file:
                return json.load(json_file)
        except FileNotFoundError as err:
            # print(err.args)
            raise DatabaseNotFoundError

    @classmethod
    def save(cls, payload: dict) -> None:
        print("save() JSONParser")
        try:
            existing_data = cls.retrieve()
        except DatabaseNotFoundError:
            existing_data = []

        existing_data.append(payload)

        with open(cls.db_name, "w") as json_file:
            json.dump(existing_data, json_file, indent=2)
