import populartimes
import os
from flask import Flask, render_template, jsonify, redirect, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/popularplace', methods=['GET'])
def predict_stuff():

    y = populartimes.get(os.environ.get("KEY"), ["bar"], (48.132986, 11.566126), (48.142199, 11.580047))
    print(y)

#     both = {
#     	"x" : x,
#     	"y" : y
#     }

    return jsonify(y)
    
if __name__ == "__main__":
    app.run()

# to start this app up you do python3 populartimes.py
# in the browser you would go to localhost:5000/popularplace


#$ export FLASK_APP=yourapp
#$ export FLASK_ENV=development
#and then you start the server with:
#$ flask run