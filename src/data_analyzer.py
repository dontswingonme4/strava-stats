import sqlite3


def analyze_data():
    # Connect to the SQLite database
    con = sqlite3.connect('activity.db')
    cur = con.cursor()

    # Query the database to fetch the count of activities
    cur.execute("SELECT COUNT(*) FROM activities")
    num_activities = cur.fetchone()[0]

    # Close the database connection
    con.close()

    return num_activities
