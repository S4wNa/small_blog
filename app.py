from flask import Flask, render_template,request, redirect, url_for
import datetime
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

from model import Section

app = Flask(__name__)

# Utiliser une variable d'environnement avec une valeur par défaut
database_path = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.sqlite'))

# Si l'URL commence par "postgres://" (format Heroku/Render), le convertir en "postgresql://"
if database_path.startswith("postgres://"):
    database_path = database_path.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title-i")
        entry_content = request.form.get("content")
        current_time = datetime.datetime.utcnow()
        new_section = Section(title=title, entry_content=entry_content, date=current_time)
        db.session.add(new_section)
        db.session.commit()
        return redirect(url_for("index"))
    
    sections = Section.query.order_by(Section.date.desc()).all()
    return render_template("index.html", sections = sections)