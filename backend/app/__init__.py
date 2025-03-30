from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

from . import routes, auth  # Import routes and auth to register them with the app 