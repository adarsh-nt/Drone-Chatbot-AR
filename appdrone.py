from flask import Flask, render_template, request, jsonify
import sys
import os

# Add the path of your script if it's in a different directory
sys.path.append('C:\Users\91807\Downloads\VRChatbot.ipynb')

# Import functions from your Python chatbot script
from chatbot_script import get_response  # Replace with actual import

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('drone1.html')

@app.route('/get_response', methods=['POST'])
def get_chatbot_response():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
