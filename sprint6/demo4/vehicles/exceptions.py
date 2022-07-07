from rest_framework.exceptions import APIException
from rest_framework.views import status

# class AlgumError(Exception):
#     ...


class NoSpotAvailableError(APIException):
    status_code = status.HTTP_409_CONFLICT
    # status_code = 409
    default_detail = "no available spots"
    default_code = "no_spots"
