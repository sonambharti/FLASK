from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome to the Flask world</h1>'

if __name__ == "__main__":
    app.run()

"""
Command to run the page:
flask --app First-App.welcome run --debug
"""