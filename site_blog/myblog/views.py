from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.contrib.auth import login, logout
from . import models
from . import forms
from .models import Post
from .forms import UserCreateForm, PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    context_object_name = 'post_details'
    model = models.Post
    template_name = 'post_detail.html'

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class = PostForm
    model = models.Post
    template_name = 'post_form.html'

class CommentCreateView(CreateView):
    model = models.Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"
