import os



TRANSLATION_API_KEY = os.getenv("TRANSLATION_API_KEY", "your_translation_api_key")
IMAGE_SAVE_PATH = "./resources/images/"

if not os.path.exists(IMAGE_SAVE_PATH ):
    os.makedirs(IMAGE_SAVE_PATH )
