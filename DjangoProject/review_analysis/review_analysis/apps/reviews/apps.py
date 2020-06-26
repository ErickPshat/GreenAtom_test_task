from django.apps import AppConfig
import os
import bz2
import pickle
import _pickle as cPickle

class ReviewsConfig(AppConfig):
	name = 'reviews'
	path = os.path.join(os.path.dirname(__file__), 'ml_data') 
	predictor_path = 'lgr.pkl'
	# vectorizer_path = 'vectorizer.pbz2'
	vectorizer_path = 'vectorizer.pkl'

	with open(os.path.join(path, predictor_path), 'rb') as f:
	    predictor = pickle.load(f)

	# with bz2.BZ2File(os.path.join(path, vectorizer_path), 'rb') as f: 
	# 	vectorizer = cPickle.load(f)

	with open(os.path.join(path, vectorizer_path), 'rb') as f:
	    vectorizer = pickle.load(f)