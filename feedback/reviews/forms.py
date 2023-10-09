from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         'required': 'Please enter your name',
#         'max_length': 'Please enter no more than 100 characters'
#     })
    
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating',
        }
        
        error_messages = {
            'user_name': {
                'required': 'Please enter your name',
                'max_length': 'Please enter no more than 100 characters',
            },
            'review_text': {
                'required': 'Please enter your feedback',
                'max_length': 'Please enter no more than 200 characters',
            },
            'rating': {
                'required': 'Please enter your rating',
                'min_value': 'Please enter a rating between 1 and 5',
                'max_value': 'Please enter a rating between 1 and 5',
            },
        }