from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter , OrderingFilter
from rest_framework.pagination import PageNumberPagination , LimitOffsetPagination


class CustomPagination(PageNumberPagination):
    page_size=5

class CustomLimitPagination(LimitOffsetPagination):
    default_limit=5
    limit_query_param='limit'
    max_limit=20 # Can be over ridden


class UserAPI(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['^first_name','^last_name']
    pagination_class=CustomPagination
    pagination_class=CustomLimitPagination
    ordering_fields=['-age']
