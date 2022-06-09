class ValidationError(Exception):
    ...


class PersonSerializer:
    valid_inputs = {"name": str, "cpf": str, "birthdate": str}

    def __init__(self, *args, **kwargs):
        self.errors = {}
        self.__data = kwargs  # atributo privado
        # self._atributo = "algo" # atributo protegido

    def is_valid(self):
        try:
            self.__validate_required_keys()
            return True
        except ValidationError:
            return False

    def __validate_required_keys(self):
        for key in self.valid_inputs.keys():
            if key not in self.__data.keys():
                # self.errors[key] = "missing key"
                self.errors.update({key: "missing key"})

        if self.errors:
            raise ValidationError("validação falhou")

    # TODO:
    # limpar dados de entrada (retirar chaves extra)
    # validar os tipos de cada campo obrigatorio
