from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import signupView , loginView


urlpatterns = [
    path('signup/', csrf_exempt(signupView.as_view())),
    path('login/', csrf_exempt(loginView.as_view())),
]
