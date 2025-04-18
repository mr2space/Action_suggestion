from django.urls import path, include
from . import  views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.APILogViewSet, basename='api_log')


urlpatterns = [
    path('analyze', views.suggestion, name="action_suggestion"),
    path('logs', include(router.urls))
]