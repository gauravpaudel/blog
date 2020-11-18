from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from myblog.views import postDetail, myStory, PostListView, SearchListView



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',home,name='home'),

    path('summernote/',include('django_summernote.urls')),

    path('',PostListView.as_view(),name='home'),
    path('story/',myStory,name='story'),
    path('post/<slug:slug>/',postDetail, name='post_detail'),
    path('search/',SearchListView.as_view(),name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
