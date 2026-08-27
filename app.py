from flask import Flask,  render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/") # "/" = homepage URL
def home(): 
    return render_template("index.html")

#this is saying: whenever someone visits homepage URL, show the HTML page

@app.route("/gallery")
def gallery(): 
    return render_template("gallery.html")

@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        clothing_type = request.form["clothingType"]
        color = request.form["color"]
        size = request.form["size"]
        measurements = request.form["measurements"]
        description = request.form["description"]

        # Create Table
        conn = sqlite3.connect('data.db') # conn = connection
        table_create_query = '''
            CREATE TABLE IF NOT EXISTS Request_Form_Data (
                name TEXT, 
                email TEXT, 
                clothing_type TEXT, 
                color TEXT, 
                size TEXT, 
                measurements TEXT, 
                description TEXT
            )
        '''

        conn.execute(table_create_query)

        # Insert Data
        data_insert_query = '''
        INSERT INTO Request_Form_Data (
            name, 
            email, 
            clothing_type, 
            color, 
            size, 
            measurements, 
            description
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        data_insert_tuple = (name, email, clothing_type, color, size, measurements, description)
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)

        conn.commit()
        conn.close()
    
    return render_template("order.html")

@app.route("/about")
def about(): 
    return render_template("about.html")

@app.route("/admin")
def admin(): 
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row

    orders = conn.execute(
        "SELECT * FROM Request_Form_Data"
    ).fetchall()

    conn.close()

    return render_template("admin.html", orders=orders)

#this is saying: if I run this file directly, start the Flask web server
if __name__ == "__main__": # running "python app.py" sets __name__ = "__main__"
    app.run(debug=True) # starts local server




