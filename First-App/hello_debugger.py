from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Flask debugger</h1>'

@app.route('/members')
def members():
    return '<h3>In member</h3>'

if __name__ == "__main__":
    app.run(debug=True)



"""
Command to run the page:
flask --app First-App.hello_debugge
if app.run()
flask --app First-App.hello_debugger run --debug
"""
