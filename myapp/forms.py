from django import forms
from django.contrib.auth.models import User
from django.utils import timezone


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def save(self, commit=True) -> User:
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["email"]  # Set username as email
        user.set_password(self.cleaned_data["password"])  # Hash password
        if commit:
            user.save()
        return user
    



