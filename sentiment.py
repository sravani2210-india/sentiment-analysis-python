from textblob import TextBlob

text = input("Enter a sentence: ")

analysis = TextBlob(text)

if analysis.sentiment.polarity > 0:
    print("Sentiment: Positive")
elif analysis.sentiment.polarity < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
