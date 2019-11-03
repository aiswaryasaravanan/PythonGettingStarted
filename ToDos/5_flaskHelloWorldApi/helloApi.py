from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "This is home page"

@app.route('/greet/')
def greet():
    return "Hello world"

@app.route('/home/<int:id>')
def myId(id):
    return 'hello my id is %d' % id

@app.route('/index/<string:content>')
def index(content):
    return render_template('index.html',name="Mapla",mssg=content)

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0',port="3000")
