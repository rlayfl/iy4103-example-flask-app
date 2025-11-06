from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///colchester.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)

    comments = db.relationship('Comment', backref='user', lazy=True)
    likes = db.relationship('Like', backref='user', lazy=True)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    comments = db.relationship('Comment', backref='place', lazy=True)
    likes = db.relationship('Like', backref='place', lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

@app.route('/example')
def example():
    return render_template('example.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# This is just a simple page which shows how to get data onto your web pages, making it a data-driven website
@app.route('/data')
def data():
    users = User.query.all()
    places = Place.query.all()
    comments = Comment.query.all()
    likes = Like.query.all()
    return render_template('data.html',
                           users=users,
                           places=places,
                           comments=comments,
                           likes=likes)


@app.route('/uploadContact', methods=['POST'])
def upload_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    marketing = request.form.get('marketing_opt_in')
    
    print(name, phone, email, marketing)

    return f"Received: {name}, {phone}, {email}, Opt-in: {marketing}"

if __name__ == '__main__':
    app.run(debug=True)
