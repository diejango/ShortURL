from django.shortcuts import render
from .models import Url
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from .serializers import UrlSerializer,UrlSerializer2
from django.views.generic import TemplateView
# Create your views here.
class UrlApiView(ListAPIView):
    serializer_class=UrlSerializer
    def get_queryset(self):
        kword=self. kwargs['kword']       
        return Url.objects.filter(get=kword)
        
        
class UrlDetailView(RetrieveAPIView):
    serializer_class= UrlSerializer2
    queryset=Url.objects.all()

class UrlCreateView(CreateAPIView):
    serializer_class= UrlSerializer2


class Front (TemplateView):
    template_name='index.html'

class Reponse (TemplateView):
    template_name='reponse.html'
    context_object_name='k'
    def get_queryset(self):
        return self.kwargs['k']