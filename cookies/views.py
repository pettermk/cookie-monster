from cookies import serializers
from cookies.models import Cookie
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from cookies.serializers import CookieSerializer


class IsPostOrIsAuthenticated(permissions.BasePermission):        
    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        # Otherwise, only allow authenticated requests
        # Post Django 1.10, 'is_authenticated' is a read-only attribute
        return request.user and request.user.is_authenticated


class CookiesView(APIView):
    serializer_class = CookieSerializer
    permission_classes = [IsPostOrIsAuthenticated]

    
    def get(self, request, format=None):
        cookies = Cookie.objects.all().order_by('time_sent')
        serializer = CookieSerializer(cookies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CookieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
