import numpy as np
import matplotlib as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
exceptions = [word for word in stopwords.words('english') if word=='not']
my_stopwords = [word for word in stopwords.words('english') if not word in exceptions]
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in my_stopwords]
    review = ' '.join(review) 
    corpus.append(review)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500) 
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X, y)
