from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home Page')

@app.route('/scrape')
def scrape_demo():
    response = requests.get('https://httpbin.org/html')
    soup = BeautifulSoup(response.text, 'html.parser')
    return f"Scraped title: {soup.find('h1').text}"
