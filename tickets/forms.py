from django import forms
from .models import Comment, Ticket


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


class TicketForm(forms.ModelForm):
    """
    This form is used to create a new ticket. 
    """

    class Meta:
        model = Ticket
        exclude = ('user',)
        fields = ['title', 'description']

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if not title:
            raise forms.ValidationError('Title cannot be empty')

        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')

        if not description:
            raise forms.ValidationError('Description cannot be empty')

        return description
