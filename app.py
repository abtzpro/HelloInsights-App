from flask import Flask, request, jsonify
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['cybersecurity']
collection = db['news']

@app.route('/news', methods=['GET'])
def get_news():
    # get news from the database
    news = collection.find({}, {'_id': False}).sort('date', -1)
    return jsonify({'news': list(news)})

@app.route('/update', methods=['GET'])
def update_news():
    # scrape news from various sources and update the database
    news_sources = ['https://www.zdnet.com/topic/security/', 
                    'https://www.darkreading.com/', 
                    'https://thehackernews.com/' ]
    for source in news_sources:
        r = requests.get(source)
        soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            title = article.find('h3').text.strip()
            summary = article.find('p').text.strip()
            link = article.find('a')['href']
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # insert the news into the database
            collection.insert_one({'title': title, 'summary': summary, 'link': link, 'date': date})
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
