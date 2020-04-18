from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class UserForm(UserCreationForm):
    field_order = {
        'email',
        'first_name',
        'last_name',
        'nick_name',
    }

    class Meta:
        model = User
        fields = {
            'email',
            'first_name',
            'last_name',
            'nick_name',
        }
