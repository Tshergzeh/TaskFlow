from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', include('rest_framework.urls')),
]
