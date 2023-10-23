from django.urls import path

from users.views import UserCreateAPIView

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create-user')
]
