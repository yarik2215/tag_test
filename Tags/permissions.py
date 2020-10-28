from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


class IsAdminOrReadOnly(permissions.BasePermission):
    '''
    Allow only users with is_company_admin permission to 
    edit objects.
    '''

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        res = request.user.is_company_admin
        return res
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        res = request.user.is_company_admin
        return res



class IsCompanyAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_company_admin



class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        user_id = request.GET.get('user_id')
        if not user_id:
            return True

        return int(user_id) == request.user.id or request.user.is_company_admin

    def has_object_permission(self, request, view, obj):

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user or request.user.is_company_admin


