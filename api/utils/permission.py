from rest_framework.permissions import BasePermission

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 1:
            return True
        return False
