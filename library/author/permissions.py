from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		return request.user.is_staff


"""
class IsStaffOrReadOnly(permissions.BasePermission):

		# Allows access to Staffs only

		def has_permission(self, request, view):
			return request.user and request.user.is_staff
"""

	
