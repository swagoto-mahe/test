from django.shortcuts import render
from django.views import generic
from .models import Post

# def about(request):
#     return render(request, 'about.html')



class about(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'about.html'
