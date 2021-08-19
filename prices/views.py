from django.shortcuts import render
from django.views import generic
from .models import Post



# def prices(request):
#     return render(request, 'prices.html')



class prices(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'prices.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'