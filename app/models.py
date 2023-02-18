from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Category(db.Model):
    '''
    Category model
    '''
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    slug = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return f"Category('{self.name}', '{self.slug}')"


class Keyword(db.Model):
    '''
    Keyword model
    '''
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return f"Keyword('{self.name}')"


class Charity(db.Model):
    '''
    Charity model
    '''
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    goal = db.Column(
        db.Text,
        nullable=False
    )

    origin_location = db.Column(
        db.String(100),
        nullable=False
    )

    region_served = db.Column(
        db.String(100),
        nullable=False
    )

    founder = db.Column(
        db.String(100),
        nullable=False
    )

    year_founded = db.Column(
        db.Integer,
        nullable=False
    )

    annual_revenue = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    wikilink = db.Column(
        db.String(200)
    )

    website_link = db.Column(
        db.String(200)
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey('category.id'),
        nullable=False
    )

    # Relationships
    category = db.relationship(
        'Category',
        backref=db.backref('charities', lazy=True)
    )

    keywords = db.relationship(
        'Keyword',
        secondary='charity_keyword',
        backref=db.backref('charities', lazy=True)
    )

    def __repr__(self):
        return f"Charity('{self.name}', '{self.goal}', '{self.region_served}')"

# Charity - Keyword relation
charity_keyword = db.Table('charity_keyword',
    db.Column('charity_id', db.Integer, db.ForeignKey('charity.id'), primary_key=True),
    db.Column('keyword_id', db.Integer, db.ForeignKey('keyword.id'), primary_key=True)
)
