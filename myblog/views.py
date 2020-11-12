from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name='myblog/homepage.html'
    context_object_name = 'posts'
    paginate_by = 3
    

class SearchListView(ListView):
    model = Post
    template_name = 'myblog/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query)| Q(body__icontains=query))
        return object_list
    

def myStory(request):
    return render(request,'myblog/mystory.html')



def postDetail(request, slug):
    post = get_object_or_404(Post, slug = slug)
    
    context = { 'post': post}

    return render(request,'myblog/post.html', context)

#class PostDetailView(Detailview):
