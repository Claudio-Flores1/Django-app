from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 

from ..models import Art
from art_pieces.serializers import ArtSerializer

class ArtsView(APIView):
    """View class for arts/ for viewing all and creating"""
    def get(self, request):
        arts = Art.objects.all()
        serializer = ArtSerializer(arts, many=True)
        return Response({'arts': serializer.data})

    def post(self, request):
        serializer = ArtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtDetailView(APIView):
    """View class for arts/:pk for viewing a single art, updating a single art, or removing a single art"""
    def get(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        serializer = ArtSerializer(art)
        return Response({'art': serializer.data})

    def patch(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        serializer = ArtSerializer(art, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
