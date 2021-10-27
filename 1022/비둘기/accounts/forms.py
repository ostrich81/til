from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User=get_user_model()

class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model=User
        fields=('password','username','email','last_name','first_name',)
        