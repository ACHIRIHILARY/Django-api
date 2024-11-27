from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import BlockpostSerializer
from . models import Blockpost


class BlockPostListCreate(generics.ListCreateAPIView):
    queryset = Blockpost.objects.all()
    serializer_class = BlockpostSerializer

    def delete(self, request, *args, **kwargs):
         Blockpost.objects.all().delete()
         return Response(status = status.HTTP_204_NO_CONTENT)
         


class BlockpostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
     queryset = Blockpost.objects.all()
     serializer_class = BlockpostSerializer
     Lookup_field = "pk"


