from django.views.generic import CreateView

from accounts.models import User
from accounts.utils import get_username


class UserCreateView(CreateView):
    model = User
    fields = {
        'email',
        'first_name',
        'last_name',
        'nick_name',
    }
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        username = user.email.split("@")
        username = username[0]
        user.username = get_username(username)
        user.save()
        user.set_password("q1w2e3r4")
        return super().form_valid(form)

    def get_success_url(self):
        return "/"
