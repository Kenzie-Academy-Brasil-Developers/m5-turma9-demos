from django.urls import path

from . import views

# urlpatterns = [
#     path("bands/", views.BandView.as_view()),
#     path("bands/<int:band_id>/", views.BandDetailView.as_view()),
# ]


urlpatterns = [
    # path("bands/", views.ListBandView.as_view()),
    # Errado
    path("bands/", views.ListCreateBandView.as_view()),
    path("bands/<int:band_id>/", views.RetrieveUpdateDestroyBandView.as_view()),
]
