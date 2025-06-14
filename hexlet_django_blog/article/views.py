from django.shortcuts import render

# Create your views here.
from django.views import View

class IndexView(View):
    template_name = "articles/index.html"
    
    def get(self, request, *args, **kwargs):
        context = {"app_name": "article"}
        return render(request, self.template_name, context)