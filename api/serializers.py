# serializers for the BlogPost model defined in api/models.py
# This is used to convert model instances to JSON and vice versa.

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']
        