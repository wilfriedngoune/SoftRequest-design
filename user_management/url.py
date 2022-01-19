from posixpath import basename
from rest_framework import routers

from user_management.views import MoiviewSet


router= routers.DefaultRouter()
router.register('Student', MoiviewSet, basename='Student')