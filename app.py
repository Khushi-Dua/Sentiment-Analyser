from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = None
    subjectivity = None

    if request.method == 'POST':
        text = request.form['text']
        if text.strip():
            blob = TextBlob(text)
            polarity = round(blob.sentiment.polarity, 2)
            subjectivity = round(blob.sentiment.subjectivity, 2)

            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
        else:
            sentiment = "Invalid input. Please enter valid text."

    return render_template('index.html', sentiment=sentiment, polarity=polarity, subjectivity=subjectivity)

if __name__ == '__main__':
    app.run(debug=True)
