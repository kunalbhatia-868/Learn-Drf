from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_permission=bool(request.user and request.user.is_staff)
        return request.method=="GET" or admin_permission 
    
class IsReviewOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #checkpermission for read only
            return True                     #To alloww all users to read
        else:
            #checkpermission for write request            
            if request.user==obj.review_user or request.user.is_staff:
                return True
            else:
                return False