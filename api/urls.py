from django.urls import path , include
from api import views
from rest_framework import routers, urlpatterns


router = routers.DefaultRouter()
router.register('users',views.UserAPI,basename='api')

urlpatterns=[
    path('',include(router.urls)),
]