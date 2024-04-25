from django.contrib.auth.forms import UserCreationForm
from myauth.models import ClientUser
from django.contrib.auth import get_user_model

User = get_user_model()


class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = ClientUser
        fields = ('username', 'email', 'password1', 'password2', 'aboutfield')
