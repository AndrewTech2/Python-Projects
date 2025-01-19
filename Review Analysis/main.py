from nltk.sentiment import SentimentIntensityAnalyzer
import pandas, nltk

print("Attention! Results may not be accurate!")

analyzer = SentimentIntensityAnalyzer()
reviews = pandas.read_csv("reviews.csv")
sentiments_dict = {'pos': 'positive', 'neg': 'negative', 'neu': 'neutral'}
sentiments = []

for review in reviews.iterrows():
    sentiment_chart = analyzer.polarity_scores(review[1]['review'])
    sentiment_chart.pop("compound")
    sentiment = max(sentiment_chart, key=lambda x: sentiment_chart[x])
    sentiments.append(sentiment)

sentiments = list(map(lambda x: sentiments_dict[x].capitalize(), sentiments))
reviews['Sentiment'] = sentiments
print(reviews)