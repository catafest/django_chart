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

from .models import Post

# add to views.py Author and Book 
from .models import Author, Book
# Author , Book redirect 
from django.shortcuts import redirect

from django.forms import modelformset_factory, inlineformset_factory

#
#def home_page(request):
#    return HttpResponse('Home page!')

# django framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from mysite.serializers import UserSerializer, GroupSerializer

from .models import Author, Book

def home_page(request):
    return render(request, 'test001/home.html',{
        'name':'CGF',
        'html_items': ['a','b','c','d','e']
    })

# author and book source code 
def index_next(request, author_id):
    author = Author.objects.get(pk=author_id)
    BookFormset = inlineformset_factory(Author,Book, fields=('book_name',), can_delete=False, extra=1)
    if request.method == 'POST':
        formset = BookFormset(request.POST,instance = author)
        if formset.is_valid():
            formset.save()
            return redirect('index_next',author_id = author_id)
    formset = BookFormset(instance = author)
    return render(request, 'index_next.html', {'formset': formset})



def posts(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'test001/posts.html', context)

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

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
