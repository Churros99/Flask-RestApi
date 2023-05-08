from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///database\\streamers.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1> Welcome Home </h1>"


if __name__ == '__main__':
    app.run(debug=True, port=4000)

