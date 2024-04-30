from gnews import GNews
import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    google_news = GNews()
    india_ai_news = google_news.get_news('Artificial Intelligence')[:3]
    return render_template('index.html', india_ai_news=india_ai_news)

if __name__ == '__main__':
    app.run(debug=True)
