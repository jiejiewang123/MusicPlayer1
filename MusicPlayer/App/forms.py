from .models import UserAccount
from django.forms import ModelForm

# from .models import check


class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields ='__all__'

    