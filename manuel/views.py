from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from manuel.models import Planet, User, Book
from manuel.serializers import PlanetSerializer, BookSerializer

class PlanetViewSet(viewsets.ModelViewSet):
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()

@api_view(['GET'])
def user_books(request, *args, **kwargs):
    if not 'user_id' in kwargs:
        return Response({'message':'request must have user id'}, status=status.HTTP_400_BAD_REQUEST)

    user_id = kwargs['user_id']
    user = User.objects.filter(id=user_id).get()
    friends = user.friends.values_list('id').get()

    # Build a list of a network of User Ids
    network = friends + (user_id,)
    books = Book.objects.filter(user__in=network)

    serializer = BookSerializer(books, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)
