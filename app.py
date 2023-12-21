from flask import Flask, render_template, request
import find_word

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("Hello World")
    return "Hello! 欢迎进入Flask世界！"


@app.route("/index", methods=["GET", "POST"])
def index():
    w = request.form["word"]
    le = request.form["letters"]
    res = str(find_word.find_word(w, le))
    return render_template('result.html',
                           title='查看搜索的结果', word=w, letters=le, result=res)


@app.route('/entry')
def entry():
    return render_template('entry.html', title='欢迎来到Flask的世界！')


if __name__ == '__main__':
    app.run(debug=True)
