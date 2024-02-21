import unittest
import sqlite3
from data_collector import collect_data


class TestDataCollector(unittest.TestCase):
    def test_collect_data(self):
        # Call the collect_data function
        collect_data()

        # Connect to the SQLite database
        con = sqlite3.connect('activity.db')
        cur = con.cursor()

        # Query the database to fetch all activity data
        cur.execute("SELECT * FROM activities")
        data = cur.fetchall()

        # Check if correct number of activity data fetched, this will change as activities are added
        self.assertEqual(len(data), 76)


if __name__ == '__main__':
    unittest.main()
