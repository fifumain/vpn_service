from django import forms

from .models import Site


class SiteForm(forms.ModelForm):
    """Default form for creating a new Site model object"""

    class Meta:
        model = Site
        fields = ["name", "url"]
        labels = {
            "name": "Название сайта",
            "url": "URL сайта",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите название сайта"}
            ),
            "url": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "Введите URL сайта"}
            ),
        }
