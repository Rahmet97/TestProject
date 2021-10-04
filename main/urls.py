from django.urls import path
from .views import UsersList, sign_up, login, news, add_news

urlpatterns = [
    path('', UsersList.as_view()),
    path('sign-up', sign_up),
    path('login', login),
    path('get-news', news),
    path('add-news', add_news)
]
