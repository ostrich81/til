from django import forms 
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=('title','content')

class CommunityForm(forms.ModelForm):
    content = forms.CharField(
        max_length=100,
    )
    class Meta:
        model=Comment
        fields=('content')