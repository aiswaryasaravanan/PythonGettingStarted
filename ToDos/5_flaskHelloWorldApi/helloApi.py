from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is home page"

@app.route('/greet/')
def greet():
    return "Hello world"

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0',port="3000")
