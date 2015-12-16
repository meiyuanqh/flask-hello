#coding=utf-8
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 align=\"center\">欢迎测试!<h1><h3 align=\"center\">Powered by flask and python</h3>"

@app.route("/meiyuan")
def hellomeiyuan():
    return "<h1 align=\"center\">你好 meiyuan!<h1><h3 align=\"center\">Powered by flask and python</h3>"

if __name__ == "__main__":
    app.run("0.0.0.0", 80)
