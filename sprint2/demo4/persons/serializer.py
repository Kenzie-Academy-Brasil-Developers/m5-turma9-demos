class ValidationError(Exception):
    ...


class PersonSerializer:
    valid_inputs = {"name": str, "cpf": str, "birthdate": str}

    def __init__(self, *args, **kwargs):
        self.errors = {}
        self.__data = kwargs  # atributo privado
        # self._atributo = "algo" # atributo protegido
        self.validated_data = {}

    def is_valid(self):
        try:
            self.__clean_data()
            self._validate_required_keys()
            self.__validate_data_types()

            self.validated_data = self.__data

            return True
        except ValidationError:
            return False

    def _validate_required_keys(self):
        for key in self.valid_inputs.keys():
            if key not in self.__data.keys():
                # self.errors[key] = "missing key"
                self.errors.update({key: "missing key"})

        if self.errors:
            raise ValidationError("validação falhou")

    # TODO:
    # limpar dados de entrada (retirar chaves extra)
    # validar os tipos de cada campo obrigatorio
    def __clean_data(self):
        for key in list(self.__data.keys()).copy():
            if key not in self.valid_inputs.keys():
                self.__data.pop(key)

        # print(self.__data)

    def __validate_data_types(self):
        for key, value in self.valid_inputs.items():
            if type(self.__data[key]) is not value:
                self.errors.update({key: f"must be a {value.__name__}"})

        if self.errors:
            raise ValidationError("validação falhou")
