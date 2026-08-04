from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "price",
            "start_date",
            "max_participiants",
            "trainer",
            "active",
        ]
        read_only_fields = ["id"]