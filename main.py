from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/health-care")
def health_care():
    return render_template("health_care.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/retail")
def retail():
    return render_template("retail.html")

@app.route("/social-assistance")
def social_assistance():
    return render_template("social_assistance.html")

@app.route("/office")
def office():
    return render_template("office.html")

@app.route("/freelance")
def freelance():
    return render_template("freelance.html")

@app.route("/trainings")
def trainings():
    return render_template("trainings.html")

@app.route("/tests")
def tests():
    return render_template("tests.html")

@app.route("/retired-age-mothers")
def retired_age_mothers():
    return render_template("retired_age_mothers.html")

if __name__ == "__main__":
    app.run(debug=True)
    
