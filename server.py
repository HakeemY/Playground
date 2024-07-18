from flask import Flask, render_template
app = Flask(__name__)


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/play')
def level1():
    return render_template('index1.html', num=3)

@app.route('/play/<int:num>')
def level2(num):
    return render_template('index1.html', num=num)

@app.route('/play/<int:num>/<color>')
def level3(num,color):
    return render_template('index1.html', num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)