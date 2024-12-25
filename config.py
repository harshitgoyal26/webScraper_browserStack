import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# BrowserStack Credentials
BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME", "your_browserstack_username")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY", "your_browserstack_access_key")

# Translation API 
TRANSLATION_API_KEY = os.getenv("TRANSLATION_API_KEY", "your_translation_api_key")

# Application Settings
BASE_URL = "https://elpais.com/opinion"
IMAGE_SAVE_PATH = "./resources/images/"

if not os.path.exists(IMAGE_SAVE_PATH ):
    os.makedirs(IMAGE_SAVE_PATH )
