from addresses.models import Address
from addresses.serializers import AddressSerializer
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=100)

    address = AddressSerializer()

    def create(self, validated_data: dict):
        # print(validated_data)
        address_data = validated_data.pop("address")
        # print(address)

        user = User.objects.create(**validated_data)
        Address.objects.create(**address_data, user=user)

        return user

    def update(self, instance: User, validated_data: dict):
        # 0. verificando se foi passada a chave first_name, senão eu uso a que ja existe
        # pouco dinâmica, mas ainda válida.
        # instance.first_name = validated_data.get("first_name", instance.first_name)
        # instance.last_name = validated_data.get("last_name", instance.last_name)
        # ...

        # 1. Regra manual para nao permitir que address seja atualizado (regra de negocio)
        non_editable_keys = ("address",)

        for key, value in validated_data.items():
            if key in non_editable_keys:
                raise KeyError
            setattr(instance, key, value)

        # 2. Uma outra abordagem seria a de atualizar sim o address
        # para isso poderia iterar sobre a chave e atualizar o necessario através
        # de user.address

        # address_data = validated_data.pop("address", None)
        # # Atualiza address, se tiver sido passado por body do PATCH
        # if address_data:
        #     for key, value in address_data.items():
        #         # Passo intance.address que é uma instancia de Address
        #         setattr(instance.address, key, value)

        # # Atualiza os atributos de user (sem o address)
        # for key, value in validated_data.items():
        #     setattr(instance, key, value)

        instance.save()

        return instance
