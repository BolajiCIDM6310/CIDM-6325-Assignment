from django import forms
from .models import Comment, CommentRes, RecipeRating


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class EmailRecipeForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    responses = forms.CharField(
        required=False,
        widget=forms.Textarea
    )


class CommentRecForm(forms.ModelForm):
    class Meta:
        model = CommentRes
        fields = ['name', 'email', 'body']


class RecipeRatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['rating']


class SearchForm(forms.Form):
    query = forms.CharField()
