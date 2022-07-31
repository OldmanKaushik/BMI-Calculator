from flask import Flask, render_template,request,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("bmi.html")

@app.route("/display" , methods = ["POST"])
def bmi_cal():
    name = request.form["name_name"]
    age = int(request.form["age_name"])
    weight = int(request.form["weight_name"])
    height = float(request.form["height_name"])
    bmi = weight//(height**2)
    
    return "<img src = 'https://images.everydayhealth.com/images/diet-nutrition/weight/bmi-in-adults-722x406.jpg'>"+"<br>"+f"Hi {name}, your bmi is {bmi} , please check if you are normal or not!."

if __name__ == "__main__":
    app.run()


