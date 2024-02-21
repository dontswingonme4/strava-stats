import unittest
from data_analyzer import analyze_data


class TestDataAnalyzer(unittest.TestCase):
    def test_analyze_data(self):
        # Call the analyze_data function
        num_activities = analyze_data()

        # Test if num_activities is an integer
        self.assertIsInstance(num_activities, int)

        # Test if num_activities is non-negative
        self.assertGreaterEqual(num_activities, 0)


if __name__ == '__main__':
    unittest.main()
