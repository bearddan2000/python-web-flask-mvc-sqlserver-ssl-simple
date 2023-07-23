from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://sa:z!x<?oB1ab@db/master"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

class DogModel(db.Model):
    __tablename__ = 'dog'

    id = db.Column(db.Integer, primary_key=True)
    breed = db.Column(db.String())
    color = db.Column(db.String())

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

@app.route('/', methods=['GET'])
def hello():
    return render_template("index.html")

@app.route('/dogs', methods=['GET'])
def handle_dogs():
    dogs = DogModel.query.all()
    results = [
        {
            "id": dog.id,
            "breed": dog.breed,
            "color": dog.color
        } for dog in dogs]

    return {"results": results}

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
