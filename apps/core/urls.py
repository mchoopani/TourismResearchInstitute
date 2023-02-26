from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import BookView, Home,PaperView , EventView , DocumentView , PlanView , ApplicationView , TopicView , CostSectionView


urlpatterns = [
    path('books/<int:book_id>', csrf_exempt(BookView.as_view())),
    path('books/', csrf_exempt(BookView.as_view())),

    path('plans/<int:plan_id>/application/topic/<int:topic_id>/section/<int:section_id>/', csrf_exempt(CostSectionView.as_view())),
    path('plans/<int:plan_id>/application/topic/<int:topic_id>/section/', csrf_exempt(CostSectionView.as_view())),
    path('plans/<int:plan_id>/application/topic/<int:topic_id>/', csrf_exempt(TopicView.as_view())),
    path('plans/<int:plan_id>/application/topic/', csrf_exempt(TopicView.as_view())),
    path('plans/<int:plan_id>/application/', csrf_exempt(ApplicationView.as_view())),
    path('plans/<int:plan_id>/documents/<int:document_id>/', csrf_exempt(DocumentView.as_view())),
    path('plans/<int:plan_id>/documents/', csrf_exempt(DocumentView.as_view())),
    path('plans/<int:plan_id>/', csrf_exempt(PlanView.as_view())),
    path('plans/', csrf_exempt(PlanView.as_view())),

    path('', csrf_exempt(Home.as_view()))
]
