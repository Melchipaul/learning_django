from typing import Any
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'
    
        
    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/thank-you')
    #     return render(request, 'reviews/review.html', {
    #         "form": form
    #     })
        
class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['message'] = 'Thanks for submitting your review!'
        return context
    
class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'
    
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
    
class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review