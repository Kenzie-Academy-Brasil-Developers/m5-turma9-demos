import json


class JSONParser:
    @staticmethod
    def retrieve() -> list | dict:
        print("retrieve JSONParser")
        with open("db.json", "r") as json_file:
            return json.load(json_file)

    # def save(self, payload: dict) -> None:
    def save(self) -> None:
        print("save JSONParser")

        existing_data = self.retrieve()
        existing_data.append(self.__dict__)

        with open("db.json", "w") as json_file:
            json.dump(existing_data, json_file, indent=2)
