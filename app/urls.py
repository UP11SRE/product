from django.contrib import admin
from django.urls import include, path
from app.views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products',ProductViewSet)

urlpatterns = [
    path('',include(router.urls))
]
