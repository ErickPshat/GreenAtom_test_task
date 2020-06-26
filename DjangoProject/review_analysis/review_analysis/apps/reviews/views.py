from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from .models import Review
from .ml import predict, proba_and_stars

def index(request):
	latest_reviews_list = Review.objects.order_by('-pub_date')
	return render(request, 'reviews/list.html', {'latest_reviews_list':latest_reviews_list})

def leave_review(request):
	review = Review()
	review.review_text = request.POST['text']
	review.review_prediction = predict(review.review_text)
	review.pub_date = timezone.now()
	review.prediction_proba = proba_and_stars(review.review_text)[0]
	review.review_stars = proba_and_stars(review.review_text)[1]
	review.save()
	return HttpResponseRedirect(reverse(index))