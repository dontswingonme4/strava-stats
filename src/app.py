from flask import Flask, render_template
# from src.data_collector import collect_data  # When deploying to Heroku
# from src.data_analyzer import analyze_data  # When deploying to Heroku
from data_collector import collect_data  # When running locally
from data_analyzer import analyze_data  # When running locally
import sqlite3

app = Flask(__name__)


@app.route("/")
def main():
    # Call collect_data function to get latest data
    collect_data()
    # Call analyze_data function to get the number of activities
    num_activities = analyze_data()
    return render_template('main.html', num_activities=num_activities)


@app.route("/get_latest_activity", methods=["POST"])
def get_latest_activity():
    collect_data()
    return "Activity Data Up to Date, press back button on browser"


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
