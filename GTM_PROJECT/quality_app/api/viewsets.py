from django.shortcuts import get_object_or_404
from quality_app.models import User, Quality
from quality_app.api.serializers import UserSerializer, QualitySerializer
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from rest_framework import generics

# Create your views here.

# Using APIView
# class UserList(APIView):
#     """
#     List all User, or create a new User.
#     """
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class UserDetail(APIView):
#     """ 
#     Retrieve, update or delete a User instance.
#     """
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Using Generics APIView.
# class UsertList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UsertDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Using Model Viewsets

class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QualityViewsets(viewsets.ModelViewSet):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer