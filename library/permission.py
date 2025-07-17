from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if  (request.method in SAFE_METHODS) or (request.user and request.user.is_authenticated):
            return True 
        # return super().has_permission(request, view)