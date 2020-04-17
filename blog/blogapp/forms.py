from django import forms

from blogapp.models import Article


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = {
            'title',
            'content',
            'active',
            'image'
        }
        widgets = {
            'title': forms.TextInput,
            'content': forms.Textarea,
        }
