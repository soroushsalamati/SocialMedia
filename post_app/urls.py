from django.urls import path
from .views import Login, TokenRefreshView
urlpatterns = [
    path('login/', Login.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]