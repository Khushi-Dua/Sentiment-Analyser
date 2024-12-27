# Sentiment Analysis Web Application 📊🎨

Welcome to the **Sentiment Analysis Web App** repository! 🌟 This project leverages **Flask/Django** to create an intuitive web application for performing sentiment analysis. With the help of **TextBlob**, the app determines whether user-entered text is **positive**, **negative**, or **neutral**, while also displaying detailed polarity and subjectivity scores. 



## Acknowledgement 🎓

This project was completed as part of my internship with **CodexIntern**. Grateful for the opportunity to learn and showcase my skills in web development and natural language processing. 🙏



## Features 🔄

- **User-Friendly Web Interface**: Input text directly on the app for real-time analysis.
- **Sentiment Classification**:
  - **Positive** 😊
  - **Negative** 😡
  - **Neutral** 😶
- **Detailed Insights**:
  - **Polarity**: Measures the sentiment (range: -1 to 1).
  - **Subjectivity**: Indicates how subjective or objective the text is (range: 0 to 1).
- **Customizable**: Easily extend the app for advanced NLP tasks.


## Tech Stack 🧠

- **Framework**: Flask (or Django alternative) 🌐
- **Backend Logic**: Python 🐍
- **NLP Library**: [TextBlob](https://textblob.readthedocs.io/en/dev/)
- **Frontend**: HTML, CSS, and Bootstrap for styling 🌀



## How It Works 🚀

1. **Input Text**: Users enter a sentence or paragraph into the text field.
2. **Process with TextBlob**: The app analyzes the input for sentiment.
3. **Display Results**:
   - Sentiment classification (Positive, Negative, or Neutral).
   - Polarity score.
   - Subjectivity score.



## Getting Started 🎮

### Prerequisites 

- Python 3.7+
- Required libraries:
  ```bash
  pip install flask textblob
  ```

### Installation 

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. Install dependencies:
   ```bash
   pip install textblob flask
   from textblob import download_corpora
   download_corpora()

   
   ```

3. Start the server:
   ```bash
   python app.py
   ```

4. Open the app in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## Code Structure 🌐

```
Sentiment-Analysis-App/
├── app.py             # Main script for Flask application
├── templates/         # HTML templates for the app
│   ├── index.html     # Home page
├── sentiment_analysis.py           #function script
├── README.md          # Project documentation
```



## Insights and Observations 🌍

- **Polarity Score**: Helps determine the overall sentiment.
- **Subjectivity Score**: Highlights the level of opinion in the text.
- **Practical Applications**:
  - Analyze customer reviews.
  - Process social media comments.
  - Perform basic text mining tasks.




## License 📚

This project is licensed under the [MIT License](LICENSE).



## Acknowledgements 🎉

- **CodexIntern**: For the opportunity to work on this exciting project!
- Open-source tools like Flask, TextBlob, and Bootstrap.
- [Myself](https://github.com/Khushi-Dua), for exploring this repository!



## Let's Connect! 📢

- **GitHub**: [Khushi-Dua](https://github.com/Khushi-Dua)
- **LinkedIn**: [Khushi Dua](https://linkedin.com/in/khushi-dua7)
- **Email**: khushidua110036@gmail.com


Happy Analyzing! 🙌🌐
