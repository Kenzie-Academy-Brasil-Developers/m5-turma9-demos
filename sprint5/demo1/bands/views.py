from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView, Response, status

from .models import Band
from .serializers import BandSerializer


class ListCreateBandView(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class RetrieveUpdateDestroyBandView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    # Muda a regra de consulta no banco
    # lookup_field = "band_id"

    # Alterar regra de url
    lookup_url_kwarg = "band_id"


# class ListBandView(generics.ListAPIView):
#     queryset = Band.objects.all()
#     serializer_class = BandSerializer


# class CreateBandView(generics.CreateAPIView):
#     queryset = Band.objects.all()
#     serializer_class = BandSerializer


# Create your views here.
# class BandView(APIView):
#     def get(self, request):
#         bands = Band.objects.all()

#         serializer = BandSerializer(bands, many=True)
#         # serializer = BandSerializer(Band.objects.all(), many=True)

#         return Response(serializer.data)

#     def post(self, request):

#         serializer = BandSerializer(data=request.data)

#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         return Response(serializer.data, status.HTTP_201_CREATED)


# class BandDetailView(APIView):
#     def get(self, request, band_id):
#         band = get_object_or_404(Band, id=band_id)

#         serializer = BandSerializer(band)

#         return Response(serializer.data)

#     def patch(self, request, band_id):
#         band = get_object_or_404(Band, id=band_id)
#         serializer = BandSerializer(band, request.data)

#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         return Response(serializer.data)

#     def delete(self, request, band_id):
#         band = get_object_or_404(Band, id=band_id)

#         band.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
