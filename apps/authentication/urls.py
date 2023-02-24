from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import signupView , loginView , logoutView , changePassView


urlpatterns = [
    path('login/', csrf_exempt(loginView.as_view())),
    path('logout/', csrf_exempt(logoutView.as_view())),
    path('changepass/', csrf_exempt(changePassView.as_view())),
    path('signup/', csrf_exempt(signupView.as_view())),
]
