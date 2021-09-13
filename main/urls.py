from django.urls import path
from .views import UsersList, sign_up, login

urlpatterns = [
    path('', UsersList.as_view()),
    path('sign-up', sign_up),
    path('login', login)
]
