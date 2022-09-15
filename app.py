from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello world, WWW!'

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/cryptohospital')
def cryptohospital():
    return render_template('cryptohospital.html')
    # import to note that it is going to look for the .html files in a folder called templates

if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=8000)
