from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1


class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 2
