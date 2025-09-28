from textblob import TextBlob
from newspaper import Article
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

url='https://www.annefrank.org/en/anne-frank/go-in-depth/what-is-the-holocaust/'
article= Article(url)

article.download()
article.parse()
article.nlp()

text=article.summary
print(text)

analyzer = SentimentIntensityAnalyzer()
vs = analyzer.polarity_scores(text)
print(vs['compound']) # Compound score is a single summary score

if (vs['compound']>0.05) :
    print("the article is positive")
elif (vs['compound'] <0.05 and vs['compound']>-0.05):
    print("the article is neutral")
else :
    print("the article is negative")