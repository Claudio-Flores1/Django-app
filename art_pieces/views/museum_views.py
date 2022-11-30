from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 

from ..models import Museum
from art_pieces.serializers import MuseumSerializer

class MuseumsView(APIView):
    """View class for museums/ for viewing all and creating"""
    def get(self, request):
        museums = Museum.objects.all()
        serializer = MuseumSerializer(museums, many=True)
        return Response({'museums': serializer.data})

    def post(self, request):
        serializer = MuseumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MuseumDetailView(APIView):
    """View class for museums/:pk for viewing a single museum, updating a single museum, or removing a single museum"""
    def get(self, request, pk):
        museum = get_object_or_404(Museum, pk=pk)
        serializer = MuseumSerializer(museum)
        return Response({'museum': serializer.data})

    def patch(self, request, pk):
        museum = get_object_or_404(Museum, pk=pk)
        serializer = MuseumSerializer(museum, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        museum = get_object_or_404(Museum, pk=pk)
        museum.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
