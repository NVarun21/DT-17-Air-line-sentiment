from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.json
        text = data.get("text", "").lower()

        if any(word in text for word in ["happy", "great", "good", "excellent"]):
            sentiment = {"sentiment": "😊 Positive Sentiment!", "color": "lightgreen"}
        elif any(word in text for word in ["bad", "worst", "poor", "terrible"]):
            sentiment = {"sentiment": "😡 Negative Sentiment!", "color": "red"}
        else:
            sentiment = {"sentiment": "😐 Neutral Sentiment!", "color": "yellow"}

        return jsonify(sentiment)

    return render_template("predict.html")  # Render a new page if accessed via GET


if __name__ == "__main__":
    app.run(debug=True)
