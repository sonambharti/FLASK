from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>In Index</h1>'

@app.route('/success/<int:score>')
def success(score):
    return f"This person passed with {str(score)} score"

@app.route('/fail/<int:score>')
def fail(score):
    return f"This person failed with {str(score)} score"



if __name__ == "__main__":
    app.run(debug=True)
