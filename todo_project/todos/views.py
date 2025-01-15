from rest_framework import viewsets, permissions
from .models import User, Todo
from .serializers import UserSerializer, TodoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=self.request.user.pk)

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Todo.objects.all()
        return Todo.objects.filter(author=self.request.user)