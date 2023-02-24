from django.urls import path
from . import views
app_name='persona_app'
urlpatterns = [
    path('apiurl/<kword>/',views.UrlApiView.as_view()),
    path('apiurl2/<pk>/',views.UrlDetailView.as_view()),
    path('create/',views.UrlCreateView.as_view()),
    path('index/',views.Front.as_view()),
    path('r/<k>/',views.Reponse.as_view()),
]