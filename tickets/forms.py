from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form used to create a new comment
    on a ticket
    """

    class Meta:
        model = Comment
        exclude = ('user', 'ticket')
        fields = ['comment']
