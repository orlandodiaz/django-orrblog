# from django.views.generic import ListView, DetailView, CreateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixIn

# Create your views here.
from .models import Page, Post
from django.views.generic import ListView, DetailView, UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UpdatePageForm, UpdatePostForm
from django.views.generic.edit import FormMixin
# from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListHomeView(ListView):
    model = Post
    context_object_name = 'posts'  # use posts instead of object_list
    ordering = ['-date_posted']
    paginate_by = 3
    template_name = 'blog/index.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'  # use posts instead of object_list
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(FormMixin, DetailView):
    model = Post
    context_object_name = 'post'
    slug_field = "slug"
    slug_url_kwarg = "slug"
    form_class = UpdatePostForm
    success_url = '/'

    update_form = None

    def get_context_data(self, **kwargs):
        """ Overwrite context so that form is also passed in addition to title"""

        context = super().get_context_data(**kwargs)

        self.update_form = UpdatePostForm(initial={
            'body2': self.object.body2,
            'title': self.object.title
        })
        context['form'] = self.update_form
        # context['form'] = UpdatePageForm(initial={'title': self.object.title, 'body': self.object.body2})

        return context


class PageDetailView(FormMixin, DetailView):
    model = Page
    context_object_name = 'page'
    slug_field = "slug"
    slug_url_kwarg = "slug"
    form_class = UpdatePageForm
    success_url = '/about'

    update_form = None

    def get_context_data(self, **kwargs):
        """ Overwrite context so that form is also passed in addition to title"""

        context = super().get_context_data(**kwargs)

        self.update_form = UpdatePageForm(initial={
            'body2': self.object.body2,
            'title': self.object.title
        })
        context['form'] = self.update_form
        # context['form'] = UpdatePageForm(initial={'title': self.object.title, 'body': self.object.body2})

        return context


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'body2']
    template_name_suffix = '_detail'

    # template_name = 'page_detail'

    def form_valid(self, form):
        post = form.save(commit=False)
        print('form is valid')
        # post.updated_by = self.request.user
        # post.updated_at = timezone.now()
        post.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form is invalid')
        for field in form:
            print(field, field.errors)
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body2']
    # template_name_suffix = '_detail'
    template_name = 'post_update_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        print('form is valid')
        # post.updated_by = self.request.user
        # post.updated_at = timezone.now()
        post.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form is invalid')
        for field in form:
            print(field, field.errors)
        return super().form_valid(form)

    # # Make the author the current logged in user
    # def form_valid(self, form):
    #     # form.instance.author = self.request.user
    #     return super().form_valid(form)
    #
    # # Prevent other users from updating other people's post
    # def test_func(self):
    #     post = self.get_object()
    #     # if self.request.user == post.author:
    #     #     return True
    #     return False
