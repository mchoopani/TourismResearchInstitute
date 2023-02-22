from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import BookView, Home,PaperView , EventView


urlpatterns = [
    path('books/<int:book_id>', csrf_exempt(BookView.as_view())),
    path('books/', csrf_exempt(BookView.as_view())),
    path('papers/<int:paper_id>', csrf_exempt(PaperView.as_view())),
    path('papers/', csrf_exempt(PaperView.as_view())),
    path('events/<int:event_id>', csrf_exempt(EventView.as_view())),
    path('events/', csrf_exempt(EventView.as_view())),
    path('', csrf_exempt(Home.as_view()))
]
