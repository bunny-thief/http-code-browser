from django.views.generic import ListView

from .models import ResponseCode

class HomePageView(ListView):
    model = ResponseCode
    template_name = "home.html"