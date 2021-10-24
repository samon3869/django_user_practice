from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from allauth.account.views import PasswordChangeView
from coplate.models import Review

# Create your views here.
class IndexView(ListView):
    model = Review
    template_name = "coplate/index.html"
    context_object_name = "reviews"
    paginate_by = 4
    ordering = ["-dt_created"]

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
