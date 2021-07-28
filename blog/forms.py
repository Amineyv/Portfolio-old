from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=255,
     widget = forms.TextInput(attrs={"class": "form-control",
     "placeholder": "Your Name"
     })
     )
     #attrs is used to allow us to specify some CSS classes.
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment"
        })
    )
