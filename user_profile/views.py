from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from django.http import Http404


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save()


# class DetailView(APIView):

#     def get_object(self, pk):
#         try:
#             return settings.AUTH_USER_MODEL.objects.get(pk=pk)
#         except ProfileSerializer.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         students = self.get_object(pk)
#         serializer = ProfileSerializer(students)
#         return Response(serializer.data)
