from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import BookView, Home


urlpatterns = [
    path('books/<int:book_id>', csrf_exempt(BookView.as_view())),
    path('books/', csrf_exempt(BookView.as_view())),
    path('', csrf_exempt(Home.as_view()))
]