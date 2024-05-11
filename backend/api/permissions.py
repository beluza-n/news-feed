from rest_framework.permissions import BasePermission


class NewsPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action == 'create':
            return request.user.is_authenticated
        elif view.action in ['update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'destroy']:
            return (obj.author == request.user or request.user.is_staff)
        else:
            return False
