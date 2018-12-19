from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>서버가 html도 보내주나???</h1>"
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>첫번째 줄!!!</h1>
    <h2>두번째 줄!!</h2>
    """

@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", people=name)

@app.route("/cube/<int:num>")
def cube(num):
    triple = num*num*num
    return render_template("cube.html", numb = triple, num=num)
    
@app.route('/lunch')
def lunch():
    lunch_list = ["김치찌개","닭갈비","소고기","스테이크"]
    l = random.choice(lunch_list)
    return render_template("lunch.html", lun = l)
    
@app.route('/lotto')
def lotto():
    list = range(1,50)
    lot = random.sample(list,6)
    sor
    return render_template("lotto.html", lott = sort_lot)
    
@app.route('/naver')
def naver():
    return render_template("naver.html")