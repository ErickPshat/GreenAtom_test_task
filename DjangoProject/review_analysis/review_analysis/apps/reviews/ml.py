import sklearn
import nltk
import re
import numpy as np
from .apps import ReviewsConfig
	
def prep(review):

    review = re.sub("[^a-zA-Z]", " ", review)

    review = review.lower()

    token = nltk.word_tokenize(review)

    review = [nltk.stem.SnowballStemmer('english').stem(w) for w in token]
    
    return " ".join(review)

def transform(text):
	 return ReviewsConfig.vectorizer.transform([prep(text)])

def predict(text):
	return ReviewsConfig.predictor.predict(transform(text))

def proba_and_stars(text):
	probas = ReviewsConfig.predictor.predict_proba(transform(text))

	pos_neg_proba = max(sum(probas[0][:4]), sum(probas[0][4:]))
	pos_neg_proba = str(round(pos_neg_proba * 100, 2))
	pos_neg_proba = '({}%)'.format(pos_neg_proba)

	probas = list(map(lambda x: round(x * 100, 2), probas[0]))
	targets = [1, 2, 3, 4, 7, 8, 9, 10]
	probas = list(zip(targets, probas))
	probas = sorted(probas, key=lambda x: x[1], reverse=True)[:3]

	stars = '('
	for s in probas:
		stars += str(s[0]) + '/10: ' + str(s[1]) + '%, '
	stars = stars[:-2] + ')'

	return pos_neg_proba, stars
