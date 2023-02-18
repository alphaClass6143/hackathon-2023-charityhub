from flask import Flask, render_template

app = Flask(__name__)
app = Flask(__name__, static_folder='assets')

# Please create routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-us')
def aboutUs():
    return render_template('about-us.html')

@app.route('/search')
def search():
    return render_template('search_result.html')

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
    return render_template('contact-us.html')

@app.route('/article-1')
def article1():
    return render_template('article_1.html')

@app.route('/article-2')
def article2():
    return render_template('article_2.html')

@app.route('/article-3')
def article3():
    return render_template('article_3.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)