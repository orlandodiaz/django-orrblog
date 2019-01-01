from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PostListHomeView.as_view(), name='blog'),
    path('posts', views.PostListView.as_view(), name='post-list'),
    path('<slug:slug>', views.PageDetailView.as_view(), name='page'),
    path(
        'page/<pk>/update', views.PageUpdateView.as_view(), name='page-update'),
    path(
        'post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path(
        'post/<pk>/update', views.PostUpdateView.as_view(), name='post-update'),

    # path('page/<int:pk>/update', views.Pa.as_view(), name='page-update')

    # path('work', views.WorkDetailView.as_view(), name='work'),

    # path('about', views.about_me, name='about-me'),
]
