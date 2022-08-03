from rest_framework import serializers
from .models import message

class messageSerliazer(serializers.ModelSerializer):
    class Meta:
        model=message
        fields=(
            'id','sender','receiver','message','subject'
        )