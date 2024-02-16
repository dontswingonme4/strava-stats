from flask import Flask, render_template
from data_collector import collect_data
import sqlite3

app = Flask(__name__)


@app.route("/")
def main():
    return '''
     <form action="/get_latest_activity" method="POST">
         <input type="submit" value="Get Latest Activity Data">
     </form>
     <br>
     <a href="/view_data">View Activity Data</a>
     '''


@app.route("/get_latest_activity", methods=["POST"])
def get_latest_activity():
    collect_data()
    return "Activity Data Up to Date"


@app.route("/view_data")
def view_data():
    # Connect to the SQLite database
    con = sqlite3.connect('activity.db')
    cur = con.cursor()

    # Query the database to fetch all activity data
    cur.execute("SELECT * FROM activities")
    data = cur.fetchall()

    # Close the database connection
    con.close()

    # Render a template to display the data
    return render_template('view_data.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
