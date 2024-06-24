from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

@app.route("/name")
def name():
	return "<h1>my name is Lee SungHee</h1>"

@app.route("/age")
def age():
	return "<h1> 24 year's old</h1>" ## 고정된 값을 보여주는 정적 라우팅

if __name__ == "__main__": # 터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다
	app.run(host="0.0.0.0", port="10111", debug=True) #실행을 위한 명련문으로 보면 된다
