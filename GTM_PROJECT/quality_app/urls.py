from collections import UserList
from django.urls import path, include
# from quality_app.api.viewsets import UsertList, UsertDetail
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from quality_app.api.viewsets import QualityViewsets, UserViewsets

router = DefaultRouter()
router.register(r'users', UserViewsets,basename="users")
router.register(r'quality', QualityViewsets,basename="quality")



urlpatterns = [
    path('api/', include(router.urls)),

    # path('api/user-list/', UsertList.as_view()),
    # path('api/user-details/<int:pk>', UsertDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)