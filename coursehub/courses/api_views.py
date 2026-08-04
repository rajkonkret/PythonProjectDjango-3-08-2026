from rest_framework import permissions, viewsets

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related("trainer").all()
    serializer_class = CourseSerializer
    # niezalogowany moze uzyc GET
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]