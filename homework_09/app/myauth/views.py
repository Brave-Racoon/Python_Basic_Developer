from django.views.generic import CreateView
from myauth.forms import MyUserCreateForm
from myauth.models import ClientUser


# Create your views here.
#
class MyUserCreateView(CreateView):
    model = ClientUser
    success_url = '/'
    form_class = MyUserCreateForm
