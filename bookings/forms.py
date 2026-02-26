from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # add other fields like 'first_name' if needed

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')