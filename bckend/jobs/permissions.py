from rest_framework.permissions import BasePermission
from users.models import User


class IsHR(BasePermission):
    """
    Allows access only to HR users.
    """

    message = "Only HR users can create jobs."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.HR
        )