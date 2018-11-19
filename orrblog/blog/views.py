# from django.views.generic import ListView, DetailView, CreateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixIn

# Create your views here.
from .models import Page, Post
from django.views.generic import ListView, DetailView, UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UpdatePageForm
from django.views.generic.edit import FormMixin
# from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'  # use posts instead of object_list
    ordering = ['-date_posted']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    # context['updateform'] = UpdatePostForm


class PageDetailView(FormMixin, DetailView):
    model = Page
    context_object_name = 'page'
    slug_field = "slug"
    slug_url_kwarg = "slug"
    form_class = UpdatePageForm
    # success_url = reverse_lazy('page','about')
    success_url = '/about'

    update_form = None

    def get_context_data(self, **kwargs):
        """ Overwrite context so that form is also passed in addition to title"""

        context = super().get_context_data(**kwargs)

        self.update_form = UpdatePageForm(initial=
                                         {'body': self.object.body2,
                                          'title': self.object.title
                                          }
                                         )
        context['form'] = self.update_form
        # context['form'] = UpdatePageForm(initial={'title': self.object.title, 'body': self.object.body2})

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # form = self.get_form()
        form = self.get_form()
        print(form)
        if form.is_valid():
            print('form is valid')
            return self.form_valid(form)
        else:
            print('not valid')
            # print(form)
            for field in form:
                print(field.name, end=" :")
                print(field.errors)
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data['title'])
        print(form.cleaned_data['body'])

        print('instance')
        print(self.get_object())
        print(type(self.get_object()))

        page = self.get_object()
        page.body2 = form.cleaned_data['body']
        page.save()

        return super(PageDetailView, self).form_valid(form)


# class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Page
#     fields = ['title']
#
#     # Make the author the current logged in user
#     def form_valid(self, form):
#         # form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     # Prevent other users from updating other people's post
#     def test_func(self):
#         post = self.get_object()
#         # if self.request.user == post.author:
#         #     return True
#         return False