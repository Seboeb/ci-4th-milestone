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

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')

        if not comment:
            raise forms.ValidationError('Comment cannot be empty')

        return comment
