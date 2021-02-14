from django.shortcuts import render
from .forms import FormMain
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import redirect
from .models import Element

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        el_list = []
        for el in Element.objects.all():
            el_list.append(el.name)

        context["elements"] = el_list

        return context

class Page2View(TemplateView):
    template_name = 'page2.html'


from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt


@api_view(["POST"])
@parser_classes([JSONParser])
def parse_data(request):
    if request.method == "POST":
        print(request.data)
        return Response(process_data(request.data))



def process_data(jsondata):
    return {'Data received from backend':jsondata}