from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
