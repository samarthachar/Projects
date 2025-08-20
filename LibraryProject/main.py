from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy


class Base(DeclarativeBase):
    pass

app = Flask(__name__)
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()




@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add",  methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["name"].strip().title(), author=request.form["author"].strip().title(), rating=float(request.form["rating"].strip().split("/")[0]))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get("id")
    end_result = db.session.execute(db.select(Book).where(Book.id == book_id))
    book = end_result.scalar()

    if request.method == "POST":
        book_id = request.args.get("id")
        book.rating = float(request.form["rating"].strip().split("/")[0])
        db.session.commit()
        return redirect(url_for("home"))


    return render_template("edit.html", book=book)


@app.route('/delete')
def delete():
    book_id = request.args.get("id")
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

