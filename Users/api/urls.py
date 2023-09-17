from django.urls import path ,include
from rest_framework.routers import DefaultRouter
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views

router = DefaultRouter()
router.register(r'users',views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.register ,name='register'),
    #  path('api-token-auth/', obtain_jwt_token, name='api_token_auth'),
    # path('api-token-refresh/', refresh_jwt_token, name='api_token_refresh'),
    # path('api-token-verify/', verify_jwt_token, name='api_token_verify'),
    path('login/', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='user_logout'),
]
