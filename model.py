import pickle
import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

  
port_stem = PorterStemmer()
vectorizer = pickle.load(open ('trained_vectorizer.sav' , 'rb'))
model = pickle.load(open('trained_model.sav' , 'rb'))


def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]' , ' ' , content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content  


# df=pd.read_excel('test2.xlsx')
# df
# df['content']=df['author']+df['title']
# df['content']=df['content'].apply(stemming)
# temp =df['content'].values
# temp = vectorizer.transform(temp)
# temp_prediction = model.predict(temp)
# if(temp_prediction):
#     print("the news is real")
# else:
#     print("the news is fake")


def predictor(author, title, text):
    
    title=re.sub(',' , ' ' , title)
    data=('author,title,text\n' f'{author},{title},{text}\n')
    data=str(data)
    from io import StringIO
    df2=pd.read_csv(StringIO(data) , dtype =object)

    df2['content'] = df2['author']+" " +df2['title']
    df2['content']=df2['content'].apply(stemming)

    temp =vectorizer.transform(df2['content'].values)
    temp_prediction = model.predict(temp)

    if(temp_prediction):
        return True
    else:
        return False


