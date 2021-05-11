from flask import Flask, render_template  
app = Flask(__name__) 

@app.route("/")
def checkerbox():
    return render_template('index.html', cols = 8, rows = 8)


@app.route("/<num>")
def checkerbox1(num):
    return render_template('index.html', cols = 8, rows= int(num))


@app.route("/<num1>/<num2>")
def checkerbox2(num1,num2):
    return render_template('index.html', cols = int(num1), rows = int(num2))


@app.route("/<num1>/<num2>/<col1>/<col2>")
def checkerbox3(num1,num2,col1,col2):
    return render_template('index.html', cols = int(num1), rows = int(num2), col1=col1, col2=col2)


if __name__=="__main__":      
    app.run(debug=True)