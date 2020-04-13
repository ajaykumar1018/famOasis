import pickle
from Depression_detection_tweets import TweetClassifier
from tes import answers,session
from textblob import TextBlob

f = open('my_classifier.pickle', 'rb')
ff = open('my_classifier2.pickle','rb')
sc_tf_idf = pickle.load(f)
sc_bow = pickle.load(ff)

an = answers.query.all()
# text1 = answers.query.fiter_by(username="cv").order_by(id.desc()).first()
# print(text1)
#blob = TextBlob(text1)
# for sentence in blob.sentences:
#     pol = sentence.sentiment.polarity
#     bo = sc_bow.classify(sentence)
#     st = sc_tf_idf.classify(sentence)
#     print(pol,",",bo,",",st)
#     if pol <0.5 or bo == True or st == True:
#         print('Depressed')
        
f.close()
ff.close()
