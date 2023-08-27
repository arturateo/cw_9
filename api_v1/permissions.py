from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action is ["retrieve", "update", "destroy"] and request.user == obj.author:
            return True
        return False
