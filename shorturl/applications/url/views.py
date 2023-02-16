from django.shortcuts import render
from .models import Url
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import UrlSerializer,UrlSerializer2
# Create your views here.
class UrlApiView(ListAPIView):
    serializer_class=UrlSerializer
    def get_queryset(self):
        kword=self. kwargs['kword']
        print(Url.objects.filter(url=kword))
        if Url.objects.filter(
            url=kword
            ):
            print(Url.objects.filter(url=kword))
            return Url.objects.filter(url=kword)
        else:
            Url.objects.create(
                url = kword
                )
            return Url.objects.filter(url=kword)
        
class UrlDetailView(RetrieveAPIView):
    serializer_class= UrlSerializer2
    queryset=Url.objects.all()