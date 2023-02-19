'''
Main flask setup
'''
from flask import Flask, render_template

# Flask setup
app = Flask(__name__)
app = Flask(__name__, static_folder='assets')

# Static pages
@app.route('/')
def index():
    '''
    Renders index page
    '''
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    '''
    Renders about us page
    '''
    return render_template('about_us.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/search')
def search():
    '''
    Renders search result
    '''
    return render_template('search/search_result.html')

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
    return render_template('news/article_1.html')

@app.route('/article-2')
def article2():
    '''
    Renders news article 2
    '''
    return render_template('news/article_2.html')

@app.route('/article-3')
def article3():
    '''
    Renders news article 3
    '''
    return render_template('news/article_3.html')

@app.errorhandler(404)
def page_not_found(e):
    '''
    Renders 404 page
    '''
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)