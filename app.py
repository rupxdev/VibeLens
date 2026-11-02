
from flask import Flask, render_template, request
import joblib
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

model_path = os.path.join(BASE_DIR, "sentiment_model (4).pkl")
vectorizer_path = os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")

model = joblib.load(model_path)
tfidf = joblib.load(vectorizer_path)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    tweet = ""
    error = None

    if request.method == "POST":
        tweet = request.form.get("tweet", "").strip()

        if not tweet:
            error = "Please enter a tweet."
        else:
            try:
                cleaned = clean_text(tweet)

                if not cleaned:
                    error = "Please enter meaningful text."
                else:
                    vector = tfidf.transform([cleaned])
                    prediction = model.predict(vector)[0]

                    print("Original Tweet:", tweet)
                    print("Cleaned Tweet:", cleaned)
                    print("Prediction:", prediction)
                    print("Model Classes:", model.classes_)

                    if prediction == 4:
                        sentiment = "Positive 😊"
                    elif prediction == 0:
                        sentiment = "Negative 😞"
                    else:
                        sentiment = str(prediction)

            except Exception as e:
                error = "Prediction failed. Please check the model files."
                print("Error:", e)

    return render_template(
        "index.html",
        sentiment=sentiment,
        tweet=tweet,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
