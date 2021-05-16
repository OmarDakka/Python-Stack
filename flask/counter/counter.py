from flask import Flask, render_template, session,redirect
app = Flask(__name__) 
app.secret_key = 'KEEP IT SAFE NIGGA'



@app.route("/")
def main():
    if 'counter' not in session:
        session["counter"] =0
    session['counter'] += 1
    return render_template("index.html", visit= str(session["counter"]))


@app.route("/add_two")
def addTwo():
    session['counter'] += 1
    return redirect ("/")

@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect ("/")

if __name__=="__main__":  
    app.run(debug=True) 