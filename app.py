from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Import functions for creating and updating assistants
from create_assistant import create_assistant
from update_assistant import update_assistant
# Import function for managing chat
from chat import start_chat

if __name__ == '__main__':
    # Create and update assistant
    create_assistant()
    update_assistant()

    # Start chat
    start_chat()

    # Run Flask app
    app.run(debug=True)
