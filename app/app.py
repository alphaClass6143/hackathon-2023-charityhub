import json
from flask import Flask, render_template


app = Flask(__name__)


# Please create routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about-us')
def aboutUs():
    return render_template('about-us.html', page_title='About Us')


@app.route('/search')
def search():
    data = []
    with open('charities.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template('search_result.html', page_title='Search', charity=data)


@app.route('/charity/<slug>')
def charity(slug):
    # Get charity here
    charity = {
        "name": "Humane Society International",
        "goal": "To protect animals and their habitats worldwide.",
        "origin_location": "USA",
        "region_served": "Global",
        "founder": "Fred Myers and Helen Jones",
        "year_founded": 1954,
        "annual_revenue": "$200 million",
        "wikilink": "https://en.wikipedia.org/wiki/Humane_Society_International",
        "website_link": "https://www.hsi.org/",
        "category": "Animals",
        "keywords": ["animal welfare", "wildlife conservation"],
        "slug": slug
    }

    return render_template('charity.html', charity=charity)


@app.route('/contact-us')
def contactUs():
    return render_template('contact-us.html', page_title='Contact Us')


@app.route('/article-1')
def article1():
    return render_template('article_1.html', page_title='Article 1')


@app.route('/article-2')
def article2():
    return render_template('article_2.html', page_title='Article 2')


@app.route('/article-3')
def article3():
    return render_template('article_3.html', page_title='Article 3')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)