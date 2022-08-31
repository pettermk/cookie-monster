from cookies.models import Cookie
from rest_framework import serializers

class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = '__all__'
