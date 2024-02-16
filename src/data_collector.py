import requests
import urllib3
import sqlite3


def collect_data():
    # Establish connection to SQLite database
    con = sqlite3.connect('activity.db')
    cur = con.cursor()

    # Disable warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Define API endpoints and authentication parameters
    activities_url = "https://www.strava.com/api/v3/athlete/activities"
    auth_url = "https://www.strava.com/oauth/token"

    payload = {
        'client_id': "120789",
        'client_secret': "3592d382fe2d7a75ca32942963f4a051b2738020",
        'refresh_token': "f30d3185f893f96c985514e698edc62692686e97",  # refresh token doesnt expire
        'grant_type': "refresh_token",
        'f': 'json'
    }

    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']

    # Prepare API request headers and parameters
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1}

    # Get data from Strava API
    my_dataset = requests.get(activities_url, headers=header, params=param).json()

    # Create activities table if not exists
    create_table_query = """
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        average_heartrate REAL,
        start_date TEXT,
        sport_type TEXT,
        name TEXT
    );
    """
    cur.execute(create_table_query)

    # Define insert query
    insert_query = "INSERT INTO activities (average_heartrate, start_date, sport_type, name) VALUES (?, ?, ?, ?)"

    # Check for existing data in the database
    cur.execute("SELECT start_date FROM activities")
    existing_dates = [row[0] for row in cur.fetchall()]

    # Insert new data into the database
    for activity in my_dataset:
        start_date = activity.get('start_date', None)
        if start_date not in existing_dates:  # Check if data already exists
            average_heartrate = activity.get('average_heartrate', None)
            sport_type = activity.get('sport_type', None)
            name = activity.get('name', None)

            # Insert new data into the database
            cur.execute(insert_query, (average_heartrate, start_date, sport_type, name))

    # Commit changes and close connection
    con.commit()
    con.close()


if __name__ == "__main__":
    collect_data()  # If the script is run directly, collect data
