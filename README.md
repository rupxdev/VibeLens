
<div align="center">

# ✨ VibeLens

### AI-Powered Twitter Sentiment Analyzer

**See the emotion behind every tweet.**

An intelligent web application that uses Natural Language Processing (NLP) and Machine Learning to analyze tweets and identify their emotional tone.

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3&logoColor=white)

</div>

---

## 🌟 About the Project

**VibeLens** is an AI-powered Twitter Sentiment Analysis web application designed to identify the emotional tone of tweets and short text messages.

It uses Natural Language Processing (NLP) and Machine Learning techniques to classify text into two sentiment categories:

- 😊 **Positive Sentiment**
- 😞 **Negative Sentiment**

The application is developed using Python and Flask, with TF-IDF for text feature extraction and Logistic Regression for sentiment classification.

---

## 🖥️ Application Screenshots

### 🏠 Home Page
<img width="1052" height="898" alt="Homepage" src="https://github.com/user-attachments/assets/5beb7a35-4684-4dbf-9210-ef4509c026b7" />


### 😊 Positive Sentiment Prediction

<img width="972" height="870" alt="positive tweet" src="https://github.com/user-attachments/assets/6bbe5b1b-214b-4923-8230-a62beeb8d902" />


### 😞 Negative Sentiment Prediction

<img width="965" height="867" alt="Negative tweet" src="https://github.com/user-attachments/assets/c7cf0771-bf2f-402e-be7d-9ebb2bd48f76" />


---

## 🚀 Key Features

- **Sentiment Detection:** Identifies positive and negative emotions in text.
- **Text Preprocessing:** Cleans URLs, mentions, hashtags, special characters, and unnecessary spaces.
- **TF-IDF Vectorization:** Converts text into numerical features.
- **Machine Learning:** Uses Logistic Regression for sentiment classification.
- **Interactive Web Interface:** Provides a simple and attractive user experience.
- **Instant Prediction:** Displays the sentiment result after submission.
- **Input Validation:** Handles empty or invalid text input.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Backend web framework |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Sentiment classification |
| HTML5 | Frontend structure |
| CSS3 | Website styling |
| Joblib | Loading saved ML models |

---

## ⚙️ How VibeLens Works

The application follows a simple Machine Learning pipeline:

1. **User Input:** The user enters a tweet or text message.
2. **Text Preprocessing:** The submitted text is cleaned by removing URLs, mentions, hashtags, and unnecessary characters.
3. **Feature Extraction:** TF-IDF converts the cleaned text into numerical features.
4. **Sentiment Prediction:** The trained Logistic Regression model analyzes the extracted features.
5. **Result Display:** The application displays the predicted sentiment on the webpage.

---

## 📂 Project Structure

```text
VibeLens/
│
├── app.py
│
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── screenshot/
    ├── home.png
    ├── positive-result.png
    └── negative-result.png
```

---

## 💻 Installation and Setup

Follow these steps to run VibeLens locally.

### 1. Clone the Repository

```bash
git clone https://github.com/rupxdev/VibeLens.git
```

### 2. Navigate to the Project Directory

```bash
cd VibeLens
```

### 3. Install Dependencies

```bash
py -m pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
py app.py
```

### 5. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

Your VibeLens application is now ready to use!

---

## 🧪 Sample Test Cases

| Sample Tweet | Expected Sentiment |
|---|---|
| I love this beautiful day! Feeling amazing! | 😊 Positive |
| This is a wonderful experience. I am so happy! | 😊 Positive |
| I hate this terrible experience. | 😞 Negative |
| Everything is going wrong. I am very disappointed. | 😞 Negative |

*Note: These are example test cases. Actual predictions depend on the trained model.*

---

## 📊 Machine Learning Approach

| Component | Description |
|---|---|
| Dataset | Sentiment140 Twitter Dataset |
| Algorithm | Logistic Regression |
| Feature Extraction | TF-IDF Vectorization |
| Task | Binary Sentiment Classification |
| Backend | Flask |

The model learns patterns from labeled tweet data and uses those patterns to classify new text as positive or negative.

---

## 🔮 Future Enhancements

- Introduce neutral sentiment classification.
- Add prediction confidence scores.
- Improve model performance through hyperparameter tuning.
- Evaluate model performance using accuracy, precision, recall, and F1-score.
- Support sentiment analysis for larger text inputs.
- Deploy the application on a cloud platform.
- Add visual analytics and sentiment statistics.

---

## 👩‍💻 Developer

<div align="center">

### Rupsha Manna

**B.Tech – Computer Science and Engineering**

Techno India University

[![GitHub](https://img.shields.io/badge/GitHub-rupxdev-181717?style=for-the-badge&logo=github)](https://github.com/rupxdev)

</div>

---

<div align="center">

## 💜 VibeLens

**See the emotion behind every tweet.**

*Designed and developed with Python, Machine Learning, and Flask.*

</div>
