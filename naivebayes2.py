import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import scikitplot.plotters as skplt
import os
from sklearn.naive_bayes import GaussianNB
  
import nltk
nltk.download('stopwords')
stopwords.words('english')  
news_dataset = pd.read_csv('train.csv')
# news_dataset
news_dataset.isnull().sum()
news_dataset = news_dataset.fillna('')
news_dataset.isnull().sum()

news_dataset['content'] = news_dataset['title'] + news_dataset['author']
news_dataset['content'].head()
port_stem = PorterStemmer()
def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]' , ' ' , content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content
news_dataset['content'] = news_dataset['content'].apply(stemming)
x = news_dataset['content'].values
y = news_dataset['label'].values
# print(x)
# print(y)
vectorizer = TfidfVectorizer()
vectorizer.fit(x)
x = vectorizer.transform(x)
# print(x)
#x_train , x_test , y_train , y_test = train_test_split(x , y , test_size=0.0002 , stratify = y , random_state =2)
x_train=x[50:]
y_train=y[50:]
x_test=x[:50]
y_test=y[:50]
model =  GaussianNB()
model.fit(x_train , y_train)
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction , y_train)
print( " training_data_accuracy is "  , training_data_accuracy)
x_test_prediction = model.predict(x_test)
training_data_accuracy = accuracy_score(x_test_prediction , y_test)
print ("testing_data_accuracy" , training_data_accuracy)
t=41
x_new =   x_test[t]
prediction = model.predict(x_new)
if(prediction):
    print("the predicted news is real")
else:
    print("the predicted news is fake")
if(y_test[t]):
    print("the news is real")
else:
    print("the news is fake")

# import pickle

# filename = 'trained_model.sav'
# pickle.dump(model , open(filename ,'wb'))
# filename2='trained_vectorizer.sav '
# pickle.dump(vectorizer , open(filename2 ,'wb'))
