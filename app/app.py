
import json
from flask import Flask, render_template

app = Flask(__name__, static_folder='assets')

# Static pages
@app.route('/')
def index():
    '''
    Renders index page
    '''
    return render_template('index.html')


@app.route('/about-us')
def aboutUs():
    '''
    Renders about us page
    '''
    return render_template('about-us.html', page_title='About Us')


@app.route('/search')
def search():
    '''
    Renders search result
    '''
    data = []
    with open('charities.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template('search_result.html', page_title='Search', charity=data)



@app.route('/charity/<slug>')
def charity(slug):
    '''
    Renders a given charity
    '''
    # Get charity here
    charityobj = {
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
    return render_template('charity.html', charity=charityobj)

# News articles
@app.route('/article-1')
def article1():
    '''
    Renders news article 1
    '''
    return render_template('article_1.html', page_title='Article 1')


@app.route('/article-2')
def article2():
    '''
    Renders news article 2
    '''
    return render_template('article_2.html', page_title='Article 2')


@app.route('/article-3')
def article3():
    '''
    Renders news article 3
    '''
    return render_template('article_3.html', page_title='Article 3')

@app.errorhandler(404)
def page_not_found(e):
    '''
    Renders 404 page
    '''
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)