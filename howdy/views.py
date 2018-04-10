from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'index.html',context=None)
class AboutMeView(TemplateView):
    template_name = 'about.html'