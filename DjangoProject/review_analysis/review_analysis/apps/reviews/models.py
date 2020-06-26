from django.db import models

class Review(models.Model):
	review_text = models.TextField('text of the review')
	review_prediction = models.IntegerField('prediction of the review')
	prediction_proba = models.CharField('prediction probability', max_length = 10)
	review_stars = models.CharField('star prediction', max_length = 50)
	pub_date = models.DateTimeField('date of the review')

	def __str__(self):
		return self.review_text[:50]