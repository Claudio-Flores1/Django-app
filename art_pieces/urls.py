from django.urls import path
from .views.views import ArtsView, ArtDetailView
form .views.museum_views import MuseumsView, MuseumDetailView

urlpatterns = [
    path('', ArtsView.as_view(), name='arts'),
    path('<int:pk>/', ArtDetailView.as_view(), name='art')
    path('', MuseumsView.as_view(), name='museums'),
    path('<int:pk>/', ArtDetailView.as_view(), name='museum')
]