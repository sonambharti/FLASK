from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome To University</h1>'

@app.route('/success/<int:score>')
def success(score):
    return f"This person passed with {str(score)} score"

@app.route('/fail/<int:score>')
def fail(score):
    return f"This person failed with {str(score)} score"

### Result checker
@app.route('/result/<int:marks>')
def marks(marks):
    result = ""
    if marks<35:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))



if __name__ == "__main__":
    app.run(debug=True)
