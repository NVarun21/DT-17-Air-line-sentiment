from flask import Flask, render_template, request, jsonify
from test import TextToNum
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        msg = request.form.get("message")
        print(f"\n🔹 Received Message: {msg}")

        # Apply text preprocessing
        ob = TextToNum(msg)
        ob.cleaner()
        ob.token()
        ob.removeStop()
        st = ob.stemme()

        print(f"🔹 Processed Text: {st}")

        # Load vectorizer
        with open("vectorizer.pickle", "rb") as vcfile:
            vc = pickle.load(vcfile)

        # Transform text into numerical form
        stvc = " ".join(st)
        data = vc.transform([stvc])
        print(f"🔹 Vectorized Data: {data}")

        # Load trained model
        with open("model.pickle", "rb") as mbfile:
            model = pickle.load(mbfile)

        # Predict sentiment
        pred = model.predict(data)
        print(f"🔹 Prediction: {pred}")

        return jsonify({"result": str(pred[0])})

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"error": "Something went wrong!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)