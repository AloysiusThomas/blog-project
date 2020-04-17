from django import forms

from blogapp.models import Article, ArticleImage


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Title',
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Content',
        }
    ))

    class Meta:
        model = Article
        fields = {
            'title',
            'content',
            'active',
            'top_image'
        }
        widgets = {
            'title': forms.TextInput,
            'content': forms.Textarea,
        }


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = ArticleImage
        fields = ('image',)
