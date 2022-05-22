# install gensim 3.8.1. For Natual Language Processing
import re
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from gensim.summarization import keywords

# Read csv file instead. cmt is the most liked comment
cmt = "comment haha"

# Text Pre-Processing
# Remove capital letters, punctuations, numbers & emoji
cmt = cmt.lower()
cmt = re.sub("[,.\"!@#$%^&*(){}?/;`~:<>+=-]", "", cmt)
cmt = re.sub("1234567890", "", cmt)
emoji = re.compile("["
                   u"\U0001F600-\U0001FFFF"  # emoticons
                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                   u"\U00002702-\U000027B0"
                   u"\U000024C2-\U0001F251"
                   "]+", flags=re.UNICODE)

cmt = emoji.sub('',cmt)
slist = keywords(cmt, lemmatize=True).split() # shortlisted keywords
dict1 = {}
for word in slist:
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1

# Visualise the most occuring words
wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(dict1)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
