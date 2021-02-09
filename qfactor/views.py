from django.shortcuts import render
from .forms import FormMain
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

class IndexView(FormView):
    template_name = 'index.html'
    form_class = FormMain

    def get_success_url(self):
        return reverse('page2')

    def form_valid(self,form):
        print(form.cleaned_data)
        self.form_dat = form.cleaned_data
        return super().form_valid(form)


class Page2View(TemplateView):
    template_name = 'page2.html'

