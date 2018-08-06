from rest_framework import permissions
from pprint import pprint
#
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        pprint(request.user.id)
        # raise Exception()
        return obj.id == request.user.id