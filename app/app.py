'''
Main flask setup
'''
import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request

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
    return render_template(
        'charity.html', page_title='Charity', charities=data)


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
    # Get query
    query = request.args.get("query")

    # Get JSON
    data = []
    with open("../charities.json", "r") as json_data:
        data = json.load(json_data)

    # Loop through and add result with weight depending on the priority
    charity_list = []

    for charity in data:
        weight = 0

        if charity["category"].lower().__contains__(query.lower()):
            weight += 100

        for keyword in charity["keywords"]:
            if keyword.lower().__contains__(query.lower()):
                weight += 90
                break

        if charity["charity_name"].lower().__contains__(query.lower()):
            weight += 70

        if charity["origin_location"].lower().__contains__(query.lower()):
            weight += 50

        if charity["goal"].lower().__contains__(query.lower()):
            weight += 30

        if charity["founder"].lower().__contains__(query.lower()):
            weight += 20

        if weight > 0:
            charity_list.append({
                "weight": weight,
                "charity": charity
            })

    # Sort list by weight
    charity_list = sorted(charity_list, key=lambda charity: charity["weight"], reverse=True)

    # Remove weight for the final response
    charity_response = []

    i = 0
    for item in charity_list:
        charity_response.append(item["charity"])
        if i >= 9:
            break
        else:
            i += 1

    return render_template('search/search_result.html', page_title='Search', charity_list=charity_response, query=query)

@app.route('/charity/<company_name>')
def charity(company_name):
    '''
    Renders a given charity
    '''
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

    return render_template('news/article_1.html', page_title='No patents on seeds')


@app.route('/news/working-on-home')
def article2():
    '''
    Renders news article 2
    '''

    return render_template('news/article_2.html', page_title='Working on home')



@app.route('/news/carbon-footprint')
def article3():
    '''
    Renders news article 3
    '''

    return render_template('news/article_3.html', page_title='Carbon footprint')

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
