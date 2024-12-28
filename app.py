from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)
@app.route("/home")
def home():
    return render_template('index.html')
@app.route("/robot1")
def robot1():
    return render_template('robot1.html')
@app.route("/robot2")
def robot2():
    return render_template('robot2.html')
@app.route("/robot3")    
def robot3():
    return render_template('robot3.html')
@app.route("/robot4")
def robot4():
    return render_template('robot4.html')

if __name__=="__main__":
    app.run(debug=True)
