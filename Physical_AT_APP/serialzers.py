from rest_framework import serializers
from .models import *

class ser_Physical_At_upload_status(serializers.ModelSerializer):
    class Meta:
        model = Physical_At_upload_status
        fields = '__all__'

class ser_Physical_At_Table(serializers.ModelSerializer):
    class Meta:
        model = Physical_AT_Table
        fields = '__all__'
