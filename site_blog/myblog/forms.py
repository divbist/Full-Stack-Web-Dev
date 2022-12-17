from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Comment
from django import forms
# from .widgets import BootstrapDateTimePickerInput

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('author','title', 'text',)
        # published_date = forms.DateTimeField(
        # input_formats=['%d/%m/%Y %H:%M'],
        # widget=BootstrapDateTimePickerInput()
        # )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('post', 'author', 'text',)
