from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'style': 'border-color: blue; height: 75px;',
                'placeholder': 'Comments'
            }
        )
    )

    class Meta(object):
        model = Comment
        fields = {
            "comment"
        }
