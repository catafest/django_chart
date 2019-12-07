# default views.py
#from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
# snippet 
from django.shortcuts import get_object_or_404
# for chart 
from django.views.generic import TemplateView
from .models import Test001, Snippet
#
#def home_page(request):
#    return HttpResponse('Home page!')

def home_page(request):
    return render(request, 'test001/home.html',{
        'name':'CGF',
        'html_items': ['a','b','c','d','e']
    })


# define view for chart 
class Test001ChartView(TemplateView):
    template_name = 'test001/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Test001.objects.all()
        return context


def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    return render(request, 'test001/snippets_detail.html', {'snippet': snippet})


