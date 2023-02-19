'''
Main flask setup
'''
import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template

# Flask setup
app = Flask(__name__, static_folder='assets')

# Get variables from .env
# Automatically switches to local dev version without .env
load_dotenv()

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
    return render_template('about_us.html', page_title='About Us')


@app.route('/charities')
def charities():
    '''
    Renders charities page, reads the data from charities.json
    '''
    data = []
    with open("../charities.json", "r") as json_data:
        data = json.load(json_data)
    return render_template('charity.html', page_title='Charity', charities=data)



@app.route('/contact-us')
def contact_us():
    '''
    Renders contact us
    '''
    return render_template('contact_us.html', page_title='Contact Us')



@app.route('/search')
def search():
    '''
    Renders search result
    '''
    return render_template('search/search_result.html', page_title='Search')



@app.route('/charity/<company_name>')
def charity(company_name):
    '''
    Renders a given charity
    '''
    # Get charity here

    # charityobj = {
    #     "name": "Humane Society International",
    #     "goal": "To protect animals and their habitats worldwide.",
    #     "origin_location": "USA",
    #     "region_served": "Global",
    #     "founder": "Fred Myers and Helen Jones",
    #     "year_founded": 1954,
    #     "annual_revenue": "$200 million",
    #     "wikilink": "https://en.wikipedia.org/wiki/Humane_Society_International",
    #     "website_link": "https://www.hsi.org/",
    #     "category": "Animals",
    #     "keywords": ["animal welfare", "wildlife conservation"],
    #     "slug": slug
    # }
    company = {}
    with open("../charities.json", "r") as json_data:
        data = json.load(json_data)
        for object in data:
            if object["url"] == company_name:
                company = object
    return render_template('charity_details.html', charity_details=company)



# News articles
@app.route('/news/no-patents-on-seeds')
def article1():
    '''
    Renders news article 1
    '''

    return render_template('news/article_1.html', page_title='Article 1')



@app.route('/news/working-on-home')
def article2():
    '''
    Renders news article 2
    '''

    return render_template('news/article_2.html', page_title='Article 2')



@app.route('/news/carbon-footprint')
def article3():
    '''
    Renders news article 3
    '''

    return render_template('news/article_3.html', page_title='Article 3')



@app.errorhandler(404)
def page_not_found(e):
    '''
    Renders 404 page
    '''
    return render_template('404.html'), 404


if __name__ == '__main__':
    if os.getenv("DEVELOPMENT") == "False":
        app.run(debug=False)
    else:
        app.run(debug=True)
