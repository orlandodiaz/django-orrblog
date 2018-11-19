from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PostListView.as_view(), name='blog'),
    path('<slug:slug>', views.PageDetailView.as_view(), name='page'),
    path('blog/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    # path('page/<int:pk>/update', views.Pa.as_view(), name='page-update')

    # path('work', views.WorkDetailView.as_view(), name='work'),

    # path('about', views.about_me, name='about-me'),

]