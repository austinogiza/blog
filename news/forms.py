from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={

        'class': 'form-control',
        'row': 6,
        'resize': 'none',
        'label': 'Comment'

    }))
