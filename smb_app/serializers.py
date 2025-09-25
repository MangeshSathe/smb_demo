from rest_framework import serializers
from .models import *

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters.")
        return value
    
    def validate_author(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Author must be at least 3 characters.")
        return value
    
    def validate_price(self, value):
        if not isinstance(value, (int, float)):
            raise serializers.ValidationError("Price must be a number.")
        return value



