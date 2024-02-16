from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/get_latest_activity" method="POST">
         <input type="submit" value="Get Latest Activity Data">
     </form>
     '''

@app.route("/get_latest_activity", methods=["POST"])
def get_latest_activity():
    # Call the function from your data collector Python file to collect data
    # Replace the '...' with the actual function call and logic
    # data_collector.collect_data()  # Example function call
    # If your data collector function returns True upon successful data collection, then:
    # if data_collector.collect_data():
    #     return "Activity Data Up to Date"
    # else:
    #     return "Failed to collect activity data. Please try again."

    # For now, let's assume the data collection is successful
    return "Activity Data Up to Date"

if __name__ == "__main__":
    app.run(debug=True)
