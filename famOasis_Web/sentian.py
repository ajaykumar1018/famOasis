# import sqlalchemy as db

# engine = db.create_engine('sqlite:///answers.sqlite3')
# connection = engine.connect()
# metadata = db.MetaData()
# tabw = db.Table('answers', metadata, autoload=True, autoload_with=engine)

# print(tabw.columns.keys())

# print(tabw.columns['threeGoodThings'])


# from tes import answers, User

# an = answers.query.all()
# print(an[0].threeGoodThings)
# two = answers.query.filter_by(sleepHours=6).first()
# print(two.sleepHours,"3good",two.threeGoodThings)


# username = "aq"
# password = "qaw1"
# uname = User.query.filter_by(username="br").first()
# passw = User.query.filter_by(password="bg").first()
# print(uname.username,' - ',passw.password)


from textblob import TextBlob

# text = '''
# The titular threat of The Blob has always struck me as the ultimate movie
# monster: an insatiably hungry, amoeba-like mass able to penetrate
# virtually any safeguard, capable of--as a doomed doctor chillingly
# describes it--"assimilating flesh on contact.
# Snide comparisons to gelatin be damned, it's a concept with the most
# devastating of potential consequences, not unlike the grey goo scenario
# proposed by technological theorists fearful of
# artificial intelligence run rampant.
# '''

text = "I'm going through a lot now a days, people around me are constantly ignoring me and don't want to be with me. Their activities irritate me a lot, which makes me to take out my rage on something. I'm undergoing a lot of depression"

blob = TextBlob(text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

for sentence in blob.sentences:
    print(sentence)
    print(sentence.sentiment.polarity)

# print("depression".sentiment.polarity)