from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    message = "You are not an manager."

    def has_permission(self, request, view):
        return request.user.role == 1


class IsAdministrator(BasePermission):
    message = "You are not an administrator."

    def has_permission(self, request, view):
        return request.user.role == 2
