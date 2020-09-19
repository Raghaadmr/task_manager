from rest_framework.permissions import BasePermission

class BoardOwner(BasePermission):
    message = "YOU ARE NOT THE OWNER!!!"

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else:
            return False

class BoardOwnertask(BasePermission):
    message = "YOU ARE NOT THE OWNER!!!"

    def has_object_permission(self, request, view, obj):
        if obj.board == request.user:
            return True
        else:
            return False
