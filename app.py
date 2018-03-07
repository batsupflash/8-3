from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/pick')
def func_name():
    return render_template('pick.html')
@app.route('/khong')
def khong():
    return render_template('khong.html')
@app.route('/co')
def co():
    return render_template('co.html')

if __name__ == '__main__':
  app.run(debug=True)
