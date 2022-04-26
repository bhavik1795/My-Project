from dataclasses import fields
from rest_framework import serializers
from quality_app.models import Quality, User
from drf_writable_nested.serializers import WritableNestedModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class QualitySerializer(WritableNestedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Quality
        fields = ('id','template_name', 'description', 'parameter_name', 'error_description', 'weightage','user')

    
