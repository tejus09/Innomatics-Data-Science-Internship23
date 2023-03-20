#Import Necessary Modules
from flask import *
import re

#App Object
app = Flask(__name__)

#Routes
@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "GET":
        return render_template('home.html')

@app.route('/regex', methods=["GET", "POST"])
def regex_page():
    test_string = request.form.get("test_string")
    regex = request.form.get("regex")
    matches = re.findall(regex, test_string)
    return str(matches)


#Run App

if __name__ == "__main__":
    app.run(debug=True)