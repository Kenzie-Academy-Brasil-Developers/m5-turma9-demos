import unittest

from persons.serializer import PersonSerializer, ValidationError


class TestPersonSerializer(unittest.TestCase):
    def test_if_data_is_being_cleaned(self):
        dirty_data = {
            "name": "Chrystian",
            "cpf": "1234",
            "birthdate": "03/03/1993",
            "extra_key": "extra_value",
        }

        expected = {
            "name": "Chrystian",
            "cpf": "1234",
            "birthdate": "03/03/1993",
        }

        result = PersonSerializer(**dirty_data)

        self.assertTrue(result.is_valid())
        self.assertEqual(result.validated_data, expected)

    def test_validated_required_keys(self):
        dirty_data = {
            "cpf": "1234",
            "birthdate": "03/03/1993",
        }

        result = PersonSerializer(**dirty_data)

        with self.assertRaises(ValidationError):
            # result.is_valid()
            result._validate_required_keys()
        # with self.assertRaises(KeyError):
        #     # result.is_valid()
        #     result._validate_required_keys()
