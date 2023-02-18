'''
Loads all the data into the database
'''

import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Category, Keyword, Charity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///charityHub.db'
db = SQLAlchemy(app)

with open('data/categories.json') as f:
    categories = json.load(f)
    
with open('data/keywords.json') as f:
    keywords = json.load(f)
    
with open('data/charities.json') as f:
    charities = json.load(f)


with app.app_context():
    db.create_all()

    for category in categories:
        db.session.add(
            Category(
                name=category['name'],
                slug=category['slug']
            )
        )
        
    for keyword in keywords:
        db.session.add(
            Keyword(
                name=keyword['name']
            )
        )

    for charity in charities:
        category = Category.query.filter_by(slug=charity['category']).first()
        keywords = [Keyword.query.filter_by(name=k).first() for k in charity['keywords']]
        db.session.add(
            Charity(
                name=charity['name'],
                goal=charity['goal'],
                origin_location=charity['origin_location'],
                region_served=charity['region_served'],
                founder=charity['founder'],
                year_founded=charity['year_founded'],
                annual_revenue=charity['annual_revenue'],
                wikilink=charity['wikilink'],
                website_link=charity['website_link'],
                category=category,
                keywords=keywords
            )
        )
    db.session.commit()
