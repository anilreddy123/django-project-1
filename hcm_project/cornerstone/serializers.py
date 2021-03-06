from rest_framework import serializers
from .models import CornerstoneUserProfile


class CornerstoneUserProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = CornerstoneUserProfile
        fields = ['first_name', 'last_name']