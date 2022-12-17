from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.contrib.auth import login, logout
from . import models
from . import forms
from .models import School,Student
from .forms import UserCreateForm,SchoolForm,StudentForm

# Create your views here.


class HomePage(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "CPS"
        return context

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse("test"))
    #     return super().get(request, *args, **kwargs)

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    # fields = ("name","principal","location")
    model = models.School
    form_class = SchoolForm
    template_name = 'basic_app/school_form.html'

class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")

class StudentCreateView(CreateView):
    # fields = ("name","age","school")
    model = models.Student
    form_class = StudentForm

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

class SignUp(CreateView):
    # form_class = forms.UserCreateForm
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"
