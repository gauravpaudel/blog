from django.contrib import admin
from django.urls import path
from myblog.views import postDetail, myStory, PostListView, SearchListView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',home,name='home'),
    path('',PostListView.as_view(),name='home'),
    path('story/',myStory,name='story'),
    path('post/<slug:slug>/',postDetail, name='post_detail'),
    path('search/',SearchListView.as_view(),name='search_results'),
]
