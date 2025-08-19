# import Flask(child class) from flask (parent class)
from flask import Flask,render_template, request, redirect, url_for, flash

# create a Flask object (server)
app = Flask(__name__)
# secret key for login
app.secret_key = "your_secret_key_here"

@app.route("/", methods=["POST","GET"])
def login():
    username = "harshitachhabria18"
    password = "harshita18"

    if request.method == "POST":
        if request.form.get("uname") == username and request.form.get("password") == password:
            return redirect(url_for("home"))
        else:
            flash("Incorrect Details! Enter Details Again", "error")
            return redirect(url_for("login"))

    return render_template("form.html")

# define a route where this app object will take the user once the app is run
@app.route("/home", methods=["GET","POST"])
def home():
    # if the form is submitted
    if request.method == "POST":
        # here request stores the input data in the form
        getdata = request.form.get('section')
        if getdata == "About Me":
            section_id = "About"
        elif getdata == "Skills":
            section_id = "Skills"
        elif getdata == "Projects":
            section_id = "Projects"
        elif getdata == "Contact Section":
            section_id = "Contact"
        else:
            section_id = None
        
        # Load the index.html page after POST (submitting the form)
        return render_template("index.html", section_id=section_id)

    # here render_template is used to load the html page on the server
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)