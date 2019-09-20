import mysql.connector  as conector
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)



@app.route("/validate", methods=["GET","POST"])
def validate():
    if (request.method=="POST"):
        username=request.form["uname"]
        password=request.form["pwd"]
        myconn = conector.connect(host = "localhost",
        user = "root",passwd = "115599",database = "myoffice")
        cur = myconn.cursor()
        cur.execute=('SELECT * from signup where usern = %s AND password = %s', (username, password))
        myconn.commit()
        if (username == usern) and (password == password):
            return redirect("/home")
        else:
            return "access denied"

'''@app.route("/validate", methods=["GET","POST"])
def validate():
    if (request.method=="POST"):
        uname=request.form["uname"]
        pwd=request.form["pwd"]
        if(uname == "Admin" and pwd == "python"):
            return "Hello "+uname
        else:
            return redirect(url_for("demo"))'''

@app.route("/home")
def home():
    return render_template("home2.html")

@app.route("/backpack")
def backpack():
    return render_template("backpack.html")

@app.route("/shoes")
def shoes():
    return render_template("shoes.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if (request.method=="GET"):
        return render_template("signup.html")
    else:
        usern = request.form["Username"]
        email = request.form["email"]
        password = request.form["psw"]
        repassword = request.form["psw-repeat"]
        myconn = conector.connect(host = "localhost",
            user = "root",passwd = "115599",database = "myoffice")
        cur = myconn.cursor()
        sql = "insert into signup values (%s,%s,%s,%s)"
        val = (usern,email,password, repassword)
        cur.execute(sql,val)    
        myconn.commit()
        myconn.close()
        return redirect("/signup")

@app.route("/contact",methods=["GET","POST"])
def contact():
    if(request.method=="GET"):
        return render_template("contact.html")
    else:
        fn = request.form["firstname"]
        ln = request.form["lastname"]
        contact = request.form["cnum"]
        email = request.form["email"]
        location = request.form["country"]
        myconn = conector.connect(host = "localhost",
            user = "root",passwd = "115599",database = "myoffice")
        cur = myconn.cursor()
        sql = "insert into contact values (%s,%s,%s,%s,%s)"
        val = (fn,ln,contact, email, location)
        cur.execute(sql,val)    
        myconn.commit()
        myconn.close()
        return redirect("/contact")


if (__name__ == "__main__"):
    app.run(debug=True,port=7000)
