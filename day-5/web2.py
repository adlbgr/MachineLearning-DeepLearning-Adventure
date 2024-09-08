from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
             host='localhost',
             user='root',
             password='',
             database='ders'
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("/signup.html")
@app.route("/kayitol", methods=["POST"])
def kayitol():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO kullanici_bilgisi (name,email, password) VALUES(%s,%s,%s)", (name,email, password))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for("index"))

cursor=db.cursor()
name="ahmet"
email= 'ahmet@ahmet'
password="5678"
user_id=1

#cursor.execute("UPDATE kullanici_bilgisi SET name=%s, email=%s , password=%s WHERE id=%s", (name,email,password,user_id))
db.commit()


cursor.execute('DELETE FROM kullanici_bilgisi WHERE id=%s',(user_id,))
db.commit()
db.close()
if __name__ =="__main__":
    app.run(debug=True)