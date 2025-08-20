from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, length
import requests



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
from flask import Flask


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies_db.db'
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(500))


class EditForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 eg. 7.5', [DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired(), Length(max=250)])
    button = SubmitField(label="Done")


class AddForm(FlaskForm):
    title = StringField('Movie Title', [DataRequired(), Length(250)])
    button = SubmitField("Add Movie")

def sort_values_by_highest_key(data):
    sorted_items = sorted(data.items(), key=lambda x: float(x[0]), reverse=True)
    sorted_values = []

    for key, value in sorted_items:
        sorted_values.append(value)

    return sorted_values


@app.route("/")
def home():
    movies_dict = {}
    movies = Movie.query.all()
    for movie in movies:
        movies_dict[movie.rating] = movie

    ordered_movies = sort_values_by_highest_key(movies_dict)
    rank = 1
    for movie in ordered_movies:
        movie.ranking = rank
        rank += 1

    return render_template("index.html", movies=ordered_movies)

@app.route('/edit', methods=["POST", "GET"])
def edit():
    form = EditForm(request.form)
    movie = Movie.query.get_or_404(request.args.get("id", type=int))
    title = movie.title

    if request.method == "POST" and form.validate():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=form, title=title)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id", type=int)
    movie = Movie.query.get_or_404(movie_id)

    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('home'))



@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm(request.form)
    if request.method == "POST":
        url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNzFjODBlZWQ0MDY1Zjg4YjkzMDlmMzA3ODUzZmM3NyIsIm5iZiI6MTc1NTY4NzkyNy41NCwic3ViIjoiNjhhNWFiZjc0YjljZjI3YjA3M2U4NDJlIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.gj2IAborksYdSYannBsfFYwKGsvGb66gF6Ll8tn_aos"
        }
        params = {
            "query": form.title.data
        }

        response = requests.get(url,params=params, headers=headers)

        print(response.json()["results"])

        return render_template("select.html",data = response.json()["results"])
    return render_template("add.html", form=form)

@app.route('/get')
def get():
    mov_id = request.args.get("id")

    url = f"https://api.themoviedb.org/3/movie/{mov_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNzFjODBlZWQ0MDY1Zjg4YjkzMDlmMzA3ODUzZmM3NyIsIm5iZiI6MTc1NTY4NzkyNy41NCwic3ViIjoiNjhhNWFiZjc0YjljZjI3YjA3M2U4NDJlIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.gj2IAborksYdSYannBsfFYwKGsvGb66gF6Ll8tn_aos"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    new_movie = Movie(
        title = data["title"],
        img_url = f"https://image.tmdb.org/t/p/w500{data["poster_path"]}",
        year = data["release_date"][:4],
        description = data["overview"],
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
